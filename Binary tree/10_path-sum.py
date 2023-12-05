# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def solve(self, root,targetSum, sum ):
        if root ==None:
            return False

        sum+=root.val

        if root.left==None and root.right==None:
            if sum==targetSum:
                return True
            else:
                return False

        left_ans = self.solve(root.left, targetSum, sum)
        right_ans = self.solve(root.right, targetSum, sum)

        return left_ans or right_ans

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        sum=0
        return self.solve(root, targetSum, sum)


