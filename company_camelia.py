import pandas as pd

# nuskaityti faila is CSV i DataFrame
df_camelia = pd.read_csv('camelia_vaistine.csv', encoding='utf-8')


#pirmas zodis 'Kompanija' visa kita kas lieka 'Vaistu pavadinimas, padalinama 'Pavadinimas' stulpelis
df_camelia[['Kompanija', 'Vaistu pavadinimas']] = df_camelia['Pavadinimas'].str.split(n=1, expand=True)

#jei 'Komapanija' susideda is 3 ar maziau raidziu pridedamas dar vienas zodis is 'Vaistu pavadinimas'
df_camelia.loc[df_camelia['Kompanija'].str.len() <= 3, 'Kompanija']\
    += ' ' + df_camelia['Vaistu pavadinimas'].str.split().str[0]

#jei prie 'Kompanija' yra kableliu juos panaikina
df_camelia['Kompanija'] = df_camelia['Kompanija'].str.replace(',', ' ')

#is 'Vaistu pavadinimas' istraukiami paskutiniai sveikiji skaiciai(tokiem esant) ir ikeliami i 'Kiekis'
df_camelia['Kiekis'] = df_camelia['Vaistu pavadinimas'].str.extract(r'(\d+)[^\d]*$')


#jei 'Kiekis' neturi reiksmes yrasoma 0, uzimti vietai
df_camelia['Kiekis'] = df_camelia['Kiekis'].fillna(0).astype(int)

#jei 'Kiekis' neturi reiksmes yrasoma 0, uzimti vietai
df_camelia['Kiekis'] = df_camelia['Kiekis'].fillna(0).astype(int)


#pasalinami skaiciai is 'Vaistu pavadinimas' kuriuos panaudojom 'Kiekis' stulpelyje
df_camelia['Vaistu pavadinimas'] = df_camelia['Vaistu pavadinimas'].replace(r'\d+[^\d]*$', '', regex=True).str.strip()


# suorganizuojami stulpeliai
df_camelia = df_camelia[['Kompanija', 'Vaistu pavadinimas', 'Kiekis', 'Iprastine kaina', 'Kaina su nuolaida']]


#pakeisti DataFrame duomenys issaugomi kaip CSV failas
df_camelia.to_csv('modified_camelia.csv', index=False, encoding='utf-8-sig')


#pasirodom savo rezultatus :)
print("Camelia:")
print(df_camelia)