import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#heders padeda apsaugoti nuo puslapio uzblokavimo
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

#url nustatymas pasirinktam puslapiui
url_base = "https://camelia.lt/jolisearch?s=vitaminai"



#camelia sarasas uz ciklo ribu
camelia = []

#
# ciklas vaikstantis per puslapius
for page in range(1, 34):  #(1, 34) pradeda nuo pirmo iki 33 puslapio
    url = f"{url_base}&pagenumber={page}"
    r = requests.get(url, headers=headers)

    #ant puslapio palieka 3s kad speti nuskaityti informacija
    time.sleep(3)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup) # patikrinam ar veikia


    vitamins = soup.find_all('div', class_="second-block")
    # print(vitamins) # pasitikrinam klases

    #istraukiam duomenis
    for vitamin in vitamins:
        #title
        title_element = vitamin.find('h5', class_="product-name")
        title = title_element.text.strip() if title_element else None
        # print(title)

        #regular price
        regular_price_element = vitamin.find('span', class_="price regular-price disable-text-decoration")
        regular_price = regular_price_element.text.replace('€', '').strip() if regular_price_element else None
        # print(regular_price)

        ###############################################################################################################
        # regular price turi dvi klases:
        #"price regular-price disable-text-decoration"---> kai kaina neturi nuolaidos
        #"regular-price old-price"---> buvusi kaina iki nuolaidos
        #todel nuromdome salyga, kad jei nera "price regular-price disable-text-decoration"
        #butu naudojama "regular-price old-price"
        if not regular_price:
            regular_price_element = vitamin.find('span', class_="regular-price old-price")
            regular_price = regular_price_element.text.replace('€', '').strip() if regular_price_element else None
        ###############################################################################################################

        #discount price
        discount_price_element = vitamin.find('span', class_="price product-price discounted-price")
        discount_price = discount_price_element.text.replace('€', '').strip() if discount_price_element else None
        # print(discount_price)
        # Apjungiamas sarasas
        camelia.append({'Pavadinimas': title, 'Iprastine kaina': regular_price, 'Kaina su nuolaida': discount_price})


# sukuriama DataFrame camelia duomenims
df1 = pd.DataFrame(camelia)
print(df1)

# duomenys perkialiami i CSv faila
df1.to_csv('camelia_vaistine.csv', index=False)