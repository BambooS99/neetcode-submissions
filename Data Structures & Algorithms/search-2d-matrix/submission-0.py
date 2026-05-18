class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = set()

        for i in matrix:
            for j in i:
                nums.add(j)
        
        if target in nums:
            return True
        return False