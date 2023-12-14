import pandas as pd
import re


#nuskaitom modified CSV failus
df_gintarine = pd.read_csv('modified_gintarine.csv', encoding='utf-8-sig')
df_camelia = pd.read_csv('modified_camelia.csv', encoding='utf-8-sig')

#ismetamos eilutes su trukstama informacija
df_gintarine = df_gintarine.dropna(subset=['Vaistu pavadinimas'])
df_camelia = df_camelia.dropna(subset=['Vaistu pavadinimas'])

#istraukiamas zodis 'multivitaminai' is  stulpelio 'Vaistu pavadinimas'
multivitaminai_matches_gintarine = (df_gintarine['Vaistu pavadinimas']
                                    .str.contains(r'\bmultivitaminai\b', flags=re.IGNORECASE))
multivitaminai_matches_camelia = (df_camelia['Vaistu pavadinimas']
                                  .str.contains(r'\bmultivitaminai\b', flags=re.IGNORECASE))

#sukuriami nauji stulpeliai 'Iprastine kaina' ir 'Kaina su nuolaida'  vaistinems
new_df_gintarine = df_gintarine.loc[multivitaminai_matches_gintarine,
['Kompanija', 'Kiekis', 'Iprastine kaina', 'Kaina su nuolaida']]
new_df_gintarine['Iprastine kaina gintarine'] = new_df_gintarine['Iprastine kaina']
new_df_gintarine['Kaina su nuolaida gintarine'] = new_df_gintarine['Kaina su nuolaida']
new_df_gintarine = new_df_gintarine.drop(['Iprastine kaina', 'Kaina su nuolaida'], axis=1)

new_df_camelia = df_camelia.loc[multivitaminai_matches_camelia,
['Kompanija', 'Kiekis', 'Iprastine kaina', 'Kaina su nuolaida']]
new_df_camelia['Iprastine kaina camelia'] = new_df_camelia['Iprastine kaina']
new_df_camelia['Kaina su nuolaida camelia'] = new_df_camelia['Kaina su nuolaida']
new_df_camelia = new_df_camelia.drop(['Iprastine kaina', 'Kaina su nuolaida'], axis=1)

# apjungiami DataFrames
combined_df = pd.concat([new_df_gintarine, new_df_camelia], ignore_index=True)

# isaugomi DataFrame i CSV faila
combined_df.to_csv('combined_multivitaminai.csv', index=False, encoding='utf-8-sig')

# pasirodom savo DataFrame
print("Combined DataFrame:")
print(combined_df)