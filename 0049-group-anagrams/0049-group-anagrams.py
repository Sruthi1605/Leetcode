from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
