
# https://leetcode.com/problems/search-a-2d-matrix/
'''
Time complexity: Log(m*n)
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row= len(matrix)
        col = len(matrix[0])
        n= row*col
        s=0
        e=n-1
        mid = s+(e-s)//2
        while(s<=e):
            row_index = mid/col
            col_index = mid%col

            curr_number = matrix[row_index][col_index]
            if curr_number==target:
                return True
            elif curr_number<target:
                s=mid+1
            else:
                e= mid-1
            mid = s+(e-s)//2

        return False

