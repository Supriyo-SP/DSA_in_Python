class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r = "".join(char for char in s if char.isalnum())
        result=r.lower()
        # mid = len(result) // 2
        # if len(result) % 2 ==0:
        #     first_half = result[:mid]
        #     second_half = result[mid:]
        #     return first_half == second_half[::-1]
        # else:
        #     first_half = result[:mid]
        #     second_half = result[mid+1:]
        #     return first_half == second_half[::-1]
        return result == result[::-1]
        