class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l=len(cost)
        cost.sort()
        cost.reverse()
        total=0
        for i in range(0,l,3):
            total+=cost[i]
            if i+1<l:
                total+=cost[i+1]
        return total        



        