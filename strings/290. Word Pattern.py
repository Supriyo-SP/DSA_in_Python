class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word=s.split()
        if len(pattern)!= len(word):
            return False
        h={}
        seen=set()
        for i in range(len(pattern)):
            if pattern[i] in h:
                if h[pattern[i]]!=word[i]:
                    return False
            else:
                if word[i] in seen:
                    return False
                h[pattern[i]]=word[i]
                seen.add(word[i]) 
        return True           

        