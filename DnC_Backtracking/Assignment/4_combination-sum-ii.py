# https://leetcode.com/problems/combination-sum-ii/

class Solution(object):

    def helper(self, candidates, target, v, ans, index):
        if target == 0:
            ans.append(list(v))
            return
        if target < 0:
            return

        for i in range(index, len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            v.append(candidates[i])
            self.helper(candidates, target - candidates[i], v, ans, i+1)
            v.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        v = []
        ans = []
        self.helper(sorted(candidates), target, v, ans, 0)

        return ans

l=[1,2,3,-1]
print(sorted(l))