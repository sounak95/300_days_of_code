# https://leetcode.com/problems/rotate-image/

class Solution(object):
    def reverse(self, l1):
        start=0
        end=len(l1)-1
        while(start<end):
            l1[start],l1[end]=l1[end],l1[start]
            start+=1
            end-=1
        return l1

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l1= matrix
        rows = len(l1)
        cols = len(l1[0])

        #transpose
        for i in range(rows):
            for j in range(i, cols):
                l1[i][j], l1[j][i] = l1[j][i], l1[i][j]

        #reverse
        for i in range(rows):
            # reversed_list = l1[i][::-1]
            l1[i] = self.reverse(l1[i])
