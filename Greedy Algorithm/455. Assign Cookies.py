class Solution(object):
    def findContentChildren(self, g, s):
        left=right=0
        count=0
        g.sort()
        s.sort()
        n=len(g)
        m=len(s)
        while left<n and right<m:
            if g[left]<=s[right]:
                count+=1
                left+=1
            right+=1
        return count        

        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        