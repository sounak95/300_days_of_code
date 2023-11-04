
'''
solve([1,2,3,4,5], 5, 0, [])
│
├─> solve([1,2,3,4,5], 5, 1, [])
│   │
│   ├─> solve([1,2,3,4,5], 5, 2, [2])
│   │   │
│   │   ├─> solve([1,2,3,4,5], 5, 3, [2])
│   │   │   │
│   │   │   └─> solve([1,2,3,4,5], 5, 4, [2,4])
│   │   │       │
│   │   │       └─> solve([1,2,3,4,5], 5, 5, [2,4])
│   │   │
│   │   └─> (end of recursion, array index is equal to n)
│   │
│   └─> (end of recursion, array index is equal to n)
│
└─> (end of recursion, array index is equal to n)
'''
# push even elements to vector

def solve(arr, n, i, vector):
    # Base case: if we've reached the end of the array, stop the recursion
    if i == n:
        return
    # If the current element is even, append it to the vector
    if arr[i] % 2 == 0:
        vector.append(arr[i])
    # Recur for the next element in the array
    solve(arr, n, i + 1, vector)

# Initialize an empty list to store even numbers
vector = []
# Call the recursive function with the initial index set to 0
solve([1,2,3,4,5], 5, 0, vector)

# Print the list containing even numbers from the array
print(vector)
