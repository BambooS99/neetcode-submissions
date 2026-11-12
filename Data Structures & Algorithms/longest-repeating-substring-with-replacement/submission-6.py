class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = set(s)
        maxRes = 0

        for c in seen:
            count = 0 
            l = 0

            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                if (r-l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                maxRes = max(maxRes, r - l + 1)
        return maxRes