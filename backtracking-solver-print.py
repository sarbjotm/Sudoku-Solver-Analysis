from boards import *
from print_board import *
import time

# Replace row and col here to change if we solve via cols or rows. If rows in outer  
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


    # We want to check for three rows/cols (as each subsquare has 3 rows/cols) So we will go from col x to x+3 similar with rows
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

        puzzle[row_pos][col_pos] = '*' #Value reset so we backtrack

    
    return False


if __name__ == '__main__':
    print(f"Backtracking.........")
    start_time = time.time()
    puzzle = board_0()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 0: {time.time() - start_time}")
    
    current_time = time.time()
    puzzle = board_1()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 1: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_2()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 2: {time.time() - current_time}")


    current_time = time.time()
    puzzle = board_3()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 3: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_4()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 4: {time.time() - current_time}")

    print(f"TIME TAKEN TO SOLVE 5 BOARDS: {time.time() - start_time}")

    current_time = time.time()
    puzzle = board_5()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 5: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_6()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 6: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_7()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 7: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_8()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 8: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_9()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 9: {time.time() - current_time}")

    print(f"TIME TAKEN TO SOLVE 10 BOARDS: {time.time() - start_time}")

    current_time = time.time()
    puzzle = board_10()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 10: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_11()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 11: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_12()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print(puzzle)
    print(f"Time taken to solve Board 12: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_13()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 13: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_14()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 14: {time.time() - current_time}")

    print(f"TIME TAKEN TO SOLVE 15 BOARDS: {time.time() - start_time}")


    current_time = time.time()
    puzzle = board_15()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 15: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_16()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 16: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_17()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 17: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_18()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 18: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_19()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 19: {time.time() - current_time}")

    print(f"TIME TAKEN TO SOLVE 20 BOARDS: {time.time() - start_time}")



    current_time = time.time()
    puzzle = board_20()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 20: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_21()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 21: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_22()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 22: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_23()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 23: {time.time() - current_time}")

    current_time = time.time()
    puzzle = board_24()
    print_board(puzzle)
    print("\n")
    solve_sudoku(puzzle)
    print_board(puzzle)
    print(f"Time taken to solve Board 24: {time.time() - current_time}")

    print(f"TIME TAKEN TO SOLVE 25 BOARDS: {time.time() - start_time}")