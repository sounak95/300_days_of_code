# https://practice.geeksforgeeks.org/problems/array-to-bst4443/1

# construct BST from inorder

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:

    def solve(self, inorder, s , e):
        if s>e:
            return None

        mid = s+(e-s)//2
        root = TreeNode(inorder[mid])

        root.right = self.solve(inorder, mid+1, e)
        root.left = self.solve(inorder, s, mid-1)

        return root


    def preorder(self, root, ans):

        if root is None:
            return
        ans.append(root.data)
        self.preorder(root.left, ans)
        self.preorder(root.right, ans)

    def sortedArrayToBST(self, nums):
        # code here
        inorder = nums
        ans=[]
        root= self.solve(nums, 0, len(nums)-1)
        self.preorder(root, ans)
        return ans



#{
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	nums = list(map(int, input().split()))
	obj = Solution()
	ans = obj.sortedArrayToBST(nums)
	for _ in ans:
		print(_, end = " ")
	print()

# } Driver Code Ends