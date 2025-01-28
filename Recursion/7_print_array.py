'''
printArray([1,2,3,4,5], 5, 0)
│
├── print(1)
│
└─> printArray([1,2,3,4,5], 5, 1)
    │
    ├── print(2)
    │
    └─> printArray([1,2,3,4,5], 5, 2)
        │
        ├── print(3)
        │
        └─> printArray([1,2,3,4,5], 5, 3)
            │
            ├── print(4)
            │
            └─> printArray([1,2,3,4,5], 5, 4)
                │
                ├── print(5)
                │
                └─> printArray([1,2,3,4,5], 5, 5)  // Base case reached, no further calls

Time Complexity: O(n)
Space Complexity: O(n)
'''


def printArray(arr, n, index):
    if index == n:
        return
    print(arr[index])
    printArray(arr, n, index + 1)


printArray([1, 2, 3, 4, 5], 5, 0)
