# https://leetcode.com/problems/find-and-replace-pattern/

class Solution(object):

    def create_update_pattern(self, pattern):
        mapping={}
        start='a'

        normalised_str = ''

        for ch in pattern:
            if ch!=' ' and ch not in mapping:
                mapping[ch] = start
                start=chr(ord(start)+1)


        for ch in pattern:
            # print(ch)
            # print(mapping)
            normalised_str+=mapping[ch]

        return normalised_str


    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        normalised_pattern = self.create_update_pattern(pattern)
        ans=[]

        for word in words:
            normalised_word = self.create_update_pattern(word)
            if normalised_word==normalised_pattern:
                ans.append(word)

        return ans

words = ["a","b","c"]
pattern = "a"
print(Solution().findAndReplacePattern(words, pattern))