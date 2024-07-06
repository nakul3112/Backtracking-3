# Time Complexity:
# O(M*N*4*L) , M*N are board dimensions, 4*L comes from the fact that we do recursive search in 4 directions for each char in the word

# Space Complexity:  
# O(L), L= lenth of word      

# Approach: 
# DFS, Bactracking based approach.

class Solution(object):
    def __init__(self):
        self.dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        self.rows = 0
        self.cols = 0
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or len(board) == 0:
            return False

        self.rows = len(board)
        self.cols = len(board[0])

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if(self.backTrack(board, word, 0, row, col)):
                        return True
        return False

    def backTrack(self, board, word, index, row, col):
        # base
        if index == len(word):
            return True
        
        # check bounds
        if row<0 or row==self.rows or col<0 or col==self.cols or board[row][col]=="#":
            return False


        # logic
        if board[row][col] == word[index]:
            # action
            orig = board[row][col]
            board[row][col] = '#'
            # search in 4 dierections
            for dir in self.dirs:
                nr = row+dir[0]
                nc = col+dir[1]
                if self.backTrack(board,word, index+1, nr, nc):
                    return True
            # backTrack
            board[row][col] = orig
        
        return False