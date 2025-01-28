# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
'''
removeOccurrences("daabcbaabcbc", "abc")
|
+-- helper(["daabcbaabcbc"], "abc")
     |
     +-- s = "daabcbaabcbc"
     |   s.find("abc") = 2
     |   s = "da" + "baabcbc"
     |
     +-- helper(["dabaabcbc"], "abc")
          |
          +-- s = "dabaabcbc"
          |   s.find("abc") = 4
          |   s = "daba" + "bc"
          |
          +-- helper(["dababc"], "abc")
               |
               +-- s = "dababc"
               |   s.find("abc") = 3
               |   s = "dab" + ""
               |
               +-- helper(["dab"], "abc")
                    |
                    +-- s = "dab"
                    |   s.find("abc") = -1 (not found)
                    |
                    +-- (Base case reached, return)

'''


class Solution(object):
    # Helper function to recursively remove 'part' from 's'
    def helper(self, l1, part):
        # Retrieve the current string from the list
        s = l1[0]

        # Check if 'part' is in the string
        if s.find(part) != -1:
            index = s.find(part)  # Find the index where 'part' starts

            # Divide the string into two parts: before 'part' and after 'part'
            left_part = s[0:
                          index]  # The left part of the string, before 'part'
            right_part = s[
                index +
                len(part):]  # The right part of the string, after 'part'

            # Concatenate the left and right parts, excluding 'part'
            s = left_part + right_part

            # Update the list with the new string
            l1[0] = s

            # Recursively call the helper to remove the next occurrence of 'part'
            self.helper(l1, part)
        else:
            # If 'part' is not found in the string, return as the base case is reached
            return

    # Main function to remove all occurrences of 'part' from 's'
    def removeOccurrences(self, s, part):
        l1 = []  # Create a list to hold the string, to pass by reference
        l1.append(s)  # Add the initial string to the list
        self.helper(l1,
                    part)  # Call the helper function with the list and 'part'
        return l1[0]  # Return the modified string


# str1 = "abcd"
# print(str1.find("cd"))
# print(str1.find("cf"))
