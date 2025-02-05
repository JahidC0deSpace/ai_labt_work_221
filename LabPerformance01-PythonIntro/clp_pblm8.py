def sum_numbers(*nums):
    total = 0
    
    for num in nums:
        total += num
    
    return total
print("Sum of numbers:", sum_numbers(10, 20, 30, 40, 50))
