def sum_list(numbers):
    total = 0
    
    for num in numbers:
        total += num
    
    return total
num_list = [10, 20, 30, 40, 50]
print("Sum of all items in the list:", sum_list(num_list))
