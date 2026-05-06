class Solution(object):
    def isSubsequence(self, s, t):
        if not s: return True
        sp=0
        for ch in t:
            if sp<len(s) and ch==s[sp]:
                sp+=1
        return sp==len(s)                     
                   
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        