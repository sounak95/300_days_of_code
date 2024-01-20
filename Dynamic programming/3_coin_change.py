# https://leetcode.com/problems/coin-change/


class Solution(object):

  def solve_using_rec(self, coins, amount):

    if amount == 0:
      return 0

    mini = float('inf')

    for i in range(len(coins)):

      if amount - coins[i] >= 0:
        recAns = self.solve_using_rec(coins, amount - coins[i])

        if recAns != float('inf'):
          ans = 1 + recAns
          mini = min(mini, ans)

    return mini

  def solve_using_mem(self, coins, amount, dp):
    if amount == 0:
      return 0

    if dp[amount] != -1:
      return dp[amount]
    mini = float('inf')
    for i in range(len(coins)):

      if amount - coins[i] >= 0:
        recAns = self.solve_using_rec(coins, amount - coins[i])

        if recAns != float('inf'):
          ans = 1 + recAns
          mini = min(mini, ans)

    dp[amount] = mini

    return dp[amount]

  def solve_using_tab(self, coins, amount):
    n = amount
    dp = [float('inf')] * (n + 1)
    
    if amount == 0:
      return 0

    dp[0] =0
    
    for value in range(1, n+1):
      
      mini = float('inf')
      for i in range(len(coins)):

        if value-coins[i]>=0:
          recAns = dp[value-coins[i]]

          if recAns!= float('inf'):
            ans = 1+ recAns
            mini = min(mini, ans)

      dp[value] = mini

    return dp[amount]
        
    

  def coinChange(self, coins, amount):
    """
      :type coins: List[int]
      :type amount: int
      :rtype: int
      """
    # ans = self.solve_using_rec(coins, amount)
    ans = self.solve_using_tab(coins, amount)
    # n = amount
    # dp = [-1] * (n + 1)
    # ans = self.solve_using_mem(coins, amount, dp)
    if ans == float('inf'):
      return -1
    return ans


print(Solution().coinChange([1, 2, 5], 100))
# print(Solution().coinChange([2], 3))
# print(Solution().coinChange([1], 0))
