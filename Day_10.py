import math

board = [" "]*9

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_win(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_positions)

def is_draw():
    return " " not in board

def minimax(is_max):
    if check_win("O"):
        return 1
    if check_win("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

player = "X"

for turn in range(9):
    print_board()

    if player == "X":
        move = int(input("Enter position (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move")
            continue
    else:
        move = best_move()
        print(f"Computer chose position {move + 1}")

    board[move] = player

    if check_win(player):
        print_board()
        if player == "X":
            print("You win!")
        else:
            print("Computer wins!")
        break

    player = "O" if player == "X" else "X"
else:
    print_board()
    print("It's a draw!")