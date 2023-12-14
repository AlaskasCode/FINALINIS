# Importuojame reikiamas bibliotekas
import pandas as pd
import re

# Nuskaitome Camelija duomenis iš CSV failo su UTF-8 kodavimu
df_camelia = pd.read_csv('modified_camelia.csv', encoding='utf-8-sig')

# Pašaliname tuščius įrašus stulpelyje 'Vaistu pavadinimas'
df_camelia = df_camelia.dropna(subset=['Vaistu pavadinimas'])

# Filtruojame multivitaminus Camelija pagal pavadinimą
multivitaminai_matches_camelia = (df_camelia['Vaistu pavadinimas']
                                  .str.contains(r'\bmultivitaminai\b', flags=re.IGNORECASE))

# Sukuriame naują DataFrame su reikiamais stulpeliais
new_df_camelia = df_camelia.loc[multivitaminai_matches_camelia,
['Kompanija', 'Kiekis', 'Iprastine kaina', 'Kaina su nuolaida']]

# Kopijuojame ir pervadiname kainų stulpelius
new_df_camelia['Iprastine kaina camelia'] = new_df_camelia['Iprastine kaina']
new_df_camelia['Kaina su nuolaida camelia'] = new_df_camelia['Kaina su nuolaida']
new_df_camelia = new_df_camelia.drop(['Iprastine kaina', 'Kaina su nuolaida'], axis=1)

# Išsaugome rezultatus į CSV failą su UTF-8 kodavimu
new_df_camelia.to_csv('camelia_multivitaminai.csv', index=False, encoding='utf-8-sig')

# Parodome sukurtą DataFrame
print("Camelia MULTI:")
print(new_df_camelia)










