class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]
        hashmap = {}
        for char in s:
            hashmap[char]=hashmap.get(char, 0)+1
        sorted_char = sorted(hashmap.items(), key= itemgetter(1), reverse=True)
        for char , freq in sorted_char:
            result.append(char * freq)
        return "".join(result) 
        