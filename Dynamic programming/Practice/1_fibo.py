# https://leetcode.com/problems/fibonacci-number/description/


class Solution(object):

  def fib_rec(self, n):

    if n == 0:
      return 0

    if n == 1:
      return 1

    return self.fib_rec(n - 1) + self.fib_rec(n - 2)

  def fib_mem(self, n, dp):
    if n == 0:
      return 0

    if n == 1:
      return 1

    if dp[n] != -1:
      return dp[n]

    dp[n] = self.fib_mem(n - 1, dp) + self.fib_mem(n - 2, dp)

    return dp[n]

  def fib_tab(self, n):
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

  def fib_so(self, n):

    if n == 0:
      return 0

    if n == 1:
      return 1

    prev = 0

    curr = 1

    for i in range(2, n + 1):
      ans = prev + curr

      prev = curr
      curr = ans

    return ans

  def fib(self, n):
    dp = [-1] * (n + 1)
    return self.fib_mem(n, dp)
