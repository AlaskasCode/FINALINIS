import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV files
camelia_df = pd.read_csv('modified_camelia.csv', thousands='.', decimal=',')
gintarine_df = pd.read_csv('modified_gintarine.csv', thousands='.', decimal=',')

# Calculate the minimum, maximum, and average prices for all items
camelia_min_price = camelia_df['Iprastine kaina'].min()
camelia_max_price = camelia_df['Iprastine kaina'].max()
camelia_avg_price = camelia_df['Iprastine kaina'].mean()

gintarine_min_price = gintarine_df['Iprastine kaina'].min()
gintarine_max_price = gintarine_df['Iprastine kaina'].max()
gintarine_avg_price = gintarine_df['Iprastine kaina'].mean()

# Print the minimum, maximum, and average prices with 2 decimal places
print(f"Camelia Min Price: {camelia_min_price:.2f}, Max Price: {camelia_max_price:.2f}, Avg Price: {camelia_avg_price:.2f}")
print(f"Gintarine Min Price: {gintarine_min_price:.2f}, Max Price: {gintarine_max_price:.2f}, Avg Price: {gintarine_avg_price:.2f}")

# Plotting
bar_positions = [1, 2, 3, 5, 6, 7]  # Adjusted positions for side-by-side bars
bar_width = 0.4

# Make the figure size larger
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting min, max, and avg prices for Camelia
ax.bar(bar_positions[0], camelia_min_price, width=bar_width, label='Camelia Min', alpha=0.7, color='pink')
ax.bar(bar_positions[1], camelia_max_price, width=bar_width, label='Camelia Max', alpha=0.7, color='pink')
ax.bar(bar_positions[2], camelia_avg_price, width=bar_width, label='Camelia Avg', alpha=0.7, color='pink')

# Plotting min, max, and avg prices for Gintarine
ax.bar(bar_positions[3], gintarine_min_price, width=bar_width, label='Gintarine Min', alpha=0.7, color='skyblue')
ax.bar(bar_positions[4], gintarine_max_price, width=bar_width, label='Gintarine Max', alpha=0.7, color='skyblue')
ax.bar(bar_positions[5], gintarine_avg_price, width=bar_width, label='Gintarine Avg', alpha=0.7, color='skyblue')

# Set x-labels with min, max, and avg prices
ax.set_xticks([1.5, 3.5, 5.5])
ax.set_xticklabels(['Min', 'Max', 'Avg'])
# Longer y-axis label with tag ID on a separate line
ax.set_ylabel('Price\n(including tag ID)', multialignment='center')
ax.set_title('Min, Max, and Avg Prices for All Items')
ax.legend()

# Add values right on top of the bars
for i, price in enumerate([camelia_min_price, camelia_max_price, camelia_avg_price,
                            gintarine_min_price, gintarine_max_price, gintarine_avg_price]):
    ax.text(bar_positions[i], price + 1, f'{price:.2f}', ha='center', va='bottom', fontsize=8, color='black')

plt.show()