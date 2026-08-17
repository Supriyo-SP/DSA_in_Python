class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        l = len(cardPoints)
        if l == k:
            return sum(cardPoints)
        left_sum, right_sum = 0,0
        for i in range(0,k):
            left_sum += cardPoints[i] 
        maximum = left_sum
        right_idx = l-1
        for i in range(k-1,-1,-1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_idx]
            maximum = max(maximum,left_sum+right_sum)
            right_idx -= 1
        return maximum