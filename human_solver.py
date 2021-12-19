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

def determine_occupied(row, col):
    vertical_occupied = []
    horizontal_occupied = []

    col_adj1, col_adj2, row_adj1, row_adj2 = find_adjacent(row, col)

    if puzzle[row_adj1][col] != '*':
        vertical_occupied.append(True)
    else:
        vertical_occupied.append(False)

    if puzzle[row_adj2][col] != '*':
        vertical_occupied.append(True)
    else:
        vertical_occupied.append(False)

    if puzzle[row][col_adj1] != '*': 
        horizontal_occupied.append(True) 
    else:
        horizontal_occupied.append(False) 

    if puzzle[row][col_adj2] != '*':
        horizontal_occupied.append(True) 
    else:
        horizontal_occupied.append(False) 

    return vertical_occupied, horizontal_occupied


def find_adjacent(row, col):
    if col in [0, 3, 6]:                # curr # adj1 # adj2
        col_adj1 = col+1                
        col_adj2 = col+2                
    elif col in [1, 4, 7]:              # adj1 # curr # adj2
        col_adj1 = col-1
        col_adj2 = col+1
    else:                               # adj1 # adj2 # curr
        col_adj1 = col-2
        col_adj2 = col-1

    if row in [0, 3, 6]:                # curr
        row_adj1 = row+1                # adj1
        row_adj2 = row+2                # adj2

    elif row in [1, 4, 7]:              # adj1
        row_adj1 = row-1                # curr
        row_adj2 = row+1                # adj2
        
    else:                               # adj1
        row_adj1 = row-2                # adj2
        row_adj2 = row-1                # curr

    return col_adj1, col_adj2, row_adj1, row_adj2

def adjacent_col(puzzle, row, col, guess):
    result = []
    check_1 = False
    check_2 = False

    col_adj1, col_adj2, row_adj1, row_adj2 = find_adjacent(row, col)

    for i in range (0, 9):
        if puzzle[i][col_adj1] == guess:     # guess already exists in adjacent column
            check_1 = True
        if puzzle[i][col_adj2] == guess:     # guess already exists in adjacent column
            check_2 = True

    result.append(check_1)
    result.append(check_2)
    return result


def adjacent_row(puzzle, row, col, guess):
    result = []
    check_1 = False
    check_2 = False

    col_adj1, col_adj2, row_adj1, row_adj2 = find_adjacent(row, col)

    for i in range (0, 9):
        if puzzle[row_adj1][i] == guess:     # guess already exists in adjacent row
            check_1 = True
        if puzzle[row_adj2][i] == guess:     # guess already exists in adjacent row
            check_2 = True

    result.append(check_1)
    result.append(check_2)
    return result


def check_other_candidates(guess, row_pos, col_pos, candidates_dict):
    horizontal = False
    vertical = False

    for key in candidates_dict.keys():
        if key[0] == row_pos:
            if key != (row_pos, col_pos):
                if guess in candidates_dict[key]:
                    horizontal = True
        if key[1] == col_pos:
            if key != (row_pos, col_pos):
                if guess in candidates_dict[key]:
                    vertical = True   

    result = horizontal and vertical
    return result


def select_possible_candidate(puzzle, row_pos, col_pos, candidates, candidates_dict):
    vertical_occupied, horizontal_occupied = determine_occupied(row_pos, col_pos)
    vertical = vertical_occupied[0] and vertical_occupied[1]
    horizontal = horizontal_occupied[0] and horizontal_occupied[1]


    for guess in candidates:
        adj_col_result = adjacent_col(puzzle, row_pos, col_pos, guess)
        adj_col = adj_col_result[0] and adj_col_result[1]

        adj_row_result = adjacent_row(puzzle, row_pos, col_pos, guess)
        adj_row = adj_row_result[0] and adj_row_result[1]

        if adj_col and adj_row:   
            puzzle[row_pos][col_pos] = guess
            del candidates_dict[(row_pos, col_pos)]
            return True
 
        elif vertical and adj_col:                                                                 
            puzzle[row_pos][col_pos] = guess                                        # |8
            del candidates_dict[(row_pos, col_pos)]                                 # |6
            return True                                                             # |X
                                                                                    # |   1   |
                                                                                    #   ...
                                                                                    #        1|

        elif horizontal and adj_row:
            puzzle[row_pos][col_pos] = guess
            del candidates_dict[(row_pos, col_pos)] 
            return True

        elif adj_row and horizontal_occupied[1] and adj_col_result[0]:              
            puzzle[row_pos][col_pos] = guess                                        #       |6      |  
            del candidates_dict[(row_pos, col_pos)]                                 #   6   |       |  
            return True                                                             #       |       |   6
        elif adj_row and horizontal_occupied[0] and adj_col_result[1]:              #       |*  X  1|      
            puzzle[row_pos][col_pos] = guess
            del candidates_dict[(row_pos, col_pos)]
            return True

        elif adj_col and vertical_occupied[0] and adj_row_result[1]:
            puzzle[row_pos][col_pos] = guess
            del candidates_dict[(row_pos, col_pos)]
            return True
        elif adj_col and vertical_occupied[1] and adj_row_result[0]:
            puzzle[row_pos][col_pos] = guess
            del candidates_dict[(row_pos, col_pos)]
            return True

        # if guess is not candidate for any other cell in row or column
        elif not check_other_candidates(guess, row_pos, col_pos, candidates_dict):
            puzzle[row_pos][col_pos] = guess
            del candidates_dict[(row_pos, col_pos)]
            return True

      
    return False


def valid_guess(puzzle, row_pos, col_pos, guess):
    row_result = single_position_row(puzzle, row_pos, col_pos, guess)
    col_result = single_position_col(puzzle, row_pos, col_pos, guess)
    group_result = single_position_group(puzzle, row_pos, col_pos, guess)

    if row_result and col_result and group_result:
        return True
    else:
        return False

def initialize_candidate_dict(puzzle):
    candidates_dict = {}
    for row in range(0, 9):
        for col in range(0, 9):
            if puzzle[row][col] == "*":
                candidates_dict[(row, col)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    return candidates_dict

def human_solve_sudoku(puzzle):
    solved = False
    candidates_dict = initialize_candidate_dict(puzzle)
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
            if valid_guess(puzzle, row_pos, col_pos, guess):
                candidates.append(guess)

        # print(f"row_pos: {row_pos}, col_pos: {col_pos}")

        candidates_dict[(row_pos, col_pos)] = candidates

        if len(candidates) == 1:
            puzzle[row_pos][col_pos] = candidates[0]    # single candidate, write to board
            del candidates_dict[(row_pos, col_pos)]
        else:
            # select between multiple candidates 
            # if no candidates selected then proceed
            if not (select_possible_candidate(puzzle, row_pos, col_pos, candidates, candidates_dict)):
            
                # no current solution for position
                no_solution.append((row_pos, col_pos))

if __name__ == '__main__':
    start_time = time.time()
    print(f"Board 0:")
    puzzle = board_11()
    print_board(puzzle)
    human_solve_sudoku(puzzle)
    print_board(puzzle)
