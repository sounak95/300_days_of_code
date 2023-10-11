# https://leetcode.com/problems/climbing-stairs/


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