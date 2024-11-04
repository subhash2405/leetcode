class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def check(x, y, num):
            for i in range(len(board)):
                if board[i][y] == num:
                    return False
            
            for j in range(len(board[0])):
                if board[x][j] == num:
                    return False
            a = x//3
            b = y//3  
            for i in range(a*3, a*3 + 3):
                for j in range(b*3, b*3+3):
                    if board[i][j] == num:
                        return False
            return True
        
        def Sudoku(board: List[List[str]]) -> bool:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        for c in "123456789":
                            if check(i, j, c):
                                board[i][j] = c
                                if Sudoku(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True
        
        return Sudoku(board)
            

