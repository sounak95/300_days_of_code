# https://leetcode.com/problems/coin-change/

class Solution(object):

    def solve(self,coins, amount ):
        if amount==0:
            return 0
        if amount<0:
            return float('inf')

        mini = float('inf')
        for coin in coins:
            rec_ans = self.solve(coins, amount-coin)
            ans = 1+ rec_ans
            mini = min(mini, ans)

        return mini


    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = self.solve(coins, amount)
        if ans == float('inf'):
            return -1
        else:
            return ans
