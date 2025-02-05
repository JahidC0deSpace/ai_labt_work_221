def sum_odd_even(numbers):
    even_sum = 0
    odd_sum = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    
    return even_sum, odd_sum

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_sum, odd_sum = sum_odd_even(numbers)

print("Sum of Even Numbers:", even_sum)
print("Sum of Odd Numbers:", odd_sum)
