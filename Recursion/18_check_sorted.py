'''
check_sorted([1, 2, 3, 4, 9, 6], 6, 1)  # True, proceed to next
├── check_sorted([1, 2, 3, 4, 9, 6], 6, 2)  # True, proceed to next
│   ├── check_sorted([1, 2, 3, 4, 9, 6], 6, 3)  # True, proceed to next
│   │   ├── check_sorted([1, 2, 3, 4, 9, 6], 6, 4)  # True, proceed to next
│   │   │   └── check_sorted([1, 2, 3, 4, 9, 6], 6, 5)  # False, return False (9 > 6 is false)
│   │   │       └── (Ends, as False is returned)


Time Complexity: O(n)
Space Complexity: O(n)

'''


def check_sorted(arr, n, i):
    # Base case: if we have reached the end of the array, return True, because all elements were sorted till now
    if i >= n:
        return True

    # If the current element is greater than the previous one, continue checking the next element
    if arr[i] > arr[i - 1]:
        return check_sorted(arr, n, i + 1)
    else:
        # If we found an element that is not greater than the previous one, return False
        return False


# List to be checked
l1 = [1, 2, 3, 4, 9, 6]

# Call the function with the list, its length, and starting index 1 (since we compare with the previous element)
print(check_sorted(l1, len(l1), 1))
