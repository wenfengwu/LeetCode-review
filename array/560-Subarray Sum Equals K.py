# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #sum of subarray(i,j) = prefixSum[j] - prefixSum[i-1]
        #find how many pairs of <i,j>
        #where i < j, prefixSum[j] - prefixSum[i] == k?
        #so, for each j: how many i < j satisfies prefixSum[i] = prefixSum[j] - k
        #Using a dictionary to mark:
        #key - prefixSum value
        #value - numbers of occurrence of the prefixSum value
        
        result = 0
        curSum = 0
        prefixSum = {0 : 1}
        
        for n in nums:
            curSum += n
            diff = curSum - k
            
            result += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        
        return result