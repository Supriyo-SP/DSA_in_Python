class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        window_sum = 0
        answer =float("inf")
        for i in range(len(nums)):
            window_sum += nums[i]
            while window_sum >= target:
                length = i - left +1
                answer = min(answer, length)
                window_sum -= nums[left]
                left +=1
        if answer == float('inf'): return 0 
        return answer
        