class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        output = []
        start,curr,end = nums[0], nums[0], None
        for n in nums[1:]:
            curr += 1
            if n == curr:
                end = n
            else:
                if end == None:
                    output.append(str(start))
                else:   
                    output.append(str(start)+"->"+str(end))
                start = n
                curr = n
                end = None
        if not end:
            output.append(str(start))
        else:
            output.append(str(start)+"->"+str(end))
        return output


                
        