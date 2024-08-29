import numpy as np

def print_board(board):
    """ Print the Sudoku board in a formatted way """
    for row in board:
        print(' '.join(str(num) if num != 0 else '.' for num in row))

def find_empty_location(board):
    """ Find an empty location in the board (returning row, col) """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board, row, col, num):
    """ Check if placing num at board[row][col] is valid """
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    """ Solve the Sudoku board using backtracking """
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty
    
    for num in range(1, 10):  # Try numbers 1 through 9
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # Backtrack

    return False

def get_sudoku_input():
    """ Get Sudoku puzzle from user input """
    print("Enter Sudoku puzzle (use 0 for empty cells):")
    board = []
    for i in range(9):
        row = list(map(int, input().strip().split()))
        if len(row) != 9:
            raise ValueError("Each row must have exactly 9 numbers.")
        board.append(row)
    return board

if __name__ == "__main__":
    board = get_sudoku_input()
    
    print("Original Sudoku:")
    print_board(board)
    
    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("No solution exists.")
