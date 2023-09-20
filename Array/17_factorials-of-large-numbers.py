# https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1

# User function Template for python3

# User function Template for python3

class Solution:
    def factorial(self, N):
        ans = []
        ans.append(1)
        carry = 0
        for i in range(2, N + 1):
            for j in range(len(ans)):
                num = int(ans[j]) * i + carry
                digit = num % 10
                carry = num // 10
                ans[j]=digit

            while(carry):
                ans.append(carry%10)
                carry=carry//10

        reversed_list = list(reversed(ans))
        return reversed_list


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i, end="")
        print()

# } Driver Code Ends