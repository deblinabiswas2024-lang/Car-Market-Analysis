import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Complete Project Dataset
csv_data = """Car_Name,Year,Selling_Price,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner
ritz,2014,3.35,5.59,27000,Petrol,Dealer,Manual,0
sx4,2013,4.75,9.54,43000,Diesel,Dealer,Manual,0
ciaz,2017,7.25,9.85,6900,Petrol,Dealer,Manual,0
wagon r,2011,2.85,4.15,5200,Petrol,Dealer,Manual,0
swift,2014,4.6,6.87,42450,Diesel,Dealer,Manual,0
vitara brezza,2018,9.25,9.83,2071,Diesel,Dealer,Manual,0
ciaz,2015,6.75,8.12,18796,Petrol,Dealer,Manual,0
s cross,2015,6.5,8.61,33429,Diesel,Dealer,Manual,0
ciaz,2016,8.75,8.89,20273,Diesel,Dealer,Manual,0
ciaz,2015,7.45,8.92,42367,Diesel,Dealer,Manual,0
fortuner,2015,23,30.61,40000,Diesel,Dealer,Automatic,0
innova,2017,18,19.77,15000,Diesel,Dealer,Automatic,0
city,2016,10.25,13.6,49562,Petrol,Dealer,Manual,0
brio,2015,5.4,6.82,31427,Petrol,Dealer,Automatic,0
"""

df = pd.read_csv(io.StringIO(csv_data.strip()))
df['Transmission'] = df['Transmission'].str.capitalize()
df['Fuel_Type'] = df['Fuel_Type'].str.upper()
sns.set_style("whitegrid")

# --- Slide 6 Chart ---
plt.figure(figsize=(9, 5))
sns.scatterplot(data=df, x='Present_Price', y='Selling_Price', hue='Transmission', style='Transmission', s=80, palette={'Manual': '#1f77b4', 'Automatic': '#ff7f0e'})
plt.title('Selling Price vs. Present Price (by Transmission Type)', fontsize=14, fontweight='bold', pad=12)
plt.xlabel('Present Price (in Lakhs)', fontsize=12)
plt.ylabel('Selling Price (in Lakhs)', fontsize=12)
plt.tight_layout()
plt.savefig('scatter_plot_slide6.png', dpi=300)

# --- Slide 7 Chart ---
plt.figure(figsize=(8, 5))
avg_fuel_price = df.groupby('Fuel_Type')['Selling_Price'].mean().reset_index()
sns.barplot(data=avg_fuel_price, x='Fuel_Type', y='Selling_Price', hue='Fuel_Type', palette='Set2', legend=False)
plt.title('Average Selling Price by Fuel Type', fontsize=14, fontweight='bold', pad=12)
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('Average Selling Price (in Lakhs)', fontsize=12)
plt.tight_layout()
plt.savefig('barplot_slide7.png', dpi=300)

# --- Slide 8 Chart ---
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Selling_Price', kde=True, color='purple', bins=12)
plt.title('Distribution Profile of Used Car Selling Prices', fontsize=14, fontweight='bold', pad=12)
plt.xlabel('Selling Price (in Lakhs)', fontsize=12)
plt.ylabel('Count of Vehicles', fontsize=12)
plt.tight_layout()
plt.savefig('histogram_slide8.png', dpi=300)
