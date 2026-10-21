class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        storedWater = 0
        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                storedWater += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                storedWater += rightMax - height[r]
        return storedWater

        

            

        
        
        
            






