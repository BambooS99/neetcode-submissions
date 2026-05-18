# strs = ["bat","bag","bank","band"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        #bat

        for s in strs[1:]:
            #["bag","bank","band"]
            while not s.startswith(prefix):
                #while bag, bank, band doesnt start with bat
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

