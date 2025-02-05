def second_highest(numbers):
    highest = None
    second = None
    
    for num in numbers:
        if highest is None or num > highest:
            second = highest
            highest = num
        elif second is None or num > second:
            second = num
    
    return second

numbers = {10, 20, 30, 40, 50}
print("Second highest number:", second_highest(numbers))
