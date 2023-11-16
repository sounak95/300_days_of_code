# https://practice.geeksforgeeks.org/problems/reverse-a-stack/1


# User function Template for python3

from typing import List


class Solution:
    def insertAtBottom(self, St, X):
        # base case
        if len(St) == 0:
            St.append(X)
            return
        # solve one case
        temp = St[-1]
        St.pop()

        # recursion
        self.insertAtBottom(St, X)

        # backtracking
        St.append(temp)

    def reverse(self, St):
        # base case
        if len(St) == 0:
            return

        # solve one case
        temp = St[-1]
        St.pop()

        # recursion
        self.reverse(St)

        # backtracking
        self.insertAtBottom(St, temp)


# {
# Driver Code Starts

# Initial Template for Python 3


for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends