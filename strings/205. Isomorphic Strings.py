class Solution(object):
    def isIsomorphic(self, s, t):
        s_to_t={}
        t_to_s={}
        for i in range(len(s)):
            s_ch=s[i]
            t_ch=t[i]
            if s_ch in s_to_t:
                if s_to_t[s_ch]!=t_ch:
                    return False
            else:
                s_to_t[s_ch]=t_ch

            if t_ch in t_to_s:
                if t_to_s[t_ch]!=s_ch:
                    return False
            else:
                t_to_s[t_ch]=s_ch  
        return True          

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        