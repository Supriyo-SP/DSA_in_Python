class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorted_text1 = "".join(sorted(s))
        sorted_text2 = "".join(sorted(t))
        return sorted_text1 ==  sorted_text2
        