# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/


class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        pick_p =0
        pick_m=0
        pick_g=0

        last_p=0
        last_m=0
        last_g=0

        travel_p=0
        travel_m=0
        travel_g=0

        for i, str1 in enumerate(garbage):
            for ch in str1:
                if ch=='G':
                    pick_g+=1
                    last_g=i
                elif ch=='M':
                    pick_m+=1
                    last_m=i
                elif ch=='P':
                    pick_p+=1
                    last_p=i

        for i in range(last_g):
            travel_g+=travel[i]

        for i in range(last_m):
            travel_m += travel[i]

        for i in range(last_p):
            travel_p += travel[i]

        total_cost = pick_g+travel_g + pick_m+travel_m + pick_p+travel_p
        return total_cost