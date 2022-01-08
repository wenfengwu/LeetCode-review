# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

class Solution:
    def fizzBuzz(self, n: int):
        answer = []
        i = 1
        while i <= n:
            if i%3 == 0 and i%5 ==0:
                answer.append("FizzBuzz")
            elif i%3 == 0:
                answer.append("Fizz")
            elif i%5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
            i += 1
        return answer