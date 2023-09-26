# https://leetcode.com/problems/palindromic-substrings/

class Solution(object):

    def expand(self,s, i, j):
        count=0
        while(i>=0 and j<len(s) and s[i]==s[j]):
            count+=1
            i-=1
            j+=1
        return count


    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_count = 0
        for i in range(len(s)):
            # odd
            count_odd = self.expand(s, i, i)
            # even
            count_even = self.expand(s, i , i+1)

            total_count+=count_even+count_odd

        return total_count
