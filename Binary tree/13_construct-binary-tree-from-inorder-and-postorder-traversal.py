# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def solve(self, postorder,postindex, search_map,inorder_start , inorder_end, size):

        if postindex[0]<0 or inorder_start>inorder_end:
            return None

        post_index = postindex[0]
        element = postorder[post_index]

        Node = TreeNode(element)

        # search in inorder
        position = search_map[element]

        postindex[0]=post_index-1

        Node.right = self.solve(postorder, postindex, search_map, position+1, inorder_end, size)
        Node.left = self.solve(postorder, postindex, search_map, inorder_start, position - 1, size)

        return Node

    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        size = len(postorder)
        postindex=[size-1]
        search_map={}

        for i, ele in enumerate(inorder):
            search_map[ele] = i

        return self.solve(postorder,postindex,search_map, 0, len(inorder)-1, size)
