import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify

# Read CSV file
df = pd.read_csv('Student Mental health.csv')

# Count of each condition
condition_counts = df[['Do you have Depression?', 'Do you have Anxiety?', 'Do you have Panic attack?']].apply(pd.value_counts)

# Bar plot for condition counts
condition_counts.plot(kind='bar', stacked=True)
plt.title('Counts of Conditions')
plt.xlabel('Condition')
plt.ylabel('Count')
plt.show()

# Flask application
app = Flask(__name__)

# FHIR-like data
fhir_data = [
    {"patientId": i, "condition": condition, "count": count}
    for i, (condition, count) in enumerate(zip(condition_counts.index, condition_counts.sum(axis=1)))
]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fhir', methods=['GET', 'POST'])
def fhir_api():
    if request.method == 'GET':
        return jsonify(fhir_data)
    elif request.method == 'POST':
        new_record = request.json
        fhir_data.append(new_record)
        return jsonify({"status": "Record added successfully"})

if __name__ == '__main__':
    app.run(debug=True)
