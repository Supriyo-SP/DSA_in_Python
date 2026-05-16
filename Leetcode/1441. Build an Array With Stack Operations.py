class Solution(object):
    def buildArray(self, target, n):
        s=[]
        r=[]
        index=0
        for i in range(1,n+1):
            if index==len(target):
                break
            s.append(i)
            r.append("Push")
            if i==target[index]:
                index+=1
            else: 
                r.append("Pop")
        return r            
            
                   
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        