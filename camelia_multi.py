import pandas as pd
import re

df_camelia = pd.read_csv('modified_camelia.csv', encoding='utf-8-sig')

df_camelia = df_camelia.dropna(subset=['Vaistu pavadinimas'])

multivitaminai_matches_camelia = (df_camelia['Vaistu pavadinimas']
                                  .str.contains(r'\bmultivitaminai\b', flags=re.IGNORECASE))


new_df_camelia = df_camelia.loc[multivitaminai_matches_camelia,
['Kompanija', 'Kiekis', 'Iprastine kaina', 'Kaina su nuolaida']]
new_df_camelia['Iprastine kaina camelia'] = new_df_camelia['Iprastine kaina']
new_df_camelia['Kaina su nuolaida camelia'] = new_df_camelia['Kaina su nuolaida']
new_df_camelia = new_df_camelia.drop(['Iprastine kaina', 'Kaina su nuolaida'], axis=1)

new_df_camelia.to_csv('camelia_multivitaminai.csv', index=False, encoding='utf-8-sig')


# pasirodom savo DataFrame
print("Camelia MULTI:")
print(new_df_camelia)









