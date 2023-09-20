# https://practice.geeksforgeeks.org/problems/sum-of-two-numbers-represented-as-arrays3110/1

#User function Template for python3
class Solution:

    def findSum(self,a, b):
        m=len(a)
        n= len(b)
        i=m-1
        j=n-1
        carry=0
        ans=[]
        while(i>=0 and j>=0):
            num=a[i]+b[j]+carry
            digit = num%10
            carry= num//10
            ans.append(str(digit))
            i-=1
            j-=1

        while(i>=0):
            num = a[i] + 0 + carry
            digit = num % 10
            carry = num // 10
            ans.append(str(digit))
            i -= 1

        while ( j >= 0):
            num = 0 + b[j] + carry
            digit = num % 10
            carry = num // 10
            ans.append(str(digit))
            j -= 1

        if carry>0:
            ans.append(str(carry))

        reversed_list = list(reversed(ans))
        return "".join(reversed_list)


#{
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSum(a, b)
        for i in ans:
            print(i, end=" ")
        print()
        tc -= 1

# } Driver Code Ends