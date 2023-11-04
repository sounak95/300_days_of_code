'''
max_in_array([1,2,3,400,5,99], 6, 0, [-inf])
│
├─> max_in_array([1,2,3,400,5,99], 6, 1, [1])
│   │
│   ├─> max_in_array([1,2,3,400,5,99], 6, 2, [2])
│   │   │
│   │   ├─> max_in_array([1,2,3,400,5,99], 6, 3, [3])
│   │   │   │
│   │   │   ├─> max_in_array([1,2,3,400,5,99], 6, 4, [400])
│   │   │   │   │
│   │   │   │   ├─> max_in_array([1,2,3,400,5,99], 6, 5, [400])
│   │   │   │   │   │
│   │   │   │   │   └─> max_in_array([1,2,3,400,5,99], 6, 6, [400])
│   │   │   │   │       (end of recursion, array index is equal to n)
│   │   │   │   │
│   │   │   │   └─> (end of recursion, array index is equal to n)
│   │   │   │
│   │   │   └─> (end of recursion, array index is equal to n)
│   │   │
│   │   └─> (end of recursion, array index is equal to n)
│   │
│   └─> (end of recursion, array index is equal to n)
│
└─> (end of recursion, array index is equal to n)

'''

def max_in_array(arr, n, i, maxi):
    # Base case: if the end of the array is reached, stop recursion
    if i == n:
        return
    # Update the maximum value found so far
    maxi[0] = max(arr[i], maxi[0])
    # Recursively call the function for the next element
    max_in_array(arr, n, i + 1, maxi)

# Initialize maximum value with negative infinity
maxi = [-float('inf')]
# Call the recursive function starting at index 0
max_in_array([1,2,3,400,5, 99], 6, 0, maxi)

# Print the maximum value found in the array
print(maxi[0])
