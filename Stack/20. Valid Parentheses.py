class Solution(object):
    def isValid(self, s):
        res=0
        stack= []
        for ch in s:
            if ch=='(' or ch =='{' or ch=='[':
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                char=stack.pop()
                if ((char=='(' and ch==')') or (char=='{' and ch=='}') or (char=='[' and ch==']')):

                     continue 
                else:
                    return False
        return len(stack)==0                        
                

                
        """
        :type s: str
        :rtype: bool
        """
        