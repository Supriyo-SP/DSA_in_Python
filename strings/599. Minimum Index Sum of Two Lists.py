class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        m=float('inf')
        li=[]
        for x in list1:
            if x in list2:
                f=list1.index(x)+list2.index(x)
                
                if f<m:
                    m=f
                    li=[x]
                elif f==m:
                    li.append(x)    
                    
        return li             
        