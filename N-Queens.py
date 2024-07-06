# Time Complexity :
# O(n!)       n  = No. of Queens

# Space Complexity :  
# O(n**2)       n = size(dim of n*n grid) we create to store the placements of queen

# Approach:
# For-loop based Backtracking
# Recursion : 
# Start recursive call at 0th row, and for each row, check whether it is safe to place the queen at the column 
# under consideration. If so, generate another recursive call with row+1, to place another queen, and so on.
# Backtrack:
# Undo the placement of queen if it was "not safe" to put the queen at any of the cols, for given row.
# Base case: Upon hitting the end row, create a combination list, to encode the string as per 
# the problem statement and given configuration of queen placement.


class Solution(object):
    def __init__(self):
        self.grid = []
        self.result = []
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n==0:
            return []
        
        #initiate grid
        self.grid = [[0 for i in range(n)] for j in range(n)]
        #recurse
        self.recurseNQueens(0)
        return self.result


    def recurseNQueens(self, row):
        #base
        if row == len(self.grid): #this means you placed nth queen at nth row
            combination = []
            for row in range(len(self.grid)):
                currStr = []
                for col in range(len(self.grid)):
                    if self.grid[row][col] == 1:
                        currStr.append("Q")
                    else:
                        currStr.append(".")
                combination.append("".join(currStr))
            self.result.append(combination)
            return



        #logic
        # 1. for loop based recursion
        for col in range(len(self.grid)):
            # check if the placement of grid is safe at this location
            if self.isSafe(row, col):
                # action
                self.grid[row][col] = 1

                # recurse
                self.recurseNQueens(row+1)

                # backtrack
                self.grid[row][col] = 0   #(Undo placement of the queen)
    

    def isSafe(self, i, j):
        # check upward
        for row in range(i):
            if self.grid[row][j] == 1:
                return False

        # check diagonal up-left
        row = i 
        col = j
        while(row>=0 and col>=0):
            if self.grid[row][col] == 1:
                return False
            row -= 1
            col -= 1

        # check diagonal up-right
        row = i 
        col = j
        while(row>=0 and col<len(self.grid)):
            if self.grid[row][col] == 1:
                return False
            row -= 1
            col += 1

        return True