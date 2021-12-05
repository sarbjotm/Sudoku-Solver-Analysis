from boards import board_1, board_2, board_3, board_4
from print_board import print_board


def next_empty(puzzle):
    for row in range(0, 9):
        for col in range(0, 9):
            if puzzle[row][col] == "*":
                return row, col
    return None, None


def move_valid(puzzle, guess, row, col):
    row_values = puzzle[row]
    col_values = []
    for i in range(0, 9):
        col_values.append(puzzle[i][col])

    if guess in row_values or guess in col_values:
        return False 
    
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    #Row,Col values 
    # 0,0   0,0   0,0       0,3   0,3   0,3     0,6   0,6   0,6        
    # 0,0   0,0   0,0       0,3   0,3   0,3     0,6   0,6   0,6
    # 0,0   0,0   0,0       0,3   0,3   0,3     0,6   0,6   0,6

    # 3,0   3,0   3,0       3,3   3,3   3,3     3,6   3,6   3,6 
    # 3,0   3,0   3,0       3,3   3,3   3,3     3,6   3,6   3,6
    # 3,0   3,0   3,0       3,3   3,3   3,3     3,6   3,6   3,6

    # 6,0   6,0   6,0       6,3   6,3   6,3     6,6   6,6   6,6 
    # 6,0   6,0   6,0       6,3   6,3   6,3     6,6   6,6   6,6
    # 6.0   6,0   6,0       6,3   6,3   6,3     6,6   6,6   6,6



# Explanation For Loop 


# for r in range(row_start, row_start + 3):
#   for c in range(col_start, col_start + 3):
#     print(f"{r}{c}")
# This gives wrong inputs of 00 01 02 10 11 12 20 21 22 which does not follow our grid above



    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    
    return True


def solve_sudoku(puzzle):
    row_pos, col_pos = next_empty(puzzle)
    if row_pos is None and col_pos is None:
        return True

    for guess in range(1, 10):
        if move_valid(puzzle, guess, row_pos, col_pos):
            puzzle[row_pos][col_pos] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row_pos][col_pos] = '*'
    
    return False


if __name__ == '__main__':
    print(f"Board 1:")
    puzzle = board_1()
    print_board(puzzle)
    solve_sudoku(puzzle)
    print("\n \n")
    print_board(puzzle)
    print("\n \n") 
    
    print(f"Board 2:")
    puzzle = board_2()
    print_board(puzzle)
    solve_sudoku(puzzle)
    print("\n \n")
    print_board(puzzle)
    print("\n \n") 

    print(f"Board 3:")
    puzzle = board_3()
    print_board(puzzle)
    solve_sudoku(puzzle)
    print("\n \n")
    print_board(puzzle)
    print("\n \n") 

    print(f"Board 4:")
    puzzle = board_4()
    print_board(puzzle)
    solve_sudoku(puzzle)
    print("\n \n")
    print_board(puzzle)
    print("\n \n") 