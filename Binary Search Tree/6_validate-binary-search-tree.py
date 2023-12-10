
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def solve(self, root, lowerBound, upperBound):
        if not root:
            return True

        cond1 = root.val > lowerBound
        cond2 = root.val < upperBound

        leftAns = self.solve(root.left, lowerBound, root.val)
        rightAns = self.solve(root.right, root.val, upperBound)

        return cond1 and cond2 and leftAns and rightAns

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lowerBound = float('-inf')
        upperBound = float('inf')

        return self.solve(root, lowerBound, upperBound)

