# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left , right = 0, n-1
        top, bottom = 0, n-1
        number = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                matrix[top][i] = number
                number+=1
            top += 1
            
            for j in range(top, bottom+1):
                matrix[j][right] = number
                number+=1
            right-=1
                
            for i in range(right, left-1, -1):
                matrix[bottom][i] = number
                number+=1
            bottom -= 1
            
            for j in range(bottom, top-1, -1):
                matrix[j][left] = number
                number+=1
            left += 1
            
        return matrix