// Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

// It is guaranteed that the answer will fit in a 32-bit integer.

// A subarray is a contiguous subsequence of the array.

//simple solution, when the negative numbers is even, these is a biggest mul
//but we do not know which side negative number is bigger, so we need go two ways to confirm the biggest mul
//when nums[i] is 0, max reset to 1, then keep checking

var maxProduct = function(nums) {
    if(nums.length === 0){
        return 0;
    }
   let max = 1;
   let result = nums[0];
   for(let i = 0; i < nums.length; i++){
       max *= nums[i];
       result = Math.max(result, max);
       if(nums[i] === 0){
           max = 1;
       }
   }
   
   max = 1;
   for(let i = nums.length -1; i>=0; i--){
       max*=nums[i];
       result = Math.max(result,max);
       if(nums[i] === 0){
           max = 1
       }
   }
   return result;
};

//Dynamic programming
//compare three vars, nums[i], dpMax * nums[i], dpMin * nums[i]
var maxProduct = function(nums) {
    let dpMax = nums[0];
    let dpMin = nums[0];
    let result = nums[0];

    for(let i = 1; i < nums.length; i++){
        const tempMax = nums[i] * dpMax;
        dpMax = Math.max(nums[i], dpMin * nums[i], tempMax);
        dpMin = Math.min(nums[i], dpMin * nums[i], tempMax);
        result = Math.max(result, dpMax);
    }

    return result;
}