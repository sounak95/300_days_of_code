
# https://leetcode.com/problems/maximal-square/description/


class Solution(object):

    def helper(self, matrix, i, j, row, col , maxi):
        # base case
        if i>= row or j>=col:
            return 0

        # Explore all 3 directions
        right = self.helper( matrix, i, j+1, row, col , maxi)
        diagonal = self.helper(matrix, i+1, j + 1, row, col, maxi)
        down = self.helper( matrix, i+1, j, row, col , maxi)

        if matrix[i][j]=='1':
            ans = 1+ min(right,min(diagonal, down))
            # ye important hai
            maxi[0] = max(maxi[0], ans)
            return ans

        else:
            # agar 0 pr hi khade ho toh answer bhi zero hga
            return 0

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxi = [0]
        ans = self.helper(matrix, 0, 0, len(matrix), len(matrix[0]), maxi)
        return maxi[0]* maxi[0]