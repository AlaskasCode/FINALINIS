import pandas as pd

# nuskaityti faila is CSV i DataFrame
df_gintarine = pd.read_csv('gintarine_vaistine.csv', encoding='utf-8')


#pirmas zodis 'Kompanija' visa kita kas lieka 'Vaistu pavadinimas, padalinama 'Pavadinimas' stulpelis
df_gintarine[['Kompanija', 'Vaistu pavadinimas']] = df_gintarine['Pavadinimas'].str.split(n=1, expand=True)

#jei 'Komapanija' susideda is 3 ar maziau raidziu pridedamas dar vienas zodis is 'Vaistu pavadinimas'
df_gintarine.loc[df_gintarine['Kompanija'].str.len() <= 3, 'Kompanija']\
    += ' ' + df_gintarine['Vaistu pavadinimas'].str.split().str[0]

#jei prie 'Kompanija' yra kableliu juos panaikina
df_gintarine['Kompanija'] = df_gintarine['Kompanija'].str.replace(',', '').str.strip()


#is 'Vaistu pavadinimas' istraukiami paskutiniai sveikiji skaiciai(tokiem esant) ir ikeliami i 'Kiekis'
df_gintarine['Kiekis'] = df_gintarine['Vaistu pavadinimas'].str.extract(r'(\d+)[^\d]*$')


#jei 'Kiekis' neturi reiksmes yrasoma 0, uzimti vietai
df_gintarine['Kiekis'] = df_gintarine['Kiekis'].fillna(0).astype(int)


#pasalinami skaiciai is 'Vaistu pavadinimas' kuriuos panaudojom 'Kiekis' stulpelyje
df_gintarine['Vaistu pavadinimas'] = df_gintarine['Vaistu pavadinimas'].replace(r'\d+[^\d]*$', '', regex=True).str.strip()

# Pašalinti eurų ženklus iš 'Iprastine kaina' ir 'Kaina su nuolaida' stulpelių
df_gintarine['Iprastine kaina'] = df_gintarine['Iprastine kaina'].str.replace('€', '')
df_gintarine['Kaina su nuolaida'] = df_gintarine['Kaina su nuolaida'].str.replace('€', '')



# suorganizuojami stulpeliai
df_gintarine = df_gintarine[['Kompanija', 'Vaistu pavadinimas', 'Kiekis', 'Iprastine kaina', 'Kaina su nuolaida']]


#pakeisti DataFrame duomenys issaugomi kaip CSV failas
df_gintarine.to_csv('modified_gintarine.csv', index=False, encoding='utf-8-sig')


#pasirodom savo rezultatus :)
print("Gintarine:")
print(df_gintarine)