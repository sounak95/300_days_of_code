# https://leetcode.com/problems/add-strings/
'''
addStrings("123", "89")
└── helper("123", 2, "89", 1, [])
    ├── helper("123", 1, "89", 0, ["2"], carry=1)
    │   ├── helper("123", 0, "89", -1, ["2", "1"], carry=2)
    │   │   ├── helper("123", -1, "89", -1, ["2", "1", "2"], carry=0)
    │   │   │   └── (base case: p1 < 0 and p2 < 0, no carry, recursion ends)
    │   │   └── (p2 out of bounds, p1 moves to -1)
    │   └── (p2 out of bounds, p1 moves to 0)
    └── (p2 moves to 0, p1 moves to 1)

Time complexity: o(n).  max(len(num1),len(num2)), which we’ll denote as n
Space Complexity: o(n)

'''


class Solution(object):

    # Recursive helper function to perform addition
    def helper(self, num1, p1, num2, p2, ans, carry=0):
        # Base case: if both pointers are less than 0 and there's no carry, end the recursion
        if p1 < 0 and p2 < 0:
            # If there's a carry left, append it to the answer
            if carry != 0:
                ans.append(str(carry))
            return

        # Initialize digits to add as 0
        n1 = 0
        n2 = 0
        # If pointers are within bounds of the strings, get the integer values of the digits
        if p1 >= 0:
            n1 = int(num1[p1])  # Get the current digit from num1
        if p2 >= 0:
            n2 = int(num2[p2])  # Get the current digit from num2

        # Perform the addition with the carry from the previous iteration
        num = n1 + n2 + carry

        # Calculate the new digit to add to the result and the new carry
        digit = num % 10
        carry = num // 10

        # Append the calculated digit to the answer list
        ans.append(str(digit))
        # Recursive call, moving to the next pair of digits (moving leftwards)
        self.helper(num1, p1 - 1, num2, p2 - 1, ans, carry)

    # Main function to add two strings
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Initialize an empty list to store the result digits
        ans = []
        # Call the helper function with pointers set to the end of each string
        self.helper(num1, len(num1) - 1, num2, len(num2) - 1, ans)
        # Since digits were added in reverse order, reverse the list and join to get the result string
        return "".join(reversed(ans))
