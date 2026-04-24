import csv
import numpy as np
import matplotlib.pyplot as plt

# Load dataset using csv module to bypass pandas DLL issues
data = []
with open("products.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["product"] and row["store"] and row["price"]:
            data.append({
                "product": row["product"],
                "store": row["store"],
                "price": float(row["price"])
            })

# Group data natively
stores = sorted(list(set(d["store"] for d in data)))
products = sorted(list(set(d["product"] for d in data)))

pivot_df = {store: [] for store in stores}
for prod in products:
    for store in stores:
        # Find price
        price = next((d["price"] for d in data if d["product"] == prod and d["store"] == store), 0)
        pivot_df[store].append(price)

# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Product Price Comparison - Multiple Visualizations', fontsize=16)

# --- 1. Grouped Bar Chart ---
x = np.arange(len(products))
width = 0.25
multiplier = 0

for store in stores:
    offset = width * multiplier
    axs[0, 0].bar(x + offset, pivot_df[store], width, label=store)
    multiplier += 1

axs[0, 0].set_ylabel('Price (USD)')
axs[0, 0].set_title('Grouped Bar Chart')
axs[0, 0].set_xticks(x + width, products)
axs[0, 0].legend(loc='upper right')
axs[0, 0].grid(axis='y', linestyle='--', alpha=0.7)

# --- 2. Line Chart ---
for store in stores:
    axs[0, 1].plot(products, pivot_df[store], marker='o', label=store)

axs[0, 1].set_ylabel('Price (USD)')
axs[0, 1].set_title('Line Chart')
axs[0, 1].legend()
axs[0, 1].grid(True, linestyle='--', alpha=0.7)

# --- 3. Scatter Plot ---
for store in stores:
    axs[1, 0].scatter(products, pivot_df[store], label=store, s=100, alpha=0.7)

axs[1, 0].set_ylabel('Price (USD)')
axs[1, 0].set_title('Scatter Plot')
axs[1, 0].legend()
axs[1, 0].grid(True, linestyle='--', alpha=0.7)

# --- 4. Pie Chart (Average Price per Store) ---
avg_prices = []
store_labels = []
for store in stores:
    prices = [d["price"] for d in data if d["store"] == store]
    if prices:
        avg_prices.append(sum(prices) / len(prices))
        store_labels.append(store)

axs[1, 1].pie(avg_prices, labels=store_labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
axs[1, 1].set_title('Average Product Price by Store')

# Adjust layout
plt.tight_layout()

# Save the visualization to a file so it's easily accessible
plt.savefig('visualization.png')
print("Visualization saved to visualization.png")

# Also attempt to show it in a GUI window
plt.show()
