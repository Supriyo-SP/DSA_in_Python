class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        h=(30 *hour)+(.5 * minutes)
        m=6 * minutes
        diff=abs(h-m)
        small_angle=min(diff,360-diff)
        return small_angle