# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        isNegative = x<0
        if isNegative:
            x=-x

        ans=0
        num=x
        while(num>0):
            rem=num%10
            # Check for integer overflow before updating ans
            if ans > (2**31 - 1 - rem) // 10:
                return 0
            ans=ans*10+rem
            num=num//10
        if isNegative:
            return -ans
        return ans