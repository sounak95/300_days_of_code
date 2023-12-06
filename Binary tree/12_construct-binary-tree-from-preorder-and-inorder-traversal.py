# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def solve(self, preorder,preindex, search_map,inorder_start , inorder_end, size):

        if preindex[0]>size or inorder_start>inorder_end:
            return None

        pre_index = preindex[0]
        element = preorder[pre_index]

        Node = TreeNode(element)

        # search in inorder
        position = search_map[element]

        preindex[0]=pre_index+1
        Node.left = self.solve(preorder,preindex, search_map,inorder_start , position-1, size)
        Node.right = self.solve(preorder, preindex, search_map, position+1, inorder_end, size)

        return Node

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        preindex=[0]
        search_map={}

        for i, ele in enumerate(inorder):
            search_map[ele] = i

        return self.solve(preorder,preindex,search_map, 0, len(inorder)-1, len(inorder))