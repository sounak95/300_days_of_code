# https://leetcode.com/problems/climbing-stairs/

'''
                            climbStairs(4)
                           /             \
             climbStairs(3)                climbStairs(2)
             /         \                     /         \
climbStairs(2)   climbStairs(1)   climbStairs(1)   climbStairs(0)
   /      \           /                  |                |
climbStairs(1) climbStairs(0)       1 (base case)      1 (base case)
    |                |
    1               1
 (base case)     (base case)

'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n < 0:
            return 0

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)