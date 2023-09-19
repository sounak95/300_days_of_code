
# https://leetcode.com/problems/spiral-matrix/

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        starting_row = 0
        starting_col = 0
        row_count= len(matrix)
        col_count = len(matrix[0])
        ending_row = row_count-1
        ending_col = col_count-1

        total_ele = row_count * col_count
        count = 0
        ans = []

        while (count < total_ele):
            for i in range(starting_col,ending_col+1):
                ans.append(matrix[starting_row][i])
                count+=1
            # print(ans)

            starting_row += 1
            if (count < total_ele):
                for i in range(starting_row,ending_row+1):
                    ans.append(matrix[i][ending_col])
                    count+=1
                ending_col -= 1
            # print(ans, ending_col, starting_col-1)

            if (count < total_ele):
                for i in range(ending_col , starting_col-1, -1):
                    ans.append(matrix[ending_row][i])
                    count+=1
                ending_row -= 1
            # print(ans)

            if (count < total_ele):
                for i in range(ending_row , starting_row-1, -1):
                    ans.append(matrix[i][starting_col])
                    count+=1
                starting_col += 1
            # print(ans, count, total_ele)
        return ans

s=Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.spiralOrder(matrix))