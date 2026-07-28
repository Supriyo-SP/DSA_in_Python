class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq=dict()
        for char in s:
            freq[char]=freq.get(char,0)+1
        odd=''
        for k,v in freq.items():
            if v % 2 !=0:
                odd=k
        left_half=[]
        for k,v in freq.items():
            left_half.append(k * (v // 2))
        left_half.sort()    
        left_str = "".join(left_half)

        palindrome = left_str + odd + left_str[::-1]

        return palindrome
        





        