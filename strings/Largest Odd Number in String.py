class Solution(object):
    def largestOddNumber(self, num):
        n=int(num)
        temp=n
        res=0

        while temp>0:
            if temp%2!=0:
                res=temp
                break
            temp=temp//10
        if res>=1:
            return str(res)
        else:
            return ""            
        """
        :type num: str
        :rtype: str
        """
#optimal
        