def find_largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

a = input("Give the 1st num: ")
b = input("Give the 2nd num: ")
print("Largest number between", a, "and", b, "is", find_largest(int(a), int(b)))
