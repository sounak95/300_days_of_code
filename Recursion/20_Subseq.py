"""
find_subsequence("abc", "", 0, ans)
|
|-- find_subsequence("abc", "a", 1, ans)
|   |
|   |-- find_subsequence("abc", "ab", 2, ans)
|   |   |
|   |   |-- find_subsequence("abc", "abc", 3, ans) [Base case, print and store "abc"]
|   |   |
|   |   |-- find_subsequence("abc", "ab", 3, ans) [Base case, print and store "ab"]
|   |
|   |-- find_subsequence("abc", "a", 2, ans)
|       |
|       |-- find_subsequence("abc", "ac", 3, ans) [Base case, print and store "ac"]
|       |
|       |-- find_subsequence("abc", "a", 3, ans) [Base case, print and store "a"]
|
|-- find_subsequence("abc", "", 1, ans)
    |
    |-- find_subsequence("abc", "b", 2, ans)
    |   |
    |   |-- find_subsequence("abc", "bc", 3, ans) [Base case, print and store "bc"]
    |   |
    |   |-- find_subsequence("abc", "b", 3, ans) [Base case, print and store "b"]
    |
    |-- find_subsequence("abc", "", 2, ans)
        |
        |-- find_subsequence("abc", "c", 3, ans) [Base case, print and store "c"]
        |
        |-- find_subsequence("abc", "", 3, ans) [Base case, print and store ""]

https://www.geeksforgeeks.org/print-subsequences-string/

Time Complexity: O(n*2^n)
Space Complexity: O(n)

"""


def find_subsequence(str1, output, index, ans):
    # Base case: if the current index has reached the end of the string
    if index == len(str1):
        # Print the current subsequence
        print(output)
        # Add the current subsequence to the answer list
        ans.append(output)
        # Return from the function call
        return

    # Include the character at the current index and move to the next index
    find_subsequence(str1, output + str1[index], index + 1, ans)

    # Exclude the character at the current index and move to the next index
    find_subsequence(str1, output, index + 1, ans)


# Driver code
ans = []  # This will hold all the subsequences
find_subsequence("abc", "", 0,
                 ans)  # Call the function with the initial parameters
print(ans)  # Print the list of all subsequences
