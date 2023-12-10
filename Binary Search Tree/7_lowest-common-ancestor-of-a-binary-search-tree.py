# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        # Case#1
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Case 2
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        #         # Case 3
        #         elif p.val<root.val and q.val>root.val:
        #             return root

        #         # Case 4
        #         elif q.val<root.val and p.val>root.val:
        #             return root

        return root