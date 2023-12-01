# https://leetcode.com/problems/sliding-window-maximum/

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dequeue = []
        ans = []
        # process the first window
        for i in range(k):
            element = nums[i]
            # pop the smaller elemenets from back
            while (not len(dequeue) == 0 and element > nums[dequeue[-1]]):
                dequeue.pop()

            # append the element from rear
            dequeue.append(i)

        # process remaining window
        print(dequeue)
        for i in range(k, len(nums)):
            element = nums[i]
            # store front element to ans of the previous window
            ans.append(nums[dequeue[0]])

            # check if front index in range else pop from front
            while (not len(dequeue) == 0 and i - dequeue[0] >= k):
                # pop front
                dequeue.pop(0)

            # pop the smaller elemenets from back
            while (not len(dequeue) == 0 and element > nums[dequeue[-1]]):
                # pop back
                dequeue.pop()

            dequeue.append(i)
            print(i, dequeue)
        # process last window
        ans.append(nums[dequeue[0]])
        print(dequeue)
        return ans

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],2))