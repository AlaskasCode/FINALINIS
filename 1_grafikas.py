import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams["figure.figsize"] = (15, 9)
# Istraukem 2 csv failus
df_camelia = pd.read_csv('modified_camelia.csv')
df_gintarine = pd.read_csv('modified_gintarine.csv')
# Ieskome bendros kompanijos tarp 2 Data Frame
common_companies = set(df_camelia['Kompanija']).intersection(df_gintarine['Kompanija'])
# Filtruojame kompanijos/Filter data for common companies
common_camelia = df_camelia[df_camelia['Kompanija'].isin(common_companies)]
common_gintarine = df_gintarine[df_gintarine['Kompanija'].isin(common_companies)]
# Group by 'Kompanija' and calculate the count of items for common companies
grouped_camelia = common_camelia.groupby('Kompanija').size().reset_index(name='ItemCount_Camelia')
grouped_gintarine = common_gintarine.groupby('Kompanija').size().reset_index(name='ItemCount_Gintarine')
# Merge the two dataframes on 'Kompanija'
merged_grouped = pd.merge(grouped_camelia, grouped_gintarine, on='Kompanija')
# Plot the bar graphs for common companies side by side
width = 0.35  # Width of the bars
ind = np.arange(len(merged_grouped['Kompanija']))
plt.bar(ind, merged_grouped['ItemCount_Camelia'], width, label='Camelia', color='pink')
plt.bar(ind + width, merged_grouped['ItemCount_Gintarine'], width, label='Gintarine', color='skyblue', alpha=0.7)
# Add annotations above the bars
for i, value in enumerate(merged_grouped['ItemCount_Camelia']):
    plt.text(i, value + 0.1, str(value), ha='center', va='bottom')
for i, value in enumerate(merged_grouped['ItemCount_Gintarine']):
    plt.text(i + width, value + 0.1, str(value), ha='center', va='bottom')
plt.xlabel('Kompanija')
plt.ylabel('Item Count')
plt.title('Item Count for Matching Companies - Camelia vs Gintarine')
plt.xticks(ind + width / 2, merged_grouped['Kompanija'], rotation=30, ha='right')
plt.legend()
plt.show()