def print_board(board):
    print('-----')
    for row in board:
        print("|".join(row))
        print("-----")


def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True

    return False


def is_board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True


def main():
    board = [['-' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {player}, choose row (0, 1, 2): "))
        col = int(input(f"Player {player}, choose column (0, 1, 2): "))

        if board[row][col] == '-':
            board[row][col] = player

            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                player = 'O' if player == 'X' else 'X'
        else:
            print("That spot is already taken!")


if __name__ == "__main__":
    main()