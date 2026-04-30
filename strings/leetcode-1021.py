class Solution(object):
    def removeOuterParentheses(self, s):
        res=""
        count=0
        for ch in s:
            if ch=='(':
                count+=1
                if count>1:
                    res+=ch
            else:
                count-=1
                if count>0:
                    res+=ch
        return res                
        """
        :type s: str
        :rtype: str
        """
        