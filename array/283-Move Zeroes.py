# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0;
        right = 0;
        while right < len(nums):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left +=1
            right += 1
        return
                
            