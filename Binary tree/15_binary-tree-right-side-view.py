# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def solve(self, root, level, right_view):
        if root==None:
            return
        if level==len(right_view):
            right_view.append(root.data)

        self.solve(root.right, level+1, right_view)
        self.solve(root.left, level + 1, right_view)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        right_view=[]
        self.solve(root, 0, right_view)
        return right_view

