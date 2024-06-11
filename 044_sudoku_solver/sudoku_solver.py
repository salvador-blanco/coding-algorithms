# https://leetcode.com/problems/sudoku-solver/description/

from typing import List

class Solution:
    def __init__(self):
         self._numbers = [str(n) for n in range(1, 10)] 
    def solveSudoku(self, board: List[List[str]], board_size = 9, index = 0) -> None:
        
        x, y = index%9, int(index/9)
        while y <9 and board[y][x] != "." :
            x, y = index%9, int(index/9)
            index += 1

        if y == 9:
            return True
        
        if board[y][x] == ".":
            board_row = board[y]
            board_colum = [board[y][x] for y in range(0,9)]
            sector = self.get_sector(x,y, board)
            for placement_number in self._numbers:
                if (placement_number not in board_row) and (placement_number not in board_colum) and (placement_number not in sector):
                        board[y][x] = placement_number
                        if self.solveSudoku(board, board_size, index):
                            return board
            board[y][x] = "." 
            return False
        return board
    
    def get_sector(self, x, y, board):
        sector = []
        for y_board in range(int(y/3)*3, int(y/3)*3 +3):
            for x_board in range(int(x/3)*3, int(x/3)*3 +3):
                sector.append(board[y_board][x_board])        
        return sector
    
def main():
    tester = Solution()

    # Example 1:
    board = get_board_one()
    print_sudoku_board(board)
    board = tester.solveSudoku(board)
    print_sudoku_board(board)
    
    #Expected output# : [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
def print_sudoku_board(board, n = 9):

    for y in range(n):
        if not y%3:
            print(" - "*10)
        for x in range(n):
            if not x%3:
                print("|", end = "")
            character = board[y][x].replace(".", " ")
            print(f" {character} ", end = "")
        print("|", end = "")
        print()
    print(" - "*10)

def get_board_one():
        return [["5","3",".", ".","7",".", ".",".","."],
             ["6",".",".", "1","9","5", ".",".","."],
             [".","9","8", ".",".",".", ".","6","."],

             ["8",".",".", ".","6",".", ".",".","3"],
             ["4",".",".", "8",".","3", ".",".","1"],
             ["7",".",".", ".","2",".", ".",".","6"],
             
             [".","6",".", ".",".",".", "2","8","."],
             [".",".",".", "4","1","9", ".",".","5"],
             [".",".",".", ".","8",".", ".","7","9"]]

if __name__ == "__main__":
    main()