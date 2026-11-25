class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted([(p,s) for p,s in zip(position, speed) ])
        res = []

        for p,s in pair[::-1]:
            res.append((target-p)/s)
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()
        return len(res)