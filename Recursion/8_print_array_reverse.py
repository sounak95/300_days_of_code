'''
printArray([1,2,3,4,5], 5, 0)
│
└─> printArray([1,2,3,4,5], 5, 1)
    │
    └─> printArray([1,2,3,4,5], 5, 2)
        │
        └─> printArray([1,2,3,4,5], 5, 3)
            │
            └─> printArray([1,2,3,4,5], 5, 4)
                │
                └─> printArray([1,2,3,4,5], 5, 5)  // Base case reached, no further calls
                    │
                    └── print(5)                 // Unwinding stack, print in reverse order
                │
                └── print(4)
            │
            └── print(3)
        │
        └── print(2)
    │
    └── print(1)

    Time Complexity: O(n)
    Space Complexity: O(n)
'''


def printArray(arr, n, index):
    if index == n:
        return

    printArray(arr, n, index + 1)
    print(arr[index])


printArray([1, 2, 3, 4, 5], 5, 0)
