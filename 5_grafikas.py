import pandas as pd
import matplotlib.pyplot as plt

# Įkelsime duomenis iš CSV failų
camelia_df = pd.read_csv('modified_camelia.csv', thousands='.', decimal=',')
gintarine_df = pd.read_csv('modified_gintarine.csv', thousands='.', decimal=',')

# Filtruosime duomenis pagal kiekius 30, 60 ir 90
filtered_camelia = camelia_df[camelia_df['Kiekis'].isin([30, 60, 90])]
filtered_gintarine = gintarine_df[gintarine_df['Kiekis'].isin([30, 60, 90])]

# Apskaičiuosime vidutines kainas Camelia ir Gintarine
avg_prices_camelia = filtered_camelia.groupby('Kiekis')['Iprastine kaina'].mean()
avg_prices_gintarine = filtered_gintarine.groupby('Kiekis')['Iprastine kaina'].mean()

# Braižysime grafiką
bar_positions = [1, 2, 3]
bar_width = 0.4
fig, ax = plt.subplots()

# Braižysime vidutines kainas Cameliai
camelia_bars = ax.bar(bar_positions, avg_prices_camelia, width=bar_width, label='Camelia', color='pink', alpha=0.7)

# Braižysime vidutines kainas Gintarinei
gintarine_bars = ax.bar([pos + bar_width for pos in bar_positions], avg_prices_gintarine, width=bar_width, label='Gintarine', color='skyblue', alpha=0.7)

# Nustatysime x-asi su kiekiu
ax.set_xticks([1.2, 2.2, 3.2])
ax.set_xticklabels([30, 60, 90])
ax.set_ylabel('Vidutinė Kaina')
ax.set_xlabel('Kiekis')
ax.set_title('Vidutinės Kainos Kiekiams 30, 60 ir 90')
ax.legend()

# Pridėsime kainų reikšmes virš stulpelių
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{height:.2f}', ha='center', va='bottom')

add_labels(camelia_bars)
add_labels(gintarine_bars)

# Parodome grafiką
plt.show()




