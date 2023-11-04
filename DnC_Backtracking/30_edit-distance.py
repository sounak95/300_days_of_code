# https://leetcode.com/problems/edit-distance/description/


class Solution(object):

    def solve(self, word1, word2, i, j):
        # base case
        if i>=len(word1):
            return len(word2)-j

        if j>=len(word2):
            return len(word1)-i

        ans=0

        if word1[i] == word2[j]:
            ans= 0+ self.solve(word1, word2, i+1, j+1)
        else:
            # no match
            # perform operation
            # insert
            option1 = 1+ self.solve(word1, word2, i, j+1)
            # remove
            option2 = 1 + self.solve(word1, word2, i+1, j)
            # replace
            option3 = 1+ self.solve(word1, word2, i+1, j+1)
            ans = min(option1, min(option2, option3))

        return ans


    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.solve(word1, word2, 0, 0)
