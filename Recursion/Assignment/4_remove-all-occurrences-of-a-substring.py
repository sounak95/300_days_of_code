# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution(object):

    def helper(self, l1, part):
        s=l1[0]
        if s.find(part)!=-1:
            index= s.find(part)
            left_part = s[0:index]
            right_part = s[index+len(part):]
            s=left_part+right_part
            l1[0]=s
            self.helper(l1,part)
        else:
            return


    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        l1=[]
        l1.append(s)
        self.helper(l1, part)
        return l1[0]


# str1 = "abcd"
# print(str1.find("cd"))
# print(str1.find("cf"))