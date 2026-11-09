class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we will track our area which is min heights x r-l
        #we will iterate each bar and check each one for our max

        maxArea = 0
        l = 0
        r = len(heights)-1

        while l < r:
            area = (r-l) * min(heights[r], heights[l])

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            maxArea = max(area, maxArea)
        return maxArea