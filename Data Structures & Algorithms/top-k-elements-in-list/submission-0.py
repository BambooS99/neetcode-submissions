from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            res.setdefault(n, []).append(n)

        def freq(x: int) -> int:
            return len(res[x])

        ans = []
        while k > 0:
            best_key = max(res, key = freq)
            ans.append(best_key)
            del res[best_key]
            k -= 1
        return ans
        