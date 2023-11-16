# https://practice.geeksforgeeks.org/problems/sort-a-stack/1

class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack

    def insertSorted(self, s, element):
        # base case
        if len(s)==0 or element>s[-1]:
            s.append(element)
            return

        #solve one case
        temp = s[-1]
        s.pop()

        # recursion
        self.insertSorted(s, element)

        # backtracking
        s.append(temp)

    def Sorted(self, s):
        # Base case
        if len(s)==0:
            return

        # solve one case
        temp = s[-1]
        s.pop()

        # recursion
        self.Sorted(s)

        #backtracking
        self.insertSorted(s, temp)




#{
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends