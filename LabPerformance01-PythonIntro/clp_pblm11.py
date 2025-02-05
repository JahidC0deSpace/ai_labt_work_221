def reverse_tuple(tup):
    reversed_tup = ()
    
    for i in range(len(tup) - 1, -1, -1):
        reversed_tup += (tup[i],)
    
    return reversed_tup
my_tuple = (10, 20, 30, 40, 50)
print("Reversed tuple:", reverse_tuple(my_tuple))
