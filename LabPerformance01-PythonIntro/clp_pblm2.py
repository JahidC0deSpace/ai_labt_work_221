def find_smallest(numbers):
    smallest = None
    
    for num in numbers:
        if smallest is None or num < smallest:
            smallest = num
    
    return smallest

numbers = {5, 3, 9, 1, 8, 2}
print("Smallest number:", find_smallest(numbers))
