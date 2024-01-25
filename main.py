import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import numpy as np
import pandas as pd

data = pd.read_csv('Student Mental health.csv')

# Sample variables for the bar chart
labels = ['Depressed', 'Anxious', 'Having Panic \nAttacks',
          'Depressed and \nAnxious', 'Depressed and Having \nPanic Attacks',
          'Anxious and Having \nPanic Attacks', 'All Three']

gender_counts = {
    "Male": [
        (depressed["Gender"] == "Male").sum(),
        (anxious["Gender"] == "Male").sum(),
        (panicking["Gender"] == "Male").sum(),
        ((depressed["Depression"] == "Yes") & (anxious["Anxiety"] == "Yes")).sum(),
        ((depressed["Depression"] == "Yes") & (panicking["Panic_Attack"] == "Yes")).sum(),
        ((anxious["Anxiety"] == "Yes") & (panicking["Panic_Attack"] == "Yes")).sum(),
        ((depressed["Depression"] == "Yes") & (anxious["Anxiety"] == "Yes") & (panicking["Panic_Attack"] == "Yes")).sum(),
    ],

    "Female": [
        (depressed["Gender"] == "Female").sum(),
        (anxious["Gender"] == "Female").sum(),
        (panicking["Gender"] == "Female").sum(),
        ((depressed["Depression"] == "Yes") & (anxious["Anxiety"] == "Yes")).sum(),
        ((depressed["Depression"] == "Yes") & (panicking["Panic_Attack"] == "Yes")).sum(),
        ((anxious["Anxiety"] == "Yes") & (panicking["Panic_Attack"] == "Yes")).sum(),
        ((depressed["Depression"] == "Yes") & (anxious["Anxiety"] == "Yes") & (panicking["Panic_Attack"] == "Yes")).sum(),
    ]
}

colors = ['yellow', 'gray']  # Define your desired colors here

# Plotting Venn Diagram
venn3(subsets=[set(depressed.index), set(anxious.index), set(panicking.index)],
      set_labels=("Depressed", "Anxious", "Having Panic Attacks"),
      set_colors=("orange", "purple", "green"),
      alpha=0.9)
plt.title("Conditions", fontsize=16)
plt.show()

# Plotting Bar Chart
fig, ax = plt.subplots(figsize=(10, 3))
bottom = np.zeros(7)

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
