'''
vector_to_integer([3,2,1,9,8], 5, 0, 0)
└── vector_to_integer([3,2,1,9,8], 5, 1, 3)
    └── vector_to_integer([3,2,1,9,8], 5, 2, 32)
        └── vector_to_integer([3,2,1,9,8], 5, 3, 321)
            └── vector_to_integer([3,2,1,9,8], 5, 4, 3219)
                └── vector_to_integer([3,2,1,9,8], 5, 5, 32198) [Base case reached, return 32198]

                Time Complexity: O(n)
                Space Complexity: O(n)
'''


def vector_to_integer(arr, n, i, num):
    if i == n:
        return num  # Base case: when index i reaches n, return the constructed number
    num = num * 10 + arr[
        i]  # Multiply the current number by 10 and add the current digit

    # Recursive call with the next index and the updated number
    return vector_to_integer(arr, n, i + 1, num)


# Example usage
print(vector_to_integer([3, 2, 1, 9, 8], 5, 0, 0))
