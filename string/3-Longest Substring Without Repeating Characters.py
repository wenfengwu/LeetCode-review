# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempDict = {}
        result = 0
        start = 0
        
        for index, value in enumerate(s):
            #if already exist in dictionary
            if value in tempDict and start <= tempDict[value]:
                #move the left pointer to next index
                start = tempDict[value] + 1
            else:
                #if not exist, that means no duplicate char, take the max length
                result = max(result, index - start + 1)
            
            #update the index of its value
            tempDict[value] = index
            
        return result
    