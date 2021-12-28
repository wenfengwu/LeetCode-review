// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

 

// Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Example 2:

// Input: nums = []
// Output: []
// Example 3:

// Input: nums = [0]
// Output: []
 

// Constraints:

// 0 <= nums.length <= 3000
// -105 <= nums[i] <= 105

//thinking pattern
// 1. sort the Array
// 2. terverse the Array, from 0 to length - 2(at least 3 nums)
// 3. if nums[i] === nums[i + 1], then neglect/ignore this i, move to num[i+2]
// 4. if i === 0 || nums[i] !== nums[i + 1], start = i + 1, end = nums.length - 1; check three sum if is equal to 0; if it is, push to the result array, then move start(++) and end(--) pointer, then check hile(start < end && nums[start] === nums[start-1]) ; while(start < end && nums[end] === nums[end+1]) to eliminate the duplicate;
// 5. if greater than 0; move end; end--; if lower than 0; move start, start ++;


var threeSum = function(nums) {
    const result = [];
    nums = nums.sort((a, b) => a-b);
    for(let i = 0; i < nums.length - 2; i++){
        //eliminate the duplicates
        if(i === 0 || nums[i] !== nums[i-1]){
            let start = i + 1;
            let end = nums.length - 1;
            while(start < end){
                if(nums[i] + nums[start] + nums[end] > 0){
                    end--;
                }
                else if(nums[i] + nums[start] + nums[end] < 0){
                    start++;
                }
                else{
                    let match = [nums[i], nums[start], nums[end]];
                    result.push(match);
                    start++;
                    end--;
                    //eliminate the duplicates [-2,0,0,2,2]
                    while(start < end && nums[start] === nums[start-1]){
                        start++;
                    }while(start < end && nums[end] === nums[end+1]){
                        end--;
                    }
                }
            }
        }
    }
    return result;
};