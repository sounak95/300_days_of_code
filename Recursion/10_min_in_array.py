'''
min_in_array([1,2,3,4,5,-99], 6, 0, [inf])
│
└─> min_in_array([1,2,3,4,5,-99], 6, 1, [1])
    │
    └─> min_in_array([1,2,3,4,5,-99], 6, 2, [1])
        │
        └─> min_in_array([1,2,3,4,5,-99], 6, 3, [1])
            │
            └─> min_in_array([1,2,3,4,5,-99], 6, 4, [1])
                │
                └─> min_in_array([1,2,3,4,5,-99], 6, 5, [1])
                    └─> min_in_array([1,2,3,4,5,-99], 6, 6, [-99])

                    Time Complexity: O(n)
                    Space Complexity: O(n)

'''


def min_in_array(arr, n, i, mini):
    # If the index has reached the length of the array, we have checked all elements.
    if i == n:
        return
    # Update the minimum value if the current array element is smaller.
    mini[0] = min(arr[i], mini[0])
    # Move to the next element in the array.
    min_in_array(arr, n, i + 1, mini)


# Initialize the minimum value to positive infinity.
mini = [float('inf')]
# Call the recursive function starting from index 0.
min_in_array([1, 2, 3, 4, 5, -99], 6, 0, mini)

# After the recursive calls, print the smallest value found.
print(mini[0])
