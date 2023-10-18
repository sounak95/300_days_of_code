

def print_subarray_util(nums, s, e):

    if e== len(nums):
        return

    for i in range(s, e+1):
        print(nums[i], end=' ')
    print()

    print_subarray_util(nums, s, e+1)

def print_subarray(nums):
    for s in range(len(nums)):
        print_subarray_util(nums, s, s)


print_subarray([1,2,3,4,5])

