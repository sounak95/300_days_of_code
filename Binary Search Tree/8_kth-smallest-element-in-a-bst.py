# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):

    def solve(self, root, K):
        if not root:
            return -1

        # left

        leftAns = self.solve(root.left, K)

        if leftAns != -1:
            return leftAns

        # N

        K[0] -= 1
        if K[0] == 0:
            return root.val

        rightAns = self.solve(root.right, K)
        return rightAns

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.solve(root, [k])
