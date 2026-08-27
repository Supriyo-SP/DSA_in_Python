class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # str_set = list(set(strs))
        # output = []
        # i=0
        # for word in str_set:
        #     result = []
        #     for j in strs:
        #         if Counter(word) == Counter(j):
        #             result.append(j)
        #     if result not in output:
        #         output.append(result)
        # return output           
        anagram_map = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            anagram_map[key].append(word) 
        return list(anagram_map.values())       