def remove_duplicates_and_sort(numbers):
    return sorted(list(set(numbers)))

numbers = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    numbers.append(ele)
result = remove_duplicates_and_sort(numbers)
print("Sorted list without duplicates:", result)
