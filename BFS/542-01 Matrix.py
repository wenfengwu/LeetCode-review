# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # define row
        row = len(mat)
        
        # define col
        col = len(mat[0])
        
        # define the queue
        queue = deque()
        
        # firstly putting the 0 positions into the queue
		# note here we put all the 0 position into the queue, not only one 0.
		# this is not the same as the question number of islands 
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    
        # To create an empty set is the eye in this question        
        # set a visited set to record the visited position
        # why we choose a set, because it can cancel the repeated terms
        # for instance, in example 2, when we find neighbor 1 in the exactly middle position
        # we can find there are 3 "0" can find this middle 1, if we do not use a set
        # it will happen that we will put the middle position in the queue for 3 times
        # we can see the details later in the BFS
        # note: to create an empty set, we can only use set(), not {}, because {} is for
        # creating dictionary
        visited = set()
        # we let visited set firstly add all the coordinate of 0 elements
        visited.update(queue)
        
        # set a count to deal with the value of corresponding position later
        # when we traverse each level, we can deal with the output value for corresponding position
        # we can see the details later in BFS
        count = 0
        
        # BFS
        while queue:
            # take out the 1st element coordinate in the queue
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                # find the neighbor
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy

                    # skip the out border case
                    if xx < 0 or xx == row or yy < 0 or yy == col:
                        continue

                    # skip the visited position coordinate
                    if (xx, yy) in visited:
                        continue

                    # then the neigjbor will be only the position value with 1
                    # record such position coordinate, put them into the queue
                    queue.append((xx, yy))

                    # we put the coordinate of the neighbor into the visited set
                    visited.add((xx, yy))
                
                # update the cooresponding position value for (x, y)
                # here we split into 2 case
                if mat[x][y] == 0:
                    mat[x][y] = 0
                else:
                    mat[x][y] = mat[x][y] + count - 1
            
            # when each level traversal finishes, we count + 1 then out of the loop
            count += 1
            
        return mat