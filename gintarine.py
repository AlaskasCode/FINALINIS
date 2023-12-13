import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#heders padeda apsaugoti nuo puslapio uzblokavimo
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}
#url nustatymas pasirinktam puslapiui
base_url = "https://www.gintarine.lt/search?q=vitaminai"

#gintarine sarasas uz ciklo ribu
gintarine = []

# ciklas vaikstantis per puslapius
for page in range(1, 63):  # nuo pirmo iki 62 puslapio

    url = f"{base_url}&pagenumber={page}" #funkcija naudojama apjungti base_url su dabartinius puslapiu
    r = requests.get(url, headers=headers)
    # print(url)
    # print(r)

    # ant puslapio palieka 3s kad speti nuskaityti informacija
    time.sleep(3)

    soup = BeautifulSoup(r.text, 'html.parser') #parser analizuoja
    # print(soup) #

    title = soup.find_all('div', class_="product__title")
    # print(title) #patikrinam ar pavadinimus gaunam

    ###################################################################################################################
    #salyga 'if len' buvo naudota kad itraukti isparduotas prekes, jei preke isparduota jos kainos nera
    #
    #jei kaina yra mazesne nei title, tai reiskia kad preke buvo isparduota
    price = soup.find_all('span', class_="product__price--regular")
    if len(price) < len(title):
        #kai kurios prekes neturi kainos, nes buvo isparduotos

        price.extend([None] * (len(title) - len(price)))

    #kai kurie title neturi club_price
    club_price = soup.find_all('span', class_="product__price--gv-club")
    if len(club_price) < len(title):
        #jei club_price yra mazesne nei title pazymima kaip None
        club_price.extend([None] * (len(title) - len(club_price)))
    ###################################################################################################################
    for pav, kaina, club_kaina in zip(title, price, club_price):
        pav_text = pav.get_text()
        kaina_text = kaina.get_text().replace(' ', '').strip() if kaina else None
        club_kaina_text = club_kaina.get_text().replace(' ', '').strip() if club_kaina else None

        gintarine.append({'Pavadinimas': pav_text, 'Iprastine kaina': kaina_text, 'Kaina su nuolaida': club_kaina_text})

# sukuriamas DataFrame gintarine
df = pd.DataFrame(gintarine)
print(df)

# DataFramne issaygomas kaip CSV failas
df.to_csv('ginta_vaistine.csv', index=False)