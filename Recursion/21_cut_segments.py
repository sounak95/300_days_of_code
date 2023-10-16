# User function Template for python3


class Solution:

    # Function to find the maximum number of cuts.
    def maximizeTheCuts(self, n, x, y, z):
        if n==0:
            return 0
        if n<0:
            return float('-inf')
        a = 1+ self.maximizeTheCuts(n-x, x,y,z)
        b = 1 + self.maximizeTheCuts(n - y, x, y, z)
        c = 1 + self.maximizeTheCuts(n - z, x, y, z)

        return max(a,b,c)


# code here


# {
# Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        x, y, z = [int(x) for x in input().split()]

        print(Solution().maximizeTheCuts(n, x, y, z))
# } Driver Code Ends