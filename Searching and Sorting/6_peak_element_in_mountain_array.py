# https://leetcode.com/problems/find-peak-element/

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        e=len(nums)-1
        mid = s+(e-s)//2
        # to avoid infinite loop s<e and not s<=e
        while(s<e):
            if nums[mid]<nums[mid+1]:
                #goto B or peak
                s=mid+1
            elif nums[mid]>nums[mid+1]:
                #goto A but don't loose peak element
                e=mid

            mid=s+(e-s)//2

        return s # or return e
