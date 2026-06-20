class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la=len(a)-1
        lb=len(b)-1
        resulta=0
        resultb=0
        for i in a:
            d=int(i)
            resulta+=(2 ** la) * d
            la-=1
        for j in b:
            d=int(j)
            resultb+=(2 ** lb) * d 
            lb-=1
        result=resulta+resultb
        return bin(result)[2:]       

        