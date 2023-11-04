'''
binary_search([1, 2, 3, 4, 5, 6], 0, 5, 6)
|
└───> binary_search([1, 2, 3, 4, 5, 6], 3, 5, 6)  # Mid is at index 2 (value 3), target is greater
     |
     └───> binary_search([1, 2, 3, 4, 5, 6], 5, 5, 6)  # Mid is at index 4 (value 5), target is greater
          |
          └───> (Found at index 5) Returns index 5  # Mid is at index 5 (value 6), target found

'''

def binary_search(arr, s, e, target):
    # Base case: if the start index is greater than the end index, the target is not in the array
    if s > e:
        return -1

    # Calculate the middle index of the current search range
    mid = s + (e - s) // 2

    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid

    # If the target is greater than the middle element, search the upper half of the array
    if target > arr[mid]:
        return binary_search(arr, mid + 1, e, target)
    else:
        # If the target is less than the middle element, search the lower half of the array
        return binary_search(arr, s, mid - 1, target)

# Sorted array to search
l1 = [1, 2, 3, 4, 5, 6]

# Call the binary_search function with the list, start index, end index, and target value
print(binary_search(l1, 0, len(l1) - 1, 6))

