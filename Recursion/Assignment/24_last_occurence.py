'''
last_occ(arr, 6, 4)     # Checks index 6, value is 5, not the target
  └── last_occ(arr, 5, 4)   # Checks index 5, value is 4, this is the target, returns 5

'''

def last_occ(arr, index, target):
    # If the index is less than 0, it means we've reached the beginning of the array
    # and didn't find the target. Thus, return -1 to indicate the target is not present.
    if index < 0:
        return -1

    # Check if the current element at 'index' is equal to the target.
    if arr[index] == target:
        # If it is, return the current index as it's the last occurrence so far.
        return index
    else:
        # If it isn't, recursively call 'last_occ' with the previous index to continue the search.
        return last_occ(arr, index - 1, target)

# Example array and target
arr = [1, 2, 3, 3, 4, 4, 5]
# Call the function with the array, the starting index (which is the last index of the array),
# and the target value we're searching for.
print(last_occ(arr, len(arr) - 1, 4))

