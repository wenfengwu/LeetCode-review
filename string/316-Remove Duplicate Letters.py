# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ## APPROACH : STACK ##
		## 100% Same Problem Leetcode 1081. Smallest Subsequence of Distinct Characters ##
		## LOGIC ##
		#	1. We add element to the stack
		#	2. IF we get bigger element, we just push on top
		#	3. ELSE we pop if and only if there are other occurances of same letter again in the string, otherwise we donot pop
		#	4. If an element is already in the stack, we donot push.
		## TIME COMPLEXICITY : O(N) ##
		## SPACE COMPLEXICITY : O(N) ##
	
		## EXAMPLE : "cdadabcc"	##
		## STACK TRACE ##
        # {'c': 7, 'd': 3, 'a': 4, 'b': 5}
        # ['c']
        # ['c', 'd']
        # ['a']
        # ['a', 'd']
        # ['a', 'd', 'b']
        # ['a', 'd', 'b', 'c']
        
        stack = []
        seen = set()
        last_occurance = {}
        for i in range(len(s)):
            last_occurance[ s[i] ] = i
        
        # print(last_occurance)
        
        for i, ch in enumerate(s):
            if( ch in seen ):
                continue
            else:
                # 3
                while( stack and stack[-1] > ch and last_occurance[stack[-1]] > i ):
                    removed_char = stack.pop()
                    seen.remove(removed_char)
                seen.add(ch)
                stack.append(ch)
            # print(stack)
        return ''.join(stack)