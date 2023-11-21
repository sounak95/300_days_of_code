# https://leetcode.com/problems/decode-the-message/

class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """

        # create mapping
        mapping={}
        start='a'

        for ch in key:
            if ch!=' ' and ch not in mapping:
                mapping[ch] = start
                start= chr(ord(start)+1)

        # decode string
        decoded_str = ''
        for ch in message:
            if ch==' ':
                decoded_str +=' '
            else:
                dec_ch = mapping[ch]
                decoded_str+=dec_ch

        return decoded_str


