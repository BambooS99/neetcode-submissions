class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const keys ={}
        for  (let i=0; i< nums.length;i++){
            if (keys[nums[i]]){
                return true;
            }
            keys[nums[i]]= true;
        }
        return false;

    }
}
