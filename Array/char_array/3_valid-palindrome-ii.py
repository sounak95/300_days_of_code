# https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):

    def check_palindrome(self,s,i,j):
        while(i<=j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1
        while(i<=j):
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                ans1 =self.check_palindrome(s,i+1,j)
                ans2 = self.check_palindrome(s,i,j-1)

                return ans1 or ans2
        return True

