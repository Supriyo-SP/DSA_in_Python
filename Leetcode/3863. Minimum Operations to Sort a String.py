class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "".join(sorted(s)):
            return 0
        if len(s) == 2:
            return -1
        maxi = max(s)
        mini = min(s)
        if s[0]==mini or s[-1] == maxi:
            return 1
        if s[0]== maxi and s[-1] == mini:
            if s.count(s[0]) == 1 and s.count(s[-1]) == 1:
                return 3
        return 2