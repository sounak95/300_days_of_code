'''
find("babbar", 6, 0, 'a')
└── find("babbar", 6, 1, 'a')
    └── find("babbar", 6, 2, 'a')  # 'a' found, index 2 printed
        └── find("babbar", 6, 3, 'a')
            └── find("babbar", 6, 4, 'a')  # 'a' found, index 4 printed
                └── find("babbar", 6, 5, 'a')
                    └── find("babbar", 6, 6, 'a')  # Base case reached, recursion ends

                    Time Complexity: O(n)
                    Space Complexity: O(n)

'''


def find(arr, n, i, target):
    # Base case: If we've reached the end of the array, return to end the recursion
    if i == n:
        return

    # If the current character matches the target, print the index
    if arr[i] == target:
        print(i)

    # Recursive case: Move to the next index in the array
    find(arr, n, i + 1, target)


# The string we are searching through
arr = "babbar"

# Call the function with the string, the length of the string, the starting index, and the target character
find(arr, len(arr), 0, 'a')
