class Solution:
    def trap(self, height: List[int]) -> int:
        l,r,res = 0, len(height)-1, 0
        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(height[l], maxLeft)
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(height[r], maxRight)
                res += maxRight - height[r]
        return res