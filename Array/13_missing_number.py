
# https://leetcode.com/problems/missing-number/description/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        sum = n*(n+1)//2

        s=0
        for ele in nums:
            s+=ele

        return sum-s