from boards import *
from print_board import *
import time


# Look for next empty position that has not already been looked at 
def next_empty(puzzle, no_solution):
    for row in range(0, 9):
        for col in range(0, 9):
            if puzzle[row][col] == "*":
                if (row, col) not in no_solution:
                    return row, col
    return None, None


def single_position_row(puzzle, row, col, guess):
    for i in range (0, 9):
        if puzzle[row][i] == guess:     # guess already exists in row
            return False

    return True


def single_position_col(puzzle, row, col, guess):
    for i in range (0, 9):
        if puzzle[i][col] == guess:     # guess already exists in column
            return False
    
    return True


def single_position_group(puzzle, row, col, guess):
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:   # guess already exists in subgroup
                return False

    return True

################## Function not used #####################
def adjacent_col(puzzle, row, col, guess):
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    check_1 = False
    check_2 = False

    if col in [0, 3, 6]:
        adj1 = col+1
        adj2 = col+2
    elif col in [1, 4, 7]:
        adj1 = col+1
        adj2 = col-1
    else:
        adj1 = col-1
        adj2 = col-2

    for i in range (0, 9):
        if puzzle[i][adj1] == guess:     # guess already exists in adjacent column
            check_1 = True
        if puzzle[i][adj2] == guess:     # guess already exists in adjacent column
            check_2 = True

    if check_1 and check_2:
        return True
    else:
        return False

################## Function not used #####################
def adjacent_row(puzzle, row, col, guess):
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    check_1 = False
    check_2 = False

    if row in [0, 3, 6]:
        adj1 = row+1
        adj2 = row+2
    elif row in [1, 4, 7]:
        adj1 = row+1
        adj2 = row-1
    else:
        adj1 = row-1
        adj2 = row-2

    for i in range (0, 9):
        if puzzle[adj1][i] == guess:     # guess already exists in adjacent row
            check_1 = True
        if puzzle[adj2][i] == guess:     # guess already exists in adjacent row
            check_2 = True

    if check_1 and check_2:
        return True
    else:
        return False


################## Function not used #####################
# Secondary technique to choose between multiplate candidates
# Couldnt get the logic for this technique to work yet
def select_possible_candidate(puzzle, row_pos, col_pos, candidates):
    for guess in candidates:
        adj_col_result = adjacent_col(puzzle, row_pos, col_pos, guess)
        adj_row_result = adjacent_row(puzzle, row_pos, col_pos, guess)

        if adj_col_result and adj_row_result:   # this check isnt entirely correct
            puzzle[row_pos][col_pos] = guess
            return True
      
    return False


def human_solver(puzzle, row_pos, col_pos, guess):
    row_result = single_position_row(puzzle, row_pos, col_pos, guess)
    col_result = single_position_col(puzzle, row_pos, col_pos, guess)
    group_result = single_position_group(puzzle, row_pos, col_pos, guess)

    if row_result and col_result and group_result:
        return True
    else:
        return False


def human_solve_sudoku(puzzle):
    solved = False
    no_solution = []

    while solved == False:
        candidates = []
        row_pos, col_pos = next_empty(puzzle, no_solution)
        if row_pos is None and col_pos is None:     
            if not no_solution:                         # stop if puzzle is solved
                print("\nPuzzle solved")
                solved = True
                break
            else:
                no_solution = []
                row_pos, col_pos = next_empty(puzzle, no_solution)

        for guess in range(1, 10):
            if human_solver(puzzle, row_pos, col_pos, guess):
                candidates.append(guess)

        if len(candidates) == 1:
            puzzle[row_pos][col_pos] = candidates[0]    # single candidate, write to board
        else:
            # select between multiple candidates 
            # if no candidates selected then proceed

            # no current solution for position
            no_solution.append((row_pos, col_pos))   


if __name__ == '__main__':
    start_time = time.time()
    print(f"Board 0:")
    puzzle = board_4()
    print_board(puzzle)
    human_solve_sudoku(puzzle)
    print("\n")
    print_board(puzzle)
