class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        d=len(s)
        for i in range(0,d):
            rotate=s[i:] +s[:i]
            if rotate==goal:
                return True
        return False        
        