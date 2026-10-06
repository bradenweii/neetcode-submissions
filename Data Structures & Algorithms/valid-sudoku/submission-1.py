class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        
        for i in range(0,row):
            for j in range(0,col):
                seen = set()
                if board[0][j] != "." and seen.contains(board[0][j]):
                    return False
                seen.add(board[0][j])
        for i in range(0,row):
            for j in range(0,col):
                seen = set()
                if board[i][0] != "." and seen.contains(board[i][0]):
                    return False
                seen.add(board[i][0])
        for i in range(0,3):
            for j in range(0,3):
                seen = set()
                if seen.contains(board[i][j]):
                    return False
                seen.add(board[i][j])
        for i in range(3,6):
            for j in range(6,9):

                seen = set()
                if seen.contains(board[i][j]):
                    return False
                seen.add(board[i][j])
        for i in range(6,9):
            for j in range(6,9):
                seen = set()
                if seen.contains(board[i][j]):
                    return False
                seen.add(board[i][j])

        