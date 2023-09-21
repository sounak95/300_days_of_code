# https://leetcode.com/problems/sqrtx/

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=0
        e=x
        mid = s+(e-s)//2
        ans=-1
        while(s<=e):
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                ans=mid
                s=mid+1
            else:
                e=mid-1

            mid=s+(e-s)//2
        return ans
