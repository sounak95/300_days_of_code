# User function Template for python3
'''
maximizeTheCuts(4, 2, 1, 1)
├── maximizeTheCuts(2, 2, 1, 1)  // Cut of length x
│   ├── maximizeTheCuts(0, 2, 1, 1)  // Cut of length x (reaches base case)
│   ├── maximizeTheCuts(1, 2, 1, 1)  // Cut of length y
│   │   ├── maximizeTheCuts(-1, 2, 1, 1) // Cut of length x (invalid, n < 0)
│   │   ├── maximizeTheCuts(0, 2, 1, 1)  // Cut of length y (reaches base case)
│   │   └── maximizeTheCuts(0, 2, 1, 1)  // Cut of length z (reaches base case)
│   └── maximizeTheCuts(1, 2, 1, 1)  // Cut of length z
│       ... (similar to the previous branch)
├── maximizeTheCuts(3, 2, 1, 1)  // Cut of length y
│   ├── maximizeTheCuts(1, 2, 1, 1)  // Cut of length x
│   │   ...
│   ├── maximizeTheCuts(2, 2, 1, 1)  // Cut of length y
│   │   ...
│   └── maximizeTheCuts(2, 2, 1, 1)  // Cut of length z
│       ...
└── maximizeTheCuts(3, 2, 1, 1)  // Cut of length z
    ...

    Time Complexity: O(3^n)
    Space Complexity: O(n)

https://www.geeksforgeeks.org/problems/cutted-segments1642/1
'''


class Solution:
    # Function to find the maximum number of cuts.
    def maximizeTheCuts(self, n, x, y, z):
        # Base case: when the length of the rod is zero,
        # no more cuts can be made.
        if n == 0:
            return 0

        # Base case: when the length of the rod is negative,
        # the cut is not possible, return negative infinity
        # to indicate the impossibility of such a cut.
        if n < 0:
            return float('-inf')

        # Recursively attempt to cut the rod by length x,
        # and increase the count of cuts by 1.
        a = 1 + self.maximizeTheCuts(n - x, x, y, z)

        # Recursively attempt to cut the rod by length y,
        # and increase the count of cuts by 1.
        b = 1 + self.maximizeTheCuts(n - y, x, y, z)

        # Recursively attempt to cut the rod by length z,
        # and increase the count of cuts by 1.
        c = 1 + self.maximizeTheCuts(n - z, x, y, z)

        # Return the maximum number of cuts among a, b, and c.
        return max(a, b, c)


# code here

# {
# Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        x, y, z = [int(x) for x in input().split()]

        print(Solution().maximizeTheCuts(n, x, y, z))
# } Driver Code Ends
