class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_seq=0
        second_seq=0
        for n in nums:
            temp = max(n+first_seq,second_seq)
            first_seq = second_seq
            second_seq = temp
        return second_seq

        