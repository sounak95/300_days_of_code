# https://www.geeksforgeeks.org/problems/painting-the-fence3727/1
'''
returns the number of ways in which the fence can be painted (modulo 109 + 7).
'''
MOD = 10**9 + 7


class Solution:

  def solve_using_rec(self, n, k):
    #code here
    if n == 1:
      return k

    if n == 2:
      return k + k * (k - 1)

    return (k - 1) * (self.solve_using_rec(n - 1, k) +
                      self.solve_using_rec(n - 2, k))

  def solve_using_mem(self, n, k, dp):
    if n == 1:
      return k

    if n == 2:
      return k + k * (k - 1)

    if dp[n] != -1:
      return dp[n]

    dp[n] = (k - 1) * (self.solve_using_mem(n - 1, k, dp) +
                       self.solve_using_mem(n - 2, k, dp)) % MOD

    return dp[n]

  def solve_using_tab(self, n, k):
    dp = [-1] * (n + 1)

    dp[1] = k

    if n == 1:
      return dp[1]

    dp[2] = k + k * (k - 1)

    if n == 2:
      return dp[2]

    for i in range(3, n + 1):
      dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2]) % MOD

    return dp[n]

  def solve_using_so(self, n, k):
    prev2 = k

    if n == 1:
      return prev2

    prev1 = k + k * (k - 1)

    if n == 2:
      return prev1

    curr = 0
    for i in range(3, n + 1):
      curr = (k - 1) * (prev1 + prev2) % MOD

      prev1, prev2 = curr, prev1

    return curr

  def countWays(self, n, k):
    # return self.solve_using_rec(n,k)
    # dp = [-1] * (n + 1)
    # return self.solve_using_mem(n, k, dp)
    # return self.solve_using_tab(n, k)
    return self.solve_using_so(n, k)
