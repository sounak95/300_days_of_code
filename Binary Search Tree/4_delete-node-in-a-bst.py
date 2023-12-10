# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxValue(self, root):
        temp = root
        while (temp.right != None):
            temp = temp.right

        return temp

    def minValue(self, root):
        temp = root
        while (temp.left != None):
            temp = temp.left

        return temp

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root.val == key:
            # 4 cases
            if root.left is None and root.right is None:
                return None
            elif root.left != None and root.right is None:
                childSubtree = root.left
                return childSubtree
            elif root.right != None and root.left is None:
                childSubtree = root.right
                return childSubtree
            else:
                maxi = self.maxValue(root.left)
                root.val = maxi.val

                root.left = self.deleteNode(root.left, maxi.val)
                return root


        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root

