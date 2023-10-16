# https://leetcode.com/problems/house-robber/

#max sum of non-adjacent elements


class Solution(object):

    def solve(self, nums, size, index):
        if index >= size:
            return 0

        option1 = nums[index] + self.solve(nums, size, index + 2)
        option2 = 0 + self.solve(nums, size, index + 1)

        return max(option1, option2)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = self.solve(nums, len(nums), 0)
        return ans