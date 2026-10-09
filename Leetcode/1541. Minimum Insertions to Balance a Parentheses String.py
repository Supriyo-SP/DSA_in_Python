class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        insert, need, i = 0, 0, 0
        while i < len(s):
            if s[i] == '(':
                need += 2
                if need % 2 != 0:
                    insert += 1
                    need -= 1
            else:
                if i + 1 <len(s) and s[i+1] == ')':
                    i += 1
                else:
                    insert += 1
                if need > 0:
                    need -= 2
                else:
                    insert += 1
            i += 1
        return need +insert            


        