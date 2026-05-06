class Solution(object):
    def detectCapitalUse(self, word):
        if word.islower():
            return True 
        if word.isupper():
            return True
        elif word.istitle():
            return True
        else:
            return False

          

        """
        :type word: str
        :rtype: bool
        """
        