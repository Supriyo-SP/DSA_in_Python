class Solution(object):
    def reversePrefix(self, word, ch):
        s=[]
        d=list(word)
        found = False
        for c in range(0,len(word)):
            s.append(d[c])
            if d[c]==ch:
                found=True
                break
        if not found:
            return word           
        s.reverse() 
        r=d[len(s):]       
        return "".join(s+r)
               
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        