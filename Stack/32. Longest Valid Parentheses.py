class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack =[-1]
        mlen = 0
        for i,char in enumerate(s):
            if char =='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mlen = max(mlen,i-stack[-1])
        return mlen