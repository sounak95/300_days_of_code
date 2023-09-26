# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        index = 0
        while (index < len(s)):
            if len(ans) - 1 >= 0 and ans[len(ans) - 1] == s[index]:
                ans.pop()
            else:
                ans.append(s[index])
            index += 1

        return "".join(ans)

