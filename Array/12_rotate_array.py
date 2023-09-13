# https://leetcode.com/problems/rotate-array/description/


# modulus technique
# space complexity o(n)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums_copy = nums[:]
        for i in range(n):
            new_index =  (i+k)%n
            nums[new_index] = nums_copy[i]

s=Solution()
nums= [1,2,3,4,5,6,7]
s.rotate(nums, 3)
print(nums)