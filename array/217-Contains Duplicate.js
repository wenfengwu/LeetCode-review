// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

// Example 1:

// Input: nums = [1,2,3,1]
// Output: true
// Example 2:

// Input: nums = [1,2,3,4]
// Output: false
// Example 3:

// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true
 

// Constraints:

// 1 <= nums.length <= 105
// -109 <= nums[i] <= 109

var containsDuplicate = function(nums) {
    const tempObj = {};
    //use dictionary to check, hasOwnProperty
    for(let elem of nums){
        if(!tempObj.hasOwnProperty(elem)){
            tempObj[elem] = 1;
        }
        else{
            return true;
        }
    }
    return false;
};

//Python solution, using set
// class Solution:
//     def containsDuplicate(self, nums: List[int]) -> bool:
//         return len(set(nums)) != len(nums)

//Python solution, using dictionary
// class Solution:
//     def containsDuplicate(self, nums: List[int]) -> bool:
//         tempDict = {}
//         for index, value in enumerate(nums):
//             if value in tempDict:
//                 return True
//             tempDict[value] = index
//         return False