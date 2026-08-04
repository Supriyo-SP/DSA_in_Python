class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob(arr,start,end):
            if len(arr)==1:
                return arr[0]
            first_seq=0
            second_seq=0
            for n in range(start,end):
                temp = max(arr[n]+first_seq,second_seq)
                first_seq = second_seq
                second_seq = temp
            return second_seq 
        f= rob(nums,0,len(nums)-1)
        e= rob(nums,1,len(nums))
        return max(f,e)
