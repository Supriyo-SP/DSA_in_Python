class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k= len(nums) - k
        
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        while k > 0:
            res = heapq.heappop(heap)
            k -=1
        return -res

#not the optimal solution