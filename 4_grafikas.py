import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Nuskaitome pirmojo CSV failo duomenis
duomenys1 = pd.read_csv('camelia_multivitaminai.csv')

# Nuskaitome antrojo CSV failo duomenis
duomenys2 = pd.read_csv('gintarine_multivitaminai.csv')

# Nurodome norimas kompanijas
norimos_kompanijos = ['ROYAL', 'NEW NORDIC', 'RAW POWDERS']
norimos_kompanijos1 = ['CENTRUM', 'AMBIO', 'SAPIENS']


# Filtruojame duomenis pagal norimas kompanijas ir skirtingas vaistines
filtruoti_duomenys1 = duomenys1[duomenys1['Kompanija'].isin(norimos_kompanijos)]
filtruoti_duomenys2 = duomenys2[duomenys2['Kompanija'].isin(norimos_kompanijos)]
filtruoti_duomenys3 = duomenys2[duomenys2['Kompanija'].isin(norimos_kompanijos1)]


# Apskaičiuojame kiekvienos kompanijos eilučių skaičių
eiluciu_skaiciai1 = filtruoti_duomenys1['Kompanija'].value_counts()
eiluciu_skaiciai2 = filtruoti_duomenys2['Kompanija'].value_counts()
eiluciu_skaiciai3 = filtruoti_duomenys3['Kompanija'].value_counts()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

# Pirmoji stulpelinė diagrama
axes[0].bar(eiluciu_skaiciai3.index, eiluciu_skaiciai3, color='skyblue')
axes[0].set_title('Gintarine: Vitaminu gamintojai, kuriu nera Camelijos vaistineje')
axes[0].set_xlabel('Tik Gintarine')
axes[0].set_ylabel('Kiekis')

bar_width = 0.4
index = np.arange(len(norimos_kompanijos))
norimos_kompanijos = eiluciu_skaiciai1.index.union(eiluciu_skaiciai2.index)

# Antroji stulpelinė diagrama
plt.bar(index, eiluciu_skaiciai1, label='Camelia', color='pink', width=bar_width)
plt.bar(index + bar_width, eiluciu_skaiciai2, label='Gintarine', color='skyblue', width=bar_width)

plt.title('Vienodu vitaminu gamintoju pasirinkimas Camelijos ir Gintarineje vaistinese')
plt.xlabel('Camelia ir Gintarine')
plt.ylabel('Kiekis')
plt.xticks(index + bar_width / 2, norimos_kompanijos)
plt.legend()

fig.tight_layout()

plt.show()



