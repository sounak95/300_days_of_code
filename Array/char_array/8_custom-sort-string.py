# https://leetcode.com/problems/custom-sort-string/submissions/


class Solution:
    # Static variable to store the order string
    str = ""

    # Static method as a custom comparator
    @staticmethod
    def compare(char):
        # This will return the position of the character in str string
        return Solution.str.find(char)

    def customSortString(self, order: str, s: str) -> str:
        # Set the order string in the static variable
        Solution.str = order
        # Sort the string s using the custom comparator
        sorted_s = sorted(s, key=Solution.compare)
        # Convert the sorted list back to a string
        return "".join(sorted_s)

# Example usage:
# order = "cba", s = "abcd"
# Output: "cbad"
print(Solution().customSortString("cba", "abcd"))
