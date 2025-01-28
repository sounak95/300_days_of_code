# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
'''
Start:
    |
    |-- numRollsToTarget(2, 3, 2)
           |
           |-- numRollsToTarget(1, 3, 1)  // Rolled a 1 on the first die
           |      |
           |      |-- numRollsToTarget(0, 3, 0)  // Rolled a 1 on the second die
           |      |      |
           |      |      |-- Return 1  // Base case: 0 dice left and target is 0
           |      |
           |      |-- numRollsToTarget(0, 3, -1) // Rolled a 2 on the second die
           |      |      |
           |      |      |-- Return 0  // Base case: target is negative
           |      |
           |      |-- numRollsToTarget(0, 3, -2) // Rolled a 3 on the second die
           |             |
           |             |-- Return 0  // Base case: target is negative
           |
           |-- numRollsToTarget(1, 3, 0)  // Rolled a 2 on the first die
           |      |
           |      |-- Return 0  // Any roll will result in sum > 2, so not shown
           |
           |-- numRollsToTarget(1, 3, -1) // Rolled a 3 on the first die
                  |
                  |-- Return 0  // No need to roll the second die since target is already negative

    |
    |-- Sum up all valid paths:
           |-- 1 (from numRollsToTarget(0, 3, 0) with 1 + 1)
           |-- 0 (from all other invalid paths)
    |
    |-- Return 1 as the total number of ways to achieve target 2 with 2 dice.


'''


class Solution(object):

    def numRollsToTarget(self, n, k, target):
        """
        This function computes the number of ways to roll n dice so that the sum of the face-up numbers equals the target.

        :type n: int: number of dice
        :type k: int: number of faces on each die
        :type target: int: target sum to achieve
        :rtype: int: number of ways to reach the target
        """

        # If the target sum becomes negative, it means this path is not possible
        # since dice cannot have negative values.
        if target < 0:
            return 0

        # If there are no more dice to roll (n == 0) and the target sum is achieved,
        # then this is a valid way to reach the target.
        if n == 0 and target == 0:
            return 1

        # If there are no more dice to roll but the target is not achieved,
        # or if there are dice left to roll but the target has been reduced to zero,
        # then this path is not a solution.
        if n == 0 or target == 0:
            return 0

        # Initialize the count of ways to 0.
        ans = 0

        # Loop through each face of the die.
        for i in range(1, k + 1):
            # For each face, recursively calculate the number of ways to achieve the
            # remaining target sum with the remaining number of dice.
            ans += self.numRollsToTarget(n - 1, k, target - i)

        # Return the total count of ways for this recursive call.
        return ans


# Example usage:
print(Solution().numRollsToTarget(2, 6, 7))
