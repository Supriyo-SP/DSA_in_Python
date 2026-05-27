class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        ls=[]
        count=0
        char_set = set(word)
        for ch in char_set:
            if ch.islower() and ch.upper() in char_set:
                count+=1 
        return count                        