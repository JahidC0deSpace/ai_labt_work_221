import matplotlib.pyplot as plt

regions = ["North", "South", "East", "West", "Central"]
sales_revenue = [50000, 70000, 65000, 80000, 72000] 

plt.figure(figsize=(8, 5))  
plt.bar(regions, sales_revenue, color='skyblue', width=0.6)

plt.xlabel("Regions")
plt.ylabel("Sales Revenue ($)")
plt.title("Sales Revenue Comparison Across Regions")
plt.grid(axis='y', linestyle='--', alpha=0.7) 

plt.show()
