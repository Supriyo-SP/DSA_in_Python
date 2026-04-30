class Solution(object):
    def reverseWords(self, s):
        word=s.split()
        word.reverse()
        r=' '.join(word)
        return r
        """
        :type s: str
        :rtype: str
        """
        