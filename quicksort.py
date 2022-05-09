#Quicksort algorithms
#Sort algorithms
#bekmuxtorov

import random
def quicksort(nums):
    if len(nums) < 2:
        return nums
    
    else:
        pivot = nums.pop(random.randrange(len(nums)))
        small_number = [i for i in nums if i <= pivot]
        big_number   = [i for i in nums if i >  pivot]
        return quicksort(small_number) + [pivot] + quicksort(big_number)


a_numbers = [10,25,13,58,4,99]
print(f"Optional nums: {a_numbers}")
print(f"Sorted nums:   {quicksort(a_numbers)}")

    
