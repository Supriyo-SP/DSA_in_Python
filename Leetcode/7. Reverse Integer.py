class Solution(object):
    def reverse(self, x):
        
        """
        :type x: int
        :rtype: int
        """
        is_neg=False
        if x<0:
            is_neg=True
        num=abs(x)
        answer=0
        while num>0:
            last_digit=num%10
            answer=(answer*10)+last_digit
            num//=10
        if answer <-(2**31) or answer>((2**31)+1):
            return 0
        return -answer if is_neg else answer        