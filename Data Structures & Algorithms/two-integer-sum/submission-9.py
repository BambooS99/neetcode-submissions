class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {} #initialize our dictionary
        for i in range(len(nums)): #iterate through each number. 
            complement = target - nums[i] #smarter way to get the value pls explain???
            if complement in res:
                return [res[complement], i]
            res[nums[i]] = i # this will populate the array with our values