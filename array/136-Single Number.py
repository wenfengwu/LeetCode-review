# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


# get(key, d): return the value of the key, If the key does not exist, return d(defaults to None)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tempDic = {};
        for num in nums:
            tempDic[num] = tempDic.get(num, 0) + 1
        for key,val in tempDic.items():
            if val == 1:
                return key

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)

