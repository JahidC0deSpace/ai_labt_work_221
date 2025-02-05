total_sum = 0

for num in range(50, 101):
    if num % 3 == 0 and num % 5 != 0:
        total_sum += num

print("Sum of numbers between 50 and 100 divisible by 3 but not 5:", total_sum)
