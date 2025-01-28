# https://leetcode.com/problems/perfect-squares/
'''
Start: numSquares(13)
  |
  |--> helper(13)
         |
         |--> helper(12)  // Trying 1^2 = 1, subtract 1 from 13
         |       |
         |       |--> helper(11)  // Trying 1^2 = 1, subtract 1 from 12
         |       |       |
         |       |       |--> helper(10)  // Trying 1^2 = 1, subtract 1 from 11
         |       |       |       |
         |       |       |       |--> helper(9)  // Trying 1^2 = 1, subtract 1 from 10
         |       |       |       |       |
         |       |       |       |       |--> helper(8)  // Trying 1^2 = 1, subtract 1 from 9
         |       |       |       |       |       |
         |       |       |       |       |       |--> helper(7)  // Trying 1^2 = 1, subtract 1 from 8
         |       |       |       |       |       |       |
         |       |       |       |       |       |       |--> helper(6)  // Trying 1^2 = 1, subtract 1 from 7
         |       |       |       |       |       |       |       |
         |       |       |       |       |       |       |       |--> helper(5)  // Trying 1^2 = 1, subtract 1 from 6
         |       |       |       |       |       |       |       |       |
         |       |       |       |       |       |       |       |       |--> helper(4)  // Trying 1^2 = 1, subtract 1 from 5
         |       |       |       |       |       |       |       |       |       |
         |       |       |       |       |       |       |       |       |       |--> helper(3)  // Trying 1^2 = 1, subtract 1 from 4
         |       |       |       |       |       |       |       |       |       |       |
         |       |       |       |       |       |       |       |       |       |       |--> helper(2)  // Trying 1^2 = 1, subtract 1 from 3
         |       |       |       |       |       |       |       |       |       |       |       |
         |       |       |       |       |       |       |       |       |       |       |       |--> helper(1)  // Trying 1^2 = 1, subtract 1 from 2
         |       |       |       |       |       |       |       |       |       |       |       |       |
         |       |       |       |       |       |       |       |       |       |       |       |       |--> helper(0)  // Base case: 0 remaining (1 perfect square used)
         |       |       |       |       |       |       |       |       |       |       |       |
         |       |       |       |       |       |       |       |       |       |       |       |--> helper(1)  // Trying 1^2 = 1 again, subtract 1 from 2
         |       |       |       |       |       |       |       |       |       |       |               |
         |       |       |       |       |       |       |       |       |       |       |               |--> helper(0)  // Base case: 0 remaining (1 perfect square used)
         |       |       |       |       |       |       |       |       |       |       |
         |       |       |       |       |       |       |       |       |       |       |--> helper(2)  // Trying 2^2 = 4, subtract 4 from 3 (not possible)
         |       |       |       |       |       |       |       |       |       |
         |       |       |       |       |       |       |       |       |       |--> helper(0)  // Base case: 0 remaining (1 perfect square used)
         |       |       |       |       |       |       |       |
         |       |       |       |       |       |       |       |--> helper(1)  // Trying 2^2 = 4, subtract 4 from 6
         |       |       |       |       |       |       |               |
         |       |       |       |       |       |       |               |--> helper(0)  // Base case: 0 remaining (1 perfect square used)
         |       |       |       |       |       |       |
         |       |       |       |       |       |       |--> helper(0)  // Base case: 0 remaining (1 perfect square used)
         |       |       |       |       |       |
         |       |       |       |       |       |--> helper(4)  // Trying 2^2 = 4, subtract 4 from 9
         |       |       |       |       |               |
         |       |       |       |       |               |--> helper(0)  // Base case: 0 remaining (1 perfect square used)
         |       |       |       |       |
         |       |       |       |       |--> helper(0)  // Base case: 0 remaining (1 perfect square used)
         |       |       |       |
         |       |       |       |--> helper(1)  // Trying 2^2 = 4, subtract 4 from 5
         |       |       |               |
         |       |       |               |--> helper(0)  // Base case: 0 remaining (1 perfect square used)
         |       |       |
         |       |       |--> helper(0)  // Base case: 0 remaining (1 perfect square used)
         |       |
         |       |--> helper(4)  // Trying 3^2 = 9, subtract 9 from 12
         |               |
         |               |--> helper(0)  // Base case: 0 remaining (1 perfect square used)
         |
         |--> helper(9)  // Trying 2^2 = 4, subtract 4 from 13
                 |
                 |--> helper(0)  // Base case: 0 remaining (1 perfect square used)

'''

import math


class Solution(object):

    def helper(self, n):
        # Base case: if n is 0, the number of perfect squares required is 0.
        if n == 0:
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
        return self.helper(n)


# Example usage:
sol = Solution()
print(sol.numSquares(5))  # Should return 2 because 5 = 1^2 + 2^2
