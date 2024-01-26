import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Read data from the CSV file
df = pd.read_csv('Student Mental health.csv')

# Rename columns
newnames = ["Timestamp", "Gender", "Age", "Major", "Year", "CGPA", "Married", "Depression", "Anxiety", "Panic Attacks", "Treated"]
df.columns = newnames

# Convert columns to binary values
def to_binary(d):
    if d == "Yes": return 1
    if d == "No": return 0

df["Married"] = df["Married"].apply(to_binary)
df["Depression"] = df["Depression"].apply(to_binary)
df["Anxiety"] = df["Anxiety"].apply(to_binary)
df["Panic Attacks"] = df["Panic Attacks"].apply(to_binary)
df["Treated"] = df["Treated"].apply(to_binary)

df["Year"] = df["Year"].str[-1:]

# Display data after transformations
df.head()

# Define additional DataFrames here
only_depressed = depressed[(depressed["Anxiety"] == 0) & (depressed["Panic Attacks"] == 0)]
only_anxious = anxious[(anxious["Depression"] == 0) & (anxious["Panic Attacks"] == 0)]
only_panicking = panicking[(panicking["Depression"] == 0) & (panicking["Anxiety"] == 0)]
depressed_anxious = depressed[(depressed["Anxiety"] == 1) & (depressed["Panic Attacks"] == 0)]
depressed_panicking = depressed[(depressed["Anxiety"] == 0) & (depressed["Panic Attacks"] == 1)]
anxious_panicking = anxious[(anxious["Depression"] == 0) & (anxious["Panic Attacks"] == 1)]
all_three = has_condition[(has_condition["Depression"] == 1) & (has_condition["Anxiety"] == 1) & (has_condition["Panic Attacks"] == 1)]

# Venn diagram
depressed = df[df['Depression'] == 1]
anxious = df[df['Anxiety'] == 1]
panicking = df[df['Panic Attacks'] == 1]

venn3(subsets=[set(depressed.index), set(anxious.index), set(panicking.index)],
      set_labels=("Depressed", "Anxious", "Having Panic Attacks"),
      set_colors=("orange", "purple", "green"),
      alpha=0.7)

plt.title("Conditions", fontsize=14)
plt.show()

# Bar chart
labels = ['Depressed', 'Anxious', 'Having Panic Attacks',
          'Depressed and Anxious', 'Depressed and Having Panic Attacks',
          'Anxious and Having Panic Attacks', 'All Three']

gender_counts = {
    "Male": [
        (only_depressed["Gender"] == "Male").sum(),
        (only_anxious["Gender"] == "Male").sum(),
        (only_panicking["Gender"] == "Male").sum(),
        (depressed_anxious["Gender"] == "Male").sum(),
        (depressed_panicking["Gender"] == "Male").sum(),
        (anxious_panicking["Gender"] == "Male").sum(),
        (all_three["Gender"] == "Male").sum(),
    ],
    "Female": [
        (only_depressed["Gender"] == "Female").sum(),
        (only_anxious["Gender"] == "Female").sum(),
        (only_panicking["Gender"] == "Female").sum(),
        (depressed_anxious["Gender"] == "Female").sum(),
        (depressed_panicking["Gender"] == "Female").sum(),
        (anxious_panicking["Gender"] == "Female").sum(),
        (all_three["Gender"] == "Female").sum(),
    ]
}

colors = ['yellow', 'gray']  # Define your desired colors here

fig, ax = plt.subplots(figsize=(10, 3))
bottom = np.zeros(7)  # Adjust to 8 since you have 8 labels now

for gender, gender_count in gender_counts.items():
    p = ax.bar(labels,
               gender_count,
               width=0.8,
               label=gender,
               bottom=bottom)
    bottom += gender_count
    ax.bar_label(container=p,
                 label_type='center',
                 fontsize=10)

ax.set_title("Condition by Gender", fontsize=20)
plt.xticks(fontsize=8, ha='right', rotation=20)
ax.legend()
plt.show()

