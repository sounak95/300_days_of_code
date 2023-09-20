# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        while(i<len(nums)):
            if nums[i]==nums[j]:
                i+=1
            else:
                j+=1
                nums[j] = nums[i]
                i+=1
        return j+1

