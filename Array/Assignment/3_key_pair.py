# https://practice.geeksforgeeks.org/problems/key-pair5616/1

#User function Template for python3
class Solution:
    # Brute Force
    def hasArrayTwoCandidates_brute_force(self, arr, n, x):
        for i in range(n):
            for j in range(i+1, n):
                if arr[i]+ arr[j]==x:
                    return True
        return False

        # Optimal

    '''
    Time complexity: O(nlogn)
    '''
    def hasArrayTwoCandidates(self, arr, n, x):
        s=0
        l=len(arr)-1
        arr=sorted(arr)
        while(s<l):
            if arr[s]+arr[l]==x:
                return True
            elif arr[s]+arr[l]<x:
                s+=1
            elif arr[s]+arr[l]>x:
                l-=1
        return False

#{
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends