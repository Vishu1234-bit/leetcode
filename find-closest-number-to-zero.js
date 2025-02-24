/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function(nums) {
    let minDiff = Infinity
    let closestNum = 0
    for(let i=0;i<nums.length;i++){
       let absNum = Math.abs(nums[i])
       if((absNum===minDiff && closestNum<nums[i])||
       absNum<minDiff ){
        minDiff = Math.min(Math.abs(nums[i]-0))
        closestNum = nums[i]
       }
    }
    return closestNum;
};
