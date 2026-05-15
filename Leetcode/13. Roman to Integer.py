class Solution(object):
    def romanToInt(self, s):
        letters={
        "I" :  1,
        "V" :  5,
        "X" :  10,
        "L" :  50,
        "C" :  100,
        "D" :  500,
        "M" :  1000
        }
        n=len(s)
        result=0
        for i in range(0,n):
            if i<n-1 and letters[s[i]]<letters[s[i+1]]:
                result-=letters[s[i]]
            else:
                result+=letters[s[i]] 
        return result           
        """
        :type s: str
        :rtype: int
        """
        