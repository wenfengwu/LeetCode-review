# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104

# time complexity(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # generate a dp array
        dp = [1] * len(nums)
        # max subsequence
        res = 1
        # traverse the nums
        for i in range(len(nums)):
            for j in range(i):
                # if the current pointer i greater than the prevous pointer j, then take max length of dp[i] and dp[j] + 1
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            # find the max subsequence
            res = max(res, dp[i])
        
        return res


# time complexity(nlongn)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        dp = []
        for x in nums:
            # return the insection index on nums
            i = bisect_left(dp,x)
            if i == len(dp):
                dp.append(x)
            else:
                dp[i] = x
        print(dp)
        return len(dp)