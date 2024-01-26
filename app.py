import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Wczytaj dane z pliku CSV
df = pd.read_csv('Student Mental health.csv')

# Zmień nazwy kolumn
newnames = ["Timestamp", "Gender", "Age", "Major", "Year", "CGPA", "Married", "Depression", "Anxiety", "Panic Attacks", "Treated"]
df.columns = newnames

# Przekształć kolumny na wartości binarne
def to_binary(d):
    if d == "Yes": return 1
    if d == "No": return 0

df["Married"] = df["Married"].apply(to_binary)
df["Depression"] = df["Depression"].apply(to_binary)
df["Anxiety"] = df["Anxiety"].apply(to_binary)
df["Panic Attacks"] = df["Panic Attacks"].apply(to_binary)
df["Treated"] = df["Treated"].apply(to_binary)

df["Year"] = df["Year"].str[-1:]

# Wyświetl dane po przekształceniach
df.head()

# Wykres Venna
depressed = df[df['Depression'] == 1]
anxious = df[df['Anxiety'] == 1]
panicking = df[df['Panic Attacks'] == 1]

venn3(subsets=[set(depressed.index), set(anxious.index), set(panicking.index)],
      set_labels=("Depressed", "Anxious", "Having Panic Attacks"),
      set_colors=("orange", "purple", "green"),
      alpha=0.7)

plt.title("Conditions", fontsize=14)
plt.show()

# Wykres słupkowy
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

colors = ['yellow', 'gray']  # Zdefiniuj wybrane kolory tutaj

fig, ax = plt.subplots(figsize=(10, 3))
bottom = np.zeros(7)  # Dostosuj do 8, jeśli masz 8 etykiet teraz

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

