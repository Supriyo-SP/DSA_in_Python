class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ans= set(nums1) & set(nums2)
        if ans:
            return min(ans)
        else:
            return -1    

      