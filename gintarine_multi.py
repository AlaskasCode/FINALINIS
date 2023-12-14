import pandas as pd
import re


#nuskaitom modified CSV failus
df_gintarine = pd.read_csv('modified_gintarine.csv', encoding='utf-8-sig')

#ismetamos eilutes su trukstama informacija
df_gintarine = df_gintarine.dropna(subset=['Vaistu pavadinimas'])

#istraukiamas zodis 'multivitaminai' is  stulpelio 'Vaistu pavadinimas'
multivitaminai_matches_gintarine = (df_gintarine['Vaistu pavadinimas']
                                    .str.contains(r'\bmultivitaminai\b', flags=re.IGNORECASE))

#sukuriami nauji stulpeliai 'Iprastine kaina' ir 'Kaina su nuolaida'  vaistinems
new_df_gintarine = df_gintarine.loc[multivitaminai_matches_gintarine,
['Kompanija', 'Kiekis', 'Iprastine kaina', 'Kaina su nuolaida']]
new_df_gintarine['Iprastine kaina gintarine'] = new_df_gintarine['Iprastine kaina']
new_df_gintarine['Kaina su nuolaida gintarine'] = new_df_gintarine['Kaina su nuolaida']
new_df_gintarine = new_df_gintarine.drop(['Iprastine kaina', 'Kaina su nuolaida'], axis=1)

# isaugomi DataFrame i CSV faila
new_df_gintarine.to_csv('gintarine_multivitaminai.csv', index=False, encoding='utf-8-sig')

# pasirodom savo DataFrame
print("Gintarine MULTI:")
print(new_df_gintarine)