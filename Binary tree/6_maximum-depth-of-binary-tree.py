# https://www.geeksforgeeks.org/problems/maximum-depth-of-binary-tree/1


# {
# Driver Code Starts
# Initial Template for Python 3

# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def maxDepth(self, root):
        if root==None:
            return 0

        maxDepth_left = self.maxDepth(root.left)
        maxDepth_right = self.maxDepth(root.right)

        maxDepth = max(maxDepth_left, maxDepth_right)+1
        return maxDepth


    def maxDepth1(self, root):
        if root==None:
            return 0

        q = []
        q.append(root)
        q.append(None)
        height=1

        while (len(q) != 0):

            front = q.pop(0)

            if front == None:

                if len(q) != 0:
                    q.append(None)
                    height += 1
            else:
                if front.left != None:
                    q.append(front.left)

                if front.right != None:
                    q.append(front.right)

        return height


# {
# Driver Code Starts.

from collections import defaultdict
from collections import deque
from sys import stdin, stdout


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        s = input()
        root = buildTree(s)

        res = Solution().maxDepth(root)
        print(res)

# } Driver Code Ends