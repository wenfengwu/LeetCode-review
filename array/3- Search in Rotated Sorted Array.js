// There is an integer array nums sorted in ascending order (with distinct values).

// Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

// Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

// You must write an algorithm with O(log n) runtime complexity.

 

// Example 1:

// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4
// Example 2:

// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1
// Example 3:

// Input: nums = [1], target = 0
// Output: -1
 

// Constraints:

// 1 <= nums.length <= 5000
// -104 <= nums[i] <= 104
// All values of nums are unique.
// nums is an ascending array that is possibly rotated.
// -104 <= target <= 104
// Accepted
// 1,218,503
// Submissions
// 3,286,908

//Use binary search, seperate to two part
// 1.find which part is sorted(only determine the start and end points)
// 2.if the target is not in right or left part, discard that part.

var search = function(nums, target) {
    let start = 0;
    let end = nums.length - 1;
    
    while(start <= end){
        let mid = Math.floor((start + end) / 2);
        
        //when found the target, return its index
        if(nums[mid] === target){
            return mid;
        }
        
        //if left side is sorted
        if(nums[mid] >= nums[start]){
            //if target is in left side, then discard right part, move the end point to index mid - 1
            if(nums[start] <= target && nums[mid] > target){
                end = mid - 1
            }
            //if target is in right side, then discard left part, move the start point to index mid + 1
            else{
                start = mid + 1;
            }
        }
        //if right side is sorted
        else{
            //if target is in right side, then discard left part, move the start point to index mid + 1
            if(target > nums[mid] && nums[end] >= target){
                start = mid + 1;
            }
            //if target is in left side, then discard right part, move the end point to index mid - 1
            else{
                end = mid - 1;
            }
        }
    }
    return -1
};