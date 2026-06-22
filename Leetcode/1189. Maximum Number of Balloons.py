class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        h={
            'b':0,
            'a':0,
            'l':0,
            'o':0,
            'n':0
        }
        for ch in text:
            if ch in h:
                h[ch]+=1
        h['l']//=2  
        h['o']//=2  
        return min(h.values())    
        