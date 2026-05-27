class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        count=0
        char_set=list(set(word))
        for ch in char_set:
            if ch.islower():
                if ch.upper() in char_set:
                     last_lower_idx = word.rfind(ch)
                     first_upper_idx = word.find(ch.upper())
                     if last_lower_idx < first_upper_idx:
                        count += 1    
        return count          
        