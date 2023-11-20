# https://leetcode.com/problems/combination-sum/


class Solution(object):

    def helper(self, candidates, target, v, ans, index):
        if target == 0:
            ans.append(list(v))
            return
        if target < 0:
            return

        for i in range(index, len(candidates)):
            v.append(candidates[i])
            self.helper(candidates, target - candidates[i], v, ans, i)
            v.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        v = []
        ans = []
        self.helper(candidates, target, v, ans, 0)

        return ans