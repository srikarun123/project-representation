import pandas as pd
import matplotlib.pyplot as plt

# Load historical prices dataset
df = pd.read_csv("historical_prices.csv")

products = df['Product'].unique()

# Create a figure with 2 subplots (1 for Price, 1 for Ratings)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
fig.suptitle('Product Volatility Over Time: Prices and Ratings', fontsize=16)

# Line Chart for Prices Over Different Days
for product in products:
    subset = df[df['Product'] == product]
    ax1.plot(subset['Day'], subset['Price'], marker='o', linewidth=2.5, markersize=8, label=product)

ax1.set_ylabel('Price (USD)')
ax1.set_title('Dynamic Price Trends Across Days')
ax1.legend(loc='upper right')
ax1.grid(True, linestyle='--', alpha=0.7)

# Line Chart for Ratings Over Different Days
for product in products:
    subset = df[df['Product'] == product]
    ax2.plot(subset['Day'], subset['Rating'], marker='s', linewidth=2.5, markersize=8, linestyle='--', label=product)

ax2.set_ylabel('Customer Rating (out of 5)')
ax2.set_xlabel('Timeline')
ax2.set_title('Rating Fluctuations Corresponding to Prices')
ax2.legend(loc='lower right')
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
