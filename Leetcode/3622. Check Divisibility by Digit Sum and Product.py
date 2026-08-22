class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digit_sum = 0
        digit_pro = 1
        digit = 0
        copy = n
        while n > 0:
            digit = n%10
            digit_sum += digit
            digit_pro *= digit
            total = digit_sum+digit_pro 
            n //= 10
        if copy % total == 0:
            return True
        else:
            return False
        