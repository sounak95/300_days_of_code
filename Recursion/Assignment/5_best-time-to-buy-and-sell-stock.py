

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''
Start:
    |
    |-- maxProfit([7, 1, 5])
    |       |
    |       |-- Initial call to helper([7, 1, 5], 0, inf, 0)
    |               |
    |               |-- Check prices[0] = 7, min_price = inf
    |               |      |
    |               |      |-- Update min_price = 7 (since 7 < inf)
    |               |      |
    |               |      |-- today_profit = 7 - 7 = 0
    |               |      |      |
    |               |      |      |-- max_profit remains 0 (since 0 == 0)
    |               |      |
    |               |      |-- Recursive call helper([7, 1, 5], 1, 7, 0)
    |               |               |
    |               |               |-- Check prices[1] = 1, min_price = 7
    |               |               |      |
    |               |               |      |-- Update min_price = 1 (since 1 < 7)
    |               |               |      |
    |               |               |      |-- today_profit = 1 - 1 = 0
    |               |               |      |      |
    |               |               |      |      |-- max_profit remains 0 (since 0 == 0)
    |               |               |      |
    |               |               |      |-- Recursive call helper([7, 1, 5], 2, 1, 0)
    |               |               |               |
    |               |               |               |-- Check prices[2] = 5, min_price = 1
    |               |               |               |      |
    |               |               |               |      |-- min_price remains 1 (since 5 > 1)
    |               |               |               |      |
    |               |               |               |      |-- today_profit = 5 - 1 = 4
    |               |               |               |      |      |
    |               |               |               |      |      |-- Update max_profit = 4 (since 4 > 0)
    |               |               |               |
    |               |               |               |-- Recursive call helper([7, 1, 5], 3, 1, 4)
    |               |               |                      |
    |               |               |                      |-- Base case reached (i == len(prices))
    |               |               |                      |
    |               |               |                      |-- Return max_profit = 4
    |               |               |
    |               |               |-- Return max_profit = 4
    |               |
    |               |-- Return max_profit = 4
    |
    |-- Return max_profit = 4
    |
End: Max Profit is 4




'''

class Solution(object):
    def helper(self, prices, i, min_price, max_profit):
        # Base case: if we've gone through all the prices, return the max profit calculated
        if i == len(prices):
            return max_profit

        # If the current price is less than the minimum price encountered so far,
        # update the minimum price
        if prices[i] < min_price:
            min_price = prices[i]

        # Calculate today's potential profit using the lowest price seen so far
        today_profit = prices[i] - min_price
        # If today's profit is greater than the maximum profit seen so far,
        # update the maximum profit
        if today_profit > max_profit:
            max_profit = today_profit

        # Recursive call to check the next day's price and update min_price and max_profit accordingly
        return self.helper(prices, i + 1, min_price, max_profit)

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Start the recursion with the first day, infinite as the initial minimum price,
        # and negative infinite as the initial maximum profit to ensure any profit will be greater
        return self.helper(prices, 0, float('inf'), 0)

# Example usage:
# sol = Solution()
# print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
