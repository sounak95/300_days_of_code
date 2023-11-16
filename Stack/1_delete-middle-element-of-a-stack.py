# https://www.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1

class Solution:

    def helper(self, s, pos):

        # base case
        if pos==1:
            s.pop()
            return

        # 1 case hum solve krenge
        temp = s[-1]
        pos-=1
        s.pop()

        # leave rest to recursion
        self.helper(s, pos)

        # backtrack
        s.append(temp)


    # Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        pos =(sizeOfStack // 2) + 1
        self.helper(s, pos)

# code here