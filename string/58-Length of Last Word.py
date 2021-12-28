# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

# Using flase and counter to counter last length of word, until i hit space after hitting any letter
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        counter = 0
        for i in range(len(s)):
            if s[len(s) - 1 -i] == " ":
                if flag == True:
                    return counter
                continue
            flag = True
            counter += 1
        return counter



# one line solution using built in method:
# strip(): cancel out multiple space if no params
# split(): split a string into a array on each space
# pop(-1): pop the last index element
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split().pop(-1))