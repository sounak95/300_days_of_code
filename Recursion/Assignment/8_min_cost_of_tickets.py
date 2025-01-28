# https://leetcode.com/problems/minimum-cost-for-tickets/
'''
mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])
|
|-- helper([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15], 0)
|   |-- (1-day pass) Cost: 2 + helper([2,3,4,5,6,7,8,9,10,30,31], [2,7,15], 1)
|   |   `-- ...
|   |
|   |-- (7-day pass) Cost: 7 + helper([8,9,10,30,31], [2,7,15], 7)
|   |   |-- (1-day pass) Cost: 2 + helper([9,10,30,31], [2,7,15], 8)
|   |   |   `-- ...
|   |   |
|   |   `-- (7-day pass) Cost: 7 + helper([30,31], [2,7,15], 10)
|   |       |-- (1-day pass) Cost: 2 + helper([31], [2,7,15], 11)
|   |       |   `-- ...
|   |       |
|   |       `-- (7-day pass) Cost: 7 + helper([], [2,7,15], 12) // Base case reached, cost = 7
|   |
|   `-- (30-day pass) Cost: 15 + helper([], [2,7,15], 12) // Base case reached, cost = 15
|
`-- ... (Tree continues for all possible combinations)

'''


class Solution(object):

    def helper(self, days, costs, i):
        # base case
        if i >= len(days):
            return 0

        # 1 day pass
        cost1 = costs[0] + self.helper(days, costs, i + 1)

        pass_end_day = days[i] + 7 - 1
        j = i
        while (j < len(days) and days[j] <= pass_end_day):
            j += 1

        # 7 day pass
        cost7 = costs[1] + self.helper(days, costs, j)

        pass_end_day = days[i] + 30 - 1
        j = i
        while (j < len(days) and days[j] <= pass_end_day):
            j += 1

        # 30 days pass
        cost30 = costs[2] + self.helper(days, costs, j)

        return min(cost1, cost7, cost30)

    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        return self.helper(days, costs, 0)
