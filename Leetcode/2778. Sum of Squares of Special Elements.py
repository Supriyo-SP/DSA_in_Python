class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = 0
        for i in range(n):
            j = i + 1
            if (n % j) == 0:
                sum += (nums[i] ** 2)
        return sum
        