# https://leetcode.com/problems/house-robber/
# The problem is to find the maximum amount of money you can rob tonight without alerting the police.
# The constraint is that you cannot rob adjacent houses.
'''
rob([2,7,9,3,1], 0)
├── rob([2,7,9,3,1], 2) // Choose to rob house 0
│   ├── rob([2,7,9,3,1], 4) // Choose to rob house 2
│   │   ├── rob([2,7,9,3,1], 6) // Choose to rob house 4 (base case, out of bounds)
│   │   └── rob([2,7,9,3,1], 5) // Skip house 4 (base case, out of bounds)
│   └── rob([2,7,9,3,1], 3) // Skip house 2
│       ├── rob([2,7,9,3,1], 5) // Choose to rob house 3 (base case, out of bounds)
│       └── rob([2,7,9,3,1], 4) // Skip house 3
│           ├── rob([2,7,9,3,1], 6) // Choose to rob house 4 (base case, out of bounds)
│           └── rob([2,7,9,3,1], 5) // Skip house 4 (base case, out of bounds)
└── rob([2,7,9,3,1], 1) // Skip house 0
    ├── rob([2,7,9,3,1], 3) // Choose to rob house 1
    │   ├── rob([2,7,9,3,1], 5) // Choose to rob house 3 (base case, out of bounds)
    │   └── rob([2,7,9,3,1], 4) // Skip house 3
    │       ├── rob([2,7,9,3,1], 6) // Choose to rob house 4 (base case, out of bounds)
    │       └── rob([2,7,9,3,1], 5) // Skip house 4 (base case, out of bounds)
    └── rob([2,7,9,3,1], 2) // Skip house 1
        ├── rob([2,7,9,3,1], 4) // Choose to rob house 2
        │   ├── rob([2,7,9,3,1], 6) // Choose to rob house 4 (base case, out of bounds)
        │   └── rob([2,7,9,3,1], 5) // Skip house 4 (base case, out of bounds)
        └── rob([2,7,9,3,1], 3) // Skip house 2
            ├── rob([2,7,9,3,1], 5) // Choose to rob house 3 (base case, out of bounds)
            └── rob([2,7,9,3,1], 4) // Skip house 3
                ├── rob([2,7,9,3,1], 6) // Choose to rob house 4 (base case, out of bounds)
                └── rob([2,7,9,3,1], 5) // Skip house 4 (base case, out of bounds)


Time Complexity: O(2^n)
Space Complexity: O(n)
'''


class Solution(object):

    # A recursive function to solve the problem for a given index.
    # 'nums' is the list of money in each house, 'size' is the total number of houses,
    # and 'index' is the current position in the list.
    def solve(self, nums, size, index):
        # Base case: If the current index is beyond the size of the list, return 0 because
        # there are no more houses to consider.
        if index >= size:
            return 0

        # Recursive case 1:
        # Choose the current house to rob (nums[index]) and add the value to the result of
        # the recursive call, skipping the next house (since we can't rob adjacent houses).
        option1 = nums[index] + self.solve(nums, size, index + 2)

        # Recursive case 2:
        # Do not rob the current house, proceed to check the next house.
        option2 = 0 + self.solve(nums, size, index + 1)

        # Return the maximum of the two options for this call.
        return max(option1, option2)

    # This is the main function to solve the house robber problem.
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Call the recursive function with the initial index 0 to start from the first house.
        ans = self.solve(nums, len(nums), 0)
        # The final answer, which is the maximum amount of money that can be robbed.
        return ans
