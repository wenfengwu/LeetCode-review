# Given an array of integers nums, sort the array in ascending order.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        leftArr = self.sortArray(nums[0:mid])
        rightArr = self.sortArray(nums[mid:])
        return self.helper(leftArr, rightArr)
    
    
    def helper(self, leftArr, rightArr):
        left = 0
        right = 0
        result = []
        while left < len(leftArr) and right < len(rightArr):
            if leftArr[left] < rightArr[right]:
                result.append(leftArr[left])
                left += 1
            else:
                result.append(rightArr[right])
                right += 1
                
        while left < len(leftArr):
            result.append(leftArr[left])
            left += 1
                
        while right < len(rightArr):
            result.append(rightArr[right])
            right += 1
        
        return result