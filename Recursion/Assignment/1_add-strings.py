# https://leetcode.com/problems/add-strings/

class Solution(object):

    def helper(self, num1, p1, num2, p2, ans, carry=0):
        if p1 < 0 and p2 < 0:
            if carry != 0:
                ans.append(str(carry))
            return

        n1 = 0
        n2 = 0
        if p1 >= 0:
            n1 = int(num1[p1])
        if p2 >= 0:
            n2 = int(num2[p2])
        num = n1 + n2 + carry
        digit = num % 10
        carry = num // 10

        ans.append(str(digit))
        self.helper(num1, p1 - 1, num2, p2 - 1, ans, carry)

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = []
        self.helper(num1, len(num1) - 1, num2, len(num2) - 1, ans)
        return "".join(reversed(ans))