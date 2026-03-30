import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('MatPlotLib\Learning\pokedex.csv', skipinitialspace=True)

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color = 'red', edgecolor = "black")

plt.title('Number of pokemons by type1', fontsize = 20, family = 'arial')
plt.xlabel('Count')
plt.tight_layout()
plt.show()