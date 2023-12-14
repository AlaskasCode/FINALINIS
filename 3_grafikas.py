import pandas as pd
import matplotlib.pyplot as plt
# Nuskaityti duomenis iš CSV failo
duomenys = pd.read_csv('combined_multivitaminai.csv')

# Ištraukti kainas iš Camelija vaistinės
camelija_kainos = duomenys['Iprastine kaina camelia'].str.replace(',', '.').astype(float)

# Ištraukti kainas iš Gintarinės vaistinės
gintarine_kainos = duomenys['Iprastine kaina gintarine'].str.replace(',', '.').astype(float)

# Paskaičiuoti vidutinę kainą kiekvienai vaistinei
maziausia_camelija_kaina = camelija_kainos.min()
maziausia_gintarine_kaina = gintarine_kainos.min()

didziausia_camelija_kaina = camelija_kainos.max()
didziausia_gintarine_kaina = gintarine_kainos.max()

# Paskaičiuoti vidutinę kainą kiekvienai vaistinei
vidutine_camelija_kaina = camelija_kainos.mean()
vidutine_gintarine_kaina = gintarine_kainos.mean()

# Palyginti max ir min kainos
print(f"Min kaina Camelijoje: {maziausia_camelija_kaina}")
print(f"Min kaina Gintarinėje: {maziausia_gintarine_kaina}")
print(f"Max kaina Camelijoje: {didziausia_camelija_kaina}")
print(f"Max kaina Gintarinėje: {didziausia_gintarine_kaina}")
print(f"Vidutinė kaina Camelijoje: {vidutine_camelija_kaina}")
print(f"Vidutinė kaina Gintarinėje: {vidutine_gintarine_kaina}")



# Sukurti stulpelinį grafiką
fig, ax = plt.subplots(figsize=(10, 6))

# Pridėkite stulpelius su spalvomis
bars = ax.bar(['Camelia (min)', 'Gintarinė (min)', 'Camelia (max)', 'Gintarinė (max)', 'Cameliia (avg)', 'Gintarinė (avg)'],
              [maziausia_camelija_kaina, maziausia_gintarine_kaina, didziausia_camelija_kaina,
               didziausia_gintarine_kaina, vidutine_camelija_kaina, vidutine_gintarine_kaina],
              color=['pink', 'skyblue', 'pink', 'skyblue', 'pink', 'skyblue'])
# Nustatykite teksto etiketes ir pasukimą
ax.set_xticklabels(['Camelia (min)', 'Gintarinė (min)', 'Camelia (max)', 'Gintarinė (max)', 'Cameliia (avg)', 'Gintarinė (avg)'], rotation=20)
# Pridėkite anotacijas virš stulpelių su pasuktu tekstu
for bar, value in zip(bars, [maziausia_camelija_kaina, maziausia_gintarine_kaina, didziausia_camelija_kaina,
                              didziausia_gintarine_kaina, vidutine_camelija_kaina, vidutine_gintarine_kaina]):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{round(value, 2)}', ha='center', va='bottom')

ax.set_ylabel('Kaina')
ax.set_title('Min, Max and Avg Prices for multuvitamins in Cameliia and Gintarinė')
plt.show()

