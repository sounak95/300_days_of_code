# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def storeInorder(self, root, inorder):
        if not root:
            return
        self.storeInorder(root.left, inorder)
        inorder.append(root.val)
        self.storeInorder(root.right, inorder)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        inorder = []
        self.storeInorder(root, inorder)

        s = 0
        e = len(inorder) - 1

        while (s < e):
            sum = inorder[s] + inorder[e]

            if sum == k:
                return True

            if sum < k:
                s += 1
            elif sum > k:
                e -= 1

        return False