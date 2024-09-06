import random
import os

# Initialize the game board and scores
BOARD = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

SCORES = {
    'user': 0,
    'computer': 0
}

PLAYER_MARK = {
    'user': '',
    'computer': ''
}

def winner():
    if horizontal_win():
        return horizontal_win()
    elif vertical_win():
        return vertical_win()
    elif diagonal_win():
        return diagonal_win()
    else:
        return None

def update_scores(winner):
    for player, mark in PLAYER_MARK.items():
        if mark == winner:
            SCORES[player] += 1
            if player == 'user':
                print('Congrats! You are the winner of this game.')
            else:
                print("You Lost!")
            break

def display_board():
    for i in range(len(BOARD)):
        print('     |     |')
        print(f"  {BOARD[i][0]}  |  {BOARD[i][1]}  |  {BOARD[i][2]}")
        print('     |     |')
        if i < (len(BOARD) - 1):
            print('-----+-----+-----')

def is_board_full():
    return not any('_' in row for row in BOARD)

def valid_move(row, col):
    return (1 <= row <= len(BOARD) and 1 <= col <= len(BOARD)) and (BOARD[row - 1][col - 1] == '_')

def vertical_win():
    for i in range(len(BOARD)):
        if BOARD[0][i] != '_' and BOARD[0][i] == BOARD[1][i] == BOARD[2][i]:
            return BOARD[0][i]
    return None

def horizontal_win():
    for i in range(len(BOARD)):
        if BOARD[i][0] != '_' and BOARD[i][0] == BOARD[i][1] == BOARD[i][2]:
            return BOARD[i][0]
    return None

def diagonal_win():
    if BOARD[1][1] != '_' and (BOARD[0][0] == BOARD[1][1] == BOARD[2][2]):
        return BOARD[1][1]
    if BOARD[1][1] != '_' and (BOARD[0][2] == BOARD[1][1] == BOARD[2][0]):
        return BOARD[1][1]
    return None

def user_move():
    print("YOUR TURN")
    print("Make sure that your input for row and column is separated by a space and should be within the range of 1 to 3!")
    
    u_row, u_col = -1, -1
    while not valid_move(u_row, u_col):
        user_input = input("Please pick your move (row column): ")
        try:
            u_row, u_col = map(int, user_input.split())
            if not valid_move(u_row, u_col):
                print("Error! Move is not valid or out of range.")
        except ValueError:
            print("Error! Please enter two numbers separated by a space.")
    
    BOARD[u_row - 1][u_col - 1] = PLAYER_MARK['user']

def computer_move():
    print("COMPUTER TURN")
    c_row, c_col = -1, -1
    while not valid_move(c_row, c_col):
        c_row = random.randint(1, 3)
        c_col = random.randint(1, 3)
    BOARD[c_row - 1][c_col - 1] = PLAYER_MARK['computer']

def choose_mark():
    mark = ''
    while mark not in ['X', 'O']:
        mark = input("Choose your mark for the game (X or O) : ").strip().upper()
    PLAYER_MARK['user'] = mark
    PLAYER_MARK['computer'] = 'O' if mark == 'X' else 'X'
    print(f"Your player mark is '{PLAYER_MARK['user']}' and Computer's player mark is '{PLAYER_MARK['computer']}'.")

def welcome():
    print('''\n\t\t\t\tWelcome to the game of Tic Tac Toe.
          1. It is a 2-player game played on a 3x3 grid called the board played against a computer.
          2. You can either choose 'X', or 'O' as your player mark.
          3. Each player takes a turn and marks a square on the board.
          4. The first player to get 3 squares in a row (horizontally, vertically, or diagonally) wins.
          5. If all 9 squares are filled and neither player has 3 in a row, the game ends in a tie.\n\n''')

def goodbye():
    print("It was nice playing with you.")

def winner_or_tie():
    game_winner = winner()
    if game_winner:
        update_scores(game_winner)
        print(f'Your Score : {SCORES["user"]} \nComputer Score : {SCORES["computer"]}')
        return True
    if is_board_full():
        print("It's a TIE!")
        return True
    return False

def main():
    welcome()
    while True:
        choose_mark()
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen based on the OS
        display_board()

        while True:
            user_move()
            display_board()
            if winner_or_tie():
                break
            
            if is_board_full() and winner() is None:
                break

            computer_move()
            display_board()
            if winner_or_tie():
                break
            
            if is_board_full() and winner() is None:
                break

        again = ''
        os.system('cls' if os.name == 'nt' else 'clear')
        while again not in ['y', 'n', 'yes', 'no']:
            again = input("Do you want to play again? (y/n) ").strip().lower()
        if again.startswith('n'):
            goodbye()
            break

if __name__ == "__main__":
    main()
