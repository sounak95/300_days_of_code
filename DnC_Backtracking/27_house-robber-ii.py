# https://leetcode.com/problems/house-robber-ii/submissions/1091169384/

'''
rob(nums)
├─ h(0, 2) [Option 1: Start from first element]
│  ├─ h(2, 2) [Rob house 0, can now rob house 2]
│  │  ├─ h(4, 2) [Base case: s > e]
│  │  └─ h(3, 2) [Rob house 2]
│  │     └─ h(5, 2) [Base case: s > e]
│  └─ h(1, 2) [Don't rob house 0]
│     ├─ h(3, 2) [Rob house 1]
│     │  └─ h(5, 2) [Base case: s > e]
│     └─ h(2, 2) [Don't rob house 1]
│        ├─ h(4, 2) [Base case: s > e]
│        └─ h(3, 2) [Rob house 2]
│           └─ h(5, 2) [Base case: s > e]
└─ h(1, 3) [Option 2: Skip first element]
   ├─ h(3, 3) [Rob house 1]
   │  ├─ h(5, 3) [Base case: s > e]
   │  └─ h(4, 3) [Don't rob house 3]
   │     └─ h(6, 3) [Base case: s > e]
   └─ h(2, 3) [Don't rob house 1]
      ├─ h(4, 3) [Rob house 2]
      │  └─ h(6, 3) [Base case: s > e]
      └─ h(3, 3) [Don't rob house 2]
         ├─ h(5, 3) [Base case: s > e]
         └─ h(4, 3) [Rob house 3]
            └─ h(6, 3) [Base case: s > e]

'''


class Solution(object):


    def helper(self, nums, s, e):
        # base case
        if s>e:
            return 0

        # chori karlo -> ith index pr
        option1 = nums[s] + self.helper(nums, s+2, e)

        # chori mat karo  -> ith index pr
        option2 = 0 + self.helper(nums, s + 1, e)

        return max(option1, option2)


    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # single element - yha pr maine glti ki thi
        if len(nums)==1:
            return nums[0]

        option1 = self.helper(nums, 0, len(nums)-2)
        option2 = self.helper(nums, 1, len(nums)-1)

        return max(option1, option2)