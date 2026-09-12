from collections import defaultdict
class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        imap = defaultdict(list)
        for i, num in enumerate(nums):
            imap[num].append(i)
        count = 0
        for i in imap.values():
            if len(i) == 3:
                if i[1] - i[0] == i[2] - i[1]:
                    count+=1
        return count            
