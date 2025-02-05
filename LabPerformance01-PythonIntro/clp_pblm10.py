def max_number(numbers):
    largest = numbers[0]
    
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest

num_list = [5, 12, 8, 25, 17]
print("Largest number in the list:", max_number(num_list))
