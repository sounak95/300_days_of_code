'''
doubleArr([1, 2, 3, 4, 5], 5, 0)
└── doubleArr([2, 2, 3, 4, 5], 5, 1)
    └── doubleArr([2, 4, 3, 4, 5], 5, 2)
        └── doubleArr([2, 4, 6, 4, 5], 5, 3)
            └── doubleArr([2, 4, 6, 8, 5], 5, 4)
                └── doubleArr([2, 4, 6, 8, 10], 5, 5) (Base case reached, no further calls)

                Time Complexity: O(n)
                Space Complexity: O(n)

'''


def doubleArr(arr, n, i):
    # Base case: if the index i is equal to the length of the array, stop recursion
    if i == n:
        return
    # Double the current element of the array
    arr[i] = 2 * arr[i]
    # Recursive call for the next element
    doubleArr(arr, n, i + 1)


# Initialize the array
arr = [1, 2, 3, 4, 5]
# Call the recursive function starting at index 0
doubleArr(arr, len(arr), 0)

# Print the modified array
print(arr)
