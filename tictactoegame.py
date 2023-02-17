import random

def print_board(board):
    """Prints the game board."""
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def get_player_move(board):
    """Gets the player's move and updates the board."""
    while True:
        move = input('Enter your move (1-9): ')
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'
                return
            else:
                print('That space is already taken. Try again.')
        else:
            print('Invalid input. Try again.')

def get_computer_move(board):
    """Gets the computer's move and updates the board."""
    print('Computer is making its move...')
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = 'O'
            return

def check_win(board):
    """Checks if there is a winner."""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]
    # No winner yet
    return None

def is_board_full(board):
    """Checks if the board is full."""
    return ' ' not in board

def play_game():
    """Plays a game of Tic Tac Toe."""
    board = [' '] * 9
    print('Welcome to Tic Tac Toe!')
    print_board(board)
    while True:
        get_player_move(board)
        print_board(board)
        winner = check_win(board)
        if winner is not None:
            print('Congratulations, ' + winner + ', you win!')
            break
        if is_board_full(board):
            print('The game is a tie!')
            break
        get_computer_move(board)
        print_board(board)
        winner = check_win(board)
        if winner is not None:
            print('Sorry, ' + winner + ' wins. Better luck next time!')
            break
        if is_board_full(board):
            print('The game is a tie!')
            break

if __name__ == '__main__':
    play_game()