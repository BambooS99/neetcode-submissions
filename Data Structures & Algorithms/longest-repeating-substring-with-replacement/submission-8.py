class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we will count the length of the characters and the length of non targetted characters.\
        #if non targetted exceed k, we can assume the max has been reached and adjust our window to the right

        values = set(s)
        res = 0

        for c in values:
            count = 0
            l = 0
            
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                if (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
            
        return res
                
                        



