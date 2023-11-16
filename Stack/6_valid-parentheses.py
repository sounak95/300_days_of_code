# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                st.append(ch)
            elif len(st)!=0:
                if ch==')' and st[-1]=='(':
                    st.pop()
                elif ch=='}' and st[-1]=='{':
                    st.pop()
                elif ch==']' and st[-1]=='[':
                    st.pop()
                else:
                    return False
            else:
                return False
        if len(st)!=0:
            return False
        return True

print(Solution().isValid("()"))