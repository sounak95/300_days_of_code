# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):

    def binary_search(self, arr, start, end, target):
        mid = (start + end) // 2
        while (start <= end):
            if arr[mid] == target:
                return mid
            if target > arr[mid]:
                # goto right
                start = mid + 1
            elif target < arr[mid]:
                # goto left
                end = mid - 1
            mid = (start + end) // 2
        return -1

    def find_pivot_index(self, arr):
        s = 0
        n = len(arr)
        e = n - 1
        mid = s + (e - s) // 2

        while (s <= e):
            if s == e:  # if array contains single element
                return s
            if (mid - 1) >= 0 and arr and [mid] < arr[mid - 1]:
                return mid - 1
            elif (mid + 1) < n and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[s]:
                e = mid - 1
            else:
                s = mid + 1
            mid = s + (e - s) // 2
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums) - 1

        pivot_index = self.find_pivot_index(nums)
        ans = -1
        # Search in A
        if target >= nums[0] and target <= nums[pivot_index]:
            ans = self.binary_search(nums, 0, pivot_index, target)
        else:
            ans = self.binary_search(nums, pivot_index + 1, len(nums) - 1, target)
        return ans
s=Solution()
print(s.search([4,5,6,7,0,1,2], 0))