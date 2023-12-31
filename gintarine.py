import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# bibliotekos


# heders padeda apsaugoti nuo puslapio uzblokavimo
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

# purodom puslapi
base_url = "https://www.gintarine.lt/search?q=vitaminai"

# tuscias listas
gintarine = []

# funkcija kad eitu per puslapius
for page in range(1, 63):
    url = f"{base_url}&pagenumber={page}"
    r = requests.get(url, headers=headers)
    time.sleep(3)  # duoda pakankamai laiko surinkti informacijai
    soup = BeautifulSoup(r.text, 'html.parser')
    # surenkama visa reikalinga info pasirenkat klases
    products = soup.find_all('div', class_='product')
    for product in products:
        title = product.find('div', class_='product__title')
        price = product.find('span', class_='product__price--regular')
        club_price = product.find('span', class_='product__price--gv-club')
        pav_text = title.get_text() if title else None
        kaina_text = price.get_text().replace(' ', '').strip() if price else None
        club_kaina_text = club_price.get_text().replace(' ', '').strip() if club_price else None
        # isdeliojam norimas vietas
        gintarine.append({'Pavadinimas': pav_text, 'Iprastine kaina': kaina_text, 'Kaina su nuolaida': club_kaina_text})

# sukuriamas naujas DataFrame
df = pd.DataFrame(gintarine)
print(df)

# sukuriamas CSV failas
df.to_csv('gintarine_vaistine.csv', index=False)