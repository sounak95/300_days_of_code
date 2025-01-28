# https://leetcode.com/problems/coin-change/
'''
solve([1, 2], 4)
├── solve([1, 2], 3) // using a coin of 1
│   ├── solve([1, 2], 2) // using a coin of 1
│   │   ├── solve([1, 2], 1) // using a coin of 1
│   │   │   ├── solve([1, 2], 0) // using a coin of 1
│   │   │   │   └── (0) // base case, amount is 0
│   │   │   └── solve([1, 2], -1) // using a coin of 2
│   │   │       └── (∞) // base case, amount is negative
│   │   ├── solve([1, 2], 0) // using a coin of 2
│   │   │   └── (0) // base case, amount is 0
│   ├── solve([1, 2], 1) // using a coin of 2
│   │   ├── solve([1, 2], 0) // using a coin of 1
│   │   │   └── (0) // base case, amount is 0
├── solve([1, 2], 2) // using a coin of 2
│   ├── solve([1, 2], 1) // using a coin of 1
│   │   ├── solve([1, 2], 0) // using a coin of 1
│   │   │   └── (0) // base case, amount is 0
│   ├── solve([1, 2], 0) // using a coin of 2
│   │   └── (0) // base case, amount is 0

Time Complexity: O(k^amount)  k=len(coins)
Space Complexity: O(amount)
'''


class Solution(object):

    def solve(self, coins, amount):
        # Base case: If the amount is 0, no more coins are needed to make the amount.
        if amount == 0:
            return 0

        # Base case: If the amount becomes negative, the solution is not feasible.
        # Return infinity to signify that this is not a valid solution.
        if amount < 0:
            return float('inf')

        # Initialize the minimum number of coins needed to make the amount as infinity.
        # This will be updated to the minimum value found during the recursion.
        mini = float('inf')

        # Iterate over each coin in the list of coins.
        for coin in coins:
            # Recursively call the solve function to find the minimum number of coins
            # needed to make the new amount, which is the current amount minus the value of the coin.
            rec_ans = self.solve(coins, amount - coin)

            # If a solution is found (not infinity), add 1 to represent the current coin being used.
            ans = 1 + rec_ans

            # Update the minimum number of coins needed if the current solution
            # uses fewer coins than the previous minimum.
            mini = min(mini, ans)

        # Return the minimum number of coins needed to make up the amount.
        # If no solution is found, this will return infinity.
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
