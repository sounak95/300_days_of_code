# https://practice.geeksforgeeks.org/problems/insert-an-element-at-the-bottom-of-a-stack/1

# User function Template for python3
class Solution:
    def insertAtBottom(self, St, X):
        # base case
        if len(St) == 0:
            St.append(X)
            return St
        # solve one case
        temp = St[-1]
        St.pop()

        # recursion
        St = self.insertAtBottom(St, X)

        # backtracking
        St.append(temp)

        return St


# {
# Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        n, x = map(int, input().split())
        stack = list(map(int, input().split()))
        obj = Solution()
        ans = obj.insertAtBottom(stack, x)
        for e in ans:
            print(e, end=" ")
        print()

# } Driver Code Ends

