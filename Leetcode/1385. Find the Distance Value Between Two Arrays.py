class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0 
        for x in arr1:
            good = True 
            for y in arr2:
                if abs(x-y)<=d:
                    good = False
                    break
            if good:
                count += 1
        return count                 
