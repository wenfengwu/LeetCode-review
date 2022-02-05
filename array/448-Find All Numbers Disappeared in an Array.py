# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            #get the index
            j = abs(nums[i]) - 1
            #if this value of index has been change, continue
            if nums[j] < 0:
                continue
            else:
                #change it to negative number
                nums[j] = nums[j] * -1
        result = []
        for k in range(len(nums)):
            if nums[k] > 0:
                result.append(k+1)
        return result