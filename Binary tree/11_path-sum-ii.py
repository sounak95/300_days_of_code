# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def solve(self, root, targetSum, sum, temp_list, ans):
        if root == None:
            return

        sum += root.val
        temp_list.append(root.val)

        if root.left == None and root.right == None:
            if sum == targetSum:
                ans.append(temp_list)
            return

        self.solve(root.left, targetSum, sum, temp_list.copy(), ans)
        self.solve(root.right, targetSum, sum, temp_list.copy(), ans)

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        temp_list = []
        ans = []
        sum = 0
        self.solve(root, targetSum, sum, temp_list.copy(), ans)
        return ans