import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

def minimax(board, depth, maximizing_player):
    if check_winner(board, 'X'):
        return -10 + depth, None
    elif check_winner(board, 'O'):
        return 10 - depth, None
    elif is_board_full(board):
        return 0, None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval, _ = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval, _ = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not check_winner(board, 'X') and not check_winner(board, 'O') and not is_board_full(board):
        player_move = None
        while player_move not in available_moves(board):
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            player_move = (row, col)
        board[player_move[0]][player_move[1]] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        print("Computer's turn...")
        _, ai_move = minimax(board, 0, True)
        board[ai_move[0]][ai_move[1]] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
