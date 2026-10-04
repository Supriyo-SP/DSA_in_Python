class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftmin, leftmax = 0, 0
        for char in s:
            if char == "(":
                leftmin, leftmax = leftmin + 1, leftmax + 1
            elif char == ")":
                leftmin, leftmax = leftmin - 1, leftmax - 1  
            else:
                leftmin, leftmax = leftmin - 1, leftmax + 1
            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0
        return leftmin == 0                
        