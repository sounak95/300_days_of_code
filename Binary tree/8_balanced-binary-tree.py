# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def height(self, root):
        if root==None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        height = max(left_height, right_height) +1

        return height

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root==None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        diff = abs (left_height-right_height)
        curr_node_ans = diff<=1

        left_node_ans = self.isBalanced(root.left)
        right_node_ans = self.isBalanced(root.right)

        ans= curr_node_ans and left_node_ans and right_node_ans

        return ans
