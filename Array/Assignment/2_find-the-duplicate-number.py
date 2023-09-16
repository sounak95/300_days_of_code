# https://leetcode.com/problems/find-the-duplicate-number/description/

'''
Sorting technique
Time complexity: O(nlogn)
Space complexity: O(1)
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]
        return -1

# '''
# Visited solution
# Time complexity: O(n)
# Space complexity: O(1)
# '''
#
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=-1
        for i, ele in enumerate(nums):
            index = abs(ele)
            #check if already visited
            if nums[index]<0:
                ans=index
            else:
                # mark as visited
                nums[index] = -1*nums[index]
        return ans

'''
Positioning technique
Time complexity: O(n)
Space complexity: O(1)
'''


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        while(nums[0]!=nums[nums[0]]):
            #swap
            index=nums[0]
            nums[0], nums[index] = nums[index], nums[0]
        return nums[0]

s=Solution()
print(s.findDuplicate([1,3,4,2,2]))

