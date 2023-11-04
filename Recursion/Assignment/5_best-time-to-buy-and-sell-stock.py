

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''
                                 h([7,1,5], 0, inf, 0)
                                         |
                                         |  [Check prices[0]: 7 < inf (No), max_profit remains 0]
                                         V
                                        h([7,1,5], 1, 7, 0)   <-- Updated min_price to 7
                                         |
                                         |  [Check prices[1]: 1 < 7 (Yes), update min_price to 1, max_profit remains 0]
                                         V
                                        h([7,1,5], 2, 1, 0)   <-- Updated min_price to 1
                                         |
                                         |  [Check prices[2]: 5 - 1 = 4 > 0 (Yes), update max_profit to 4]
                                         V
                                        h([7,1,5], 3, 1, 4)   <-- Reached end of array, return max_profit 4
                                         |
                                         V
                                        Return 4   <-- Maximum profit is 4



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
