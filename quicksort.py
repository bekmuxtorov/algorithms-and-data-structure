#Quicksort algorithms
#Sort algorithms
#bekmuxtorov

import random
def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    else:
        pivot = arr.pop(random.randrange(len(arr)))
        small_number = [i for i in arr if i <= pivot]
        big_number   = [i for i in arr if i >  pivot]
        return quicksort(small_number) + [pivot] + quicksort(big_number)


a_numbers = [10,25,13,58,4,99]
print(f"Optional arr: {a_numbers}")
print(f"Sorted arr:   {quicksort(a_numbers)}")

    
