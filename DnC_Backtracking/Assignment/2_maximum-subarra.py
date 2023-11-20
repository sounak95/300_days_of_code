#https://leetcode.com/problems/maximum-subarray/

'''
maxSubArray(nums, 0, 3) # Original call with the full array
|
+---> maxSumArrayHelper(nums, 0, 1) # Left side of the array
|     |
|     +---> maxSumArrayHelper(nums, 0, 0) # Base case, single element (a)
|     |
|     +---> maxSumArrayHelper(nums, 1, 1) # Base case, single element (b)
|     |
|     +---> Calculate cross-border sum for elements (a, b)
|
+---> maxSumArrayHelper(nums, 2, 3) # Right side of the array
      |
      +---> maxSumArrayHelper(nums, 2, 2) # Base case, single element (c)
      |
      +---> maxSumArrayHelper(nums, 3, 3) # Base case, single element (d)
      |
      +---> Calculate cross-border sum for elements (c, d)

+---> Calculate cross-border sum for the entire array (a, b, c, d)

'''

class Solution(object):

    def helper(self, nums, s, e):
        if s==e:
            return nums[s]

        mid = s+(e-s)//2

        left_max = self.helper(nums, s, mid)
        right_max = self.helper(nums, mid+1, e)

        left_border_max = float('-inf')
        right_border_max = float('-inf')
        left_border_sum = 0
        right_border_sum=0

        for i in range(mid, s-1, -1):
            left_border_sum+=nums[i]
            left_border_max=max(left_border_sum, left_border_max)

        for i in range(mid+1, e+1):
            right_border_sum+=nums[i]
            right_border_max=max(right_border_sum, right_border_max)

        cross_border_sum = left_border_max + right_border_max

        return max(cross_border_sum, max(left_max, right_max))




    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)

