# https://leetcode.com/problems/fibonacci-number/
class Solution:
  # plain recursion
  def solve_using_recursion(self, n):
    # base case
    if n == 0:
      return 0
    if n == 1:
      return 1
    # recursive relation
    ans = self.solve_using_recursion(n - 1) + self.solve_using_recursion(n - 2)
    return ans

  def solve_using_mem(self, n, dp):
    if n == 0:
      return 0

    if n == 1:
      return 1

    dp[0] = 0
    dp[1] = 1

    # check if already exists in dp, then return ans
    if dp[n] != -1:
      return dp[n]

    # recursive relation with storing ans in dp array
    dp[n] = self.solve_using_mem(n - 1, dp) + self.solve_using_mem(n - 2, dp)

    return dp[n]

  def solve_using_tab(self, n):
    dp = [-1] * (n + 1)

    if n == 0:
      return 0
    if n == 1:
      return 1

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

  def solve_using_tab_space_opt(self, n):

    if n == 0:
      return 0
    if n == 1:
      return 1

    prev = 0
    curr = 1

    for i in range(2, n + 1):
      ans = curr + prev

      curr, prev = ans, curr

    return ans

  def fib(self, n):
    dp = [-1] * (n + 1)
    # return self.solve_using_recursion(n)
    # return self.solve_using_mem(n, dp)
    # return self.solve_using_tab(n)
    return self.solve_using_tab_space_opt(n)


print(Solution().fib(6))
