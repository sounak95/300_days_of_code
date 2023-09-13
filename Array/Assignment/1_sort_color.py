# https://leetcode.com/problems/sort-colors/
# 3 pointer technique
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m=0
        l=0
        h=len(nums)-1

        while(m<=h):
            if nums[m]==0:
                nums[m],nums[l] = nums[l], nums[m]
                l+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m], nums[h]= nums[h], nums[m]
                h-=1

        return nums

