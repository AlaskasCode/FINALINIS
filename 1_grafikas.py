import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Nustatome diagramos dydį
plt.rcParams["figure.figsize"] = (15, 9)

# Įtraukiame du CSV failus
df_camelia = pd.read_csv('modified_camelia.csv')
df_gintarine = pd.read_csv('modified_gintarine.csv')

# Ieškome bendrų įmonių tarp dviejų duomenų rinkinių
common_companies = set(df_camelia['Kompanija']).intersection(df_gintarine['Kompanija'])

# Filtruojame bendras įmones
common_camelia = df_camelia[df_camelia['Kompanija'].isin(common_companies)]
common_gintarine = df_gintarine[df_gintarine['Kompanija'].isin(common_companies)]

# Grupuojame pagal 'Kompanija' ir skaičiuojame prekių kiekį
grouped_camelia = common_camelia.groupby('Kompanija').size().reset_index(name='ItemCount_Camelia')
grouped_gintarine = common_gintarine.groupby('Kompanija').size().reset_index(name='ItemCount_Gintarine')

# Sujungiame duomenis pagal stulpelį 'Kompanija'
merged_grouped = pd.merge(grouped_camelia, grouped_gintarine, on='Kompanija')

# Braižome stulpelinę diagramą
width = 0.35  # Stulpelių plotis
ind = np.arange(len(merged_grouped['Kompanija']))
plt.bar(ind, merged_grouped['ItemCount_Camelia'], width, label='Camelia', color='pink')
plt.bar(ind + width, merged_grouped['ItemCount_Gintarine'], width, label='Gintarine', color='skyblue', alpha=0.7)

# Nurodome tekstines reikšmes virš kiekvieno stulpelio
for i, value in enumerate(merged_grouped['ItemCount_Camelia']):
    plt.text(i, value + 0.1, str(value), ha='center', va='bottom')
for i, value in enumerate(merged_grouped['ItemCount_Gintarine']):
    plt.text(i + width, value + 0.1, str(value), ha='center', va='bottom')
    
# Nurodome ašių pavadinimus
plt.xlabel('Kompanija')
plt.ylabel('Prekių kiekis')
plt.title('Prekių kiekis tarp bendrų įmonių - Camelia vs Gintarine')
plt.xticks(ind + width / 2, merged_grouped['Kompanija'], rotation=30, ha='right')
plt.legend()

# Parodome diagramą
plt.show()
