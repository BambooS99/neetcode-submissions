from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            key = tuple(sorted(s))
            res.setdefault(key, []).append(s)
        
        return list(res.values())