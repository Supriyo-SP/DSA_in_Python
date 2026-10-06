class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        validCountOpen = 0
        validCountClose = 0
        for i in range(len(s)):
            if s[i] == '(':
                validCountClose += 1
            elif s[i] == ')':
                if validCountClose > 0:
                    validCountClose -= 1
                else:
                    validCountOpen += 1
        return validCountClose + validCountOpen