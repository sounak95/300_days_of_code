# https://leetcode.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        balance=0
        deficit=0
        start=0

        for i in range(len(gas)):
            balance+=gas[i] - cost[i]

            if balance<0:
                deficit+=abs(balance)
                start=i+1
                balance=0

        if balance-deficit>=0:
            return start
        else:
            return -1