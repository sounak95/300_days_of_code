# https://leetcode.com/problems/row-with-maximum-ones/

'''
Time complexity: o(m*n)
Space complexity: o(1)
'''
class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        one_count = -float('inf')
        rows = len(mat)
        cols = len(mat[0])
        row = 0
        for i in range(rows):
            count = 0
            for j in range(cols):
                if mat[i][j] == 1:
                    count += 1

            if count > one_count:
                one_count = count
                row = i
        return [row, one_count]