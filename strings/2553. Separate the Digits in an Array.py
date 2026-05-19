class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = "".join(map(str, nums))
        return list(map(int, result))