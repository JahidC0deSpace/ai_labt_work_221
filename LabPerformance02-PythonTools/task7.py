import pandas as pd

file_path = "sales_data.csv"  
df = pd.read_csv(file_path)

df["Revenue"] = df["Quantity"] * df["Price"] 
total_revenue = df.groupby("Product")["Revenue"].sum() 
print("Total Revenue per Product:")
for product, revenue in total_revenue.items():
    print(f"{product}: {revenue}")

