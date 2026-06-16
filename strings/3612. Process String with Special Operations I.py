class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        for ch in s:
            if ch == "#":
                result=result*2
            elif ch=="*":
                result=result[:-1] 
            elif ch == "%":
                result=result[::-1]
            else:
                result=result+ch
        return result                   

