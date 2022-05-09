#Bubblesort algorithms
#Sort algorithms
#bekmuxtorov
#python

def bubble(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i] , nums[i+1] = nums[i+1] , nums[i]

    return nums



def bubble_sort(nums):
    for _ in range(len(nums)-1):
        bubble(nums)

    return nums



a_numbers = [10,22,9,64,3]
print(bubble_sort(a_numbers))

