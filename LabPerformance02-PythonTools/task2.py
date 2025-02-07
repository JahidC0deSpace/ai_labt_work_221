def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = input("Enter numbers for first list: ").split()
list2 = input("Enter numbers for second list: ").split()

list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]

common_elements = find_common_elements(list1, list2)

if common_elements:
    print("Common elements:", common_elements)
else:
    print("There is no common number.")
