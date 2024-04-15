# https://leetcode.com/problems/house-robber/description/


class Solution(object):

  def solve_using_rec(self, nums, i):
    if i >= len(nums):
      return 0

    include = nums[i] + self.solve_using_rec(nums, i + 2)
    exclude = 0 + self.solve_using_rec(nums, i + 1)

    ans = max(include, exclude)

    return ans

  def solve_using_mem(self, nums, i, dp):
    if i >= len(nums):
      return 0

    if dp[i] != -1:
      return dp[i]

    include = nums[i] + self.solve_using_rec(nums, i + 2)
    exclude = 0 + self.solve_using_rec(nums, i + 1)

    dp[i] = max(include, exclude)

    return dp[i]

  def solve_using_tab(self, nums):
    n = len(nums)
    dp = [-1] * n

    dp[n - 1] = nums[n - 1]

    for i in range(n - 2, -1, -1):
      temp_ans = 0
      if i + 2 < n:
        temp_ans = dp[i + 2]
      include = nums[i] + temp_ans
      exclude = 0 + dp[i + 1]
      dp[i] = max(include, exclude)

    return dp[0]

  def solve_using_so(self, nums):
    n = len(nums)
    next = 0  #i+2
    curr = 0
    prev = nums[n - 1]  #i+1

    for i in range(n - 2, -1, -1):

      include = nums[i] + next
      exclude = 0 + prev
      curr = max(include, exclude)

      prev, next = curr, prev

    return prev

  def rob(self, nums):
    """
      :type nums: List[int]
      :rtype: int
      """
    # return self.solve_using_rec(nums, 0)
    # n = len(nums)
    # dp = [-1] * n
    # return self.solve_using_mem(nums, 0, dp)
    # return self.solve_using_tab(nums)
    return self.solve_using_so(nums)
