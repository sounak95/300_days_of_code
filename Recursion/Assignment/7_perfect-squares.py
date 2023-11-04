
# https://leetcode.com/problems/perfect-squares/

'''
numSquares(5)
│
└─ helper(5)
   ├─ helper(4)  // Trying 1^2 = 1, so we subtract 1 from 5
   │  ├─ helper(3)  // Trying 1^2 = 1, subtract from 4
   │  │  ├─ helper(2)  // Trying 1^2 = 1, subtract from 3
   │  │  │  ├─ helper(1)  // Trying 1^2 = 1, subtract from 2
   │  │  │  │  └─ helper(0)  // Base case, 0 remaining - 1 square
   │  │  │  └─ helper(1)  // Trying 1^2 = 1, subtract from 2
   │  │  │     └─ helper(0)  // Base case, 0 remaining - 1 square
   │  │  └─ helper(2)  // Trying 2^2 = 4, subtract from 3 (not possible, go to next i)
   │  └─ helper(0)  // Base case, 0 remaining - 1 square
   ├─ helper(1)  // Trying 2^2 = 4, subtract from 5
   │  └─ helper(0)  // Base case, 0 remaining - 1 square
   └─ [No further recursion since sqrt(5) < 3 and we don't consider non-integer squares]

'''


import math

class Solution(object):

    def helper(self, n):
        # Base case: if n is 0, the number of perfect squares required is 0 (1-1).
        if n == 0:
            return 1
        # If n is negative, no perfect square can be subtracted from it to reach 0.
        if n < 0:
            return 0
        # Initialize the minimum number of perfect squares to infinity.
        ans = float('inf')
        # Loop through all possible perfect squares smaller than or equal to n.
        for i in range(1, int(math.sqrt(n)) + 1):
            perf_sq = i * i  # Current perfect square.
            # Recursively subtract the perfect square from n and add 1 to the count.
            num_perf_sq = 1 + self.helper(n - perf_sq)
            # Find the minimum count of perfect squares.
            ans = min(ans, num_perf_sq)

        return ans

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Subtract 1 from the result to get the correct number of perfect squares.
        return self.helper(n) - 1

# Example usage:
sol = Solution()
print(sol.numSquares(5))  # Should return 2 because 5 = 1^2 + 2^2
