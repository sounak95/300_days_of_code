'''
print_subarray([1, 2, 3])
|
+-- print_subarray_util([1, 2, 3], 0, 0)  # Prints [1]
|    |
|    +-- print_subarray_util([1, 2, 3], 0, 1)  # Prints [1, 2]
|    |    |
|    |    +-- print_subarray_util([1, 2, 3], 0, 2)  # Prints [1, 2, 3]
|    |         |
|    |         +-- print_subarray_util([1, 2, 3], 0, 3)  # Base case, e == len(nums), returns
|    |
|    +-- (Backtrack to the previous state)
|
+-- print_subarray_util([1, 2, 3], 1, 1)  # Prints [2]
|    |
|    +-- print_subarray_util([1, 2, 3], 1, 2)  # Prints [2, 3]
|         |
|         +-- print_subarray_util([1, 2, 3], 1, 3)  # Base case, e == len(nums), returns
|
+-- (Backtrack to the previous state)
|
+-- print_subarray_util([1, 2, 3], 2, 2)  # Prints [3]
     |
     +-- print_subarray_util([1, 2, 3], 2, 3)  # Base case, e == len(nums), returns

'''
def print_subarray_util(nums, s, e):
    # Base case: If the end index has reached the length of the array, we return
    if e == len(nums):
        return

    # Print the subarray from the start index 's' to the end index 'e'
    for i in range(s, e + 1):
        print(nums[i], end=' ')
    print()  # Print a newline after printing the subarray

    # Recursive call: extend the subarray by increasing the end index 'e'
    print_subarray_util(nums, s, e + 1)

def print_subarray(nums):
    # Iterate over the array and use each index as the start index 's'
    for s in range(len(nums)):
        # Call the helper function with the current start index 's' and same 's' as end index 'e'
        print_subarray_util(nums, s, s)

# Call the function with an example array
print_subarray([1, 2, 3, 4, 5])


