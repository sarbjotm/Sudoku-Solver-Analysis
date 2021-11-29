def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print(f"------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(f" | ", end="")

            if j == 8:
                print(f"{board[i][j]}")
            else:
                print(f"{board[i][j]} ", end="")