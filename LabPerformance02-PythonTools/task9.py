import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = [22, 24, 20, 26, 23, 25, 21] 

plt.figure(figsize=(8, 5))  
plt.plot(days, temperatures, marker='o', linestyle='-', color='b', linewidth=2, markersize=6, label="Temperature °C")

plt.xlabel("Days of the Week")
plt.ylabel("Temperature in °C")
plt.title("Temperature Of a Week")
plt.grid(True) 
plt.legend()

plt.show()
