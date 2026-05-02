# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
str = "abcdabcbb"
m=0
for i in range(0,len(str)):
    s=set()
    for j in range(i,len(str)):
        if str[j] in s:
            break
        m=max(m,j-i+1)
        s.add(str[j])
print(m)   
# optimal     
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d=dict()
        left=0
        right=0
        m=0
        n=len(s)
        while right<n:
            if s[right] in d:
                left=max(left,d[s[right]]+1)
            m=max(m,right-left+1)
            d[s[right]]=right
            right+=1
        return m    

        """
        :type s: str
        :rtype: int
        """
        


    
