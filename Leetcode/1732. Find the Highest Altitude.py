class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        hgain=[0]
        altitude=0
        for i in gain:
            altitude+=i
            hgain.append(altitude)
        return max(hgain)    
        