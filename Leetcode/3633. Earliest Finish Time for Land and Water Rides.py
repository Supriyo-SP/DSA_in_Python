class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        min_time = float('inf')
        n = len(landStartTime)
        m = len(waterStartTime)
        for i in range(n):
            for j in range(m):
                landf=landStartTime[i]+landDuration[i]
                water=max(landf,waterStartTime[j])
                f1=water+waterDuration[j]
                waterf=waterStartTime[j]+waterDuration[j]
                land=max(waterf,landStartTime[i])
                f2=land+landDuration[i]
                min_time=min(min_time,f1,f2)
        return min_time        
