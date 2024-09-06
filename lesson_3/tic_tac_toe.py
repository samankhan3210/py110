'''
Tic Tac Toe is a 2-player game played on a 3x3 grid called the board. 
Each player takes a turn and marks a square on the board. The first player to get 3 squares in a row 
-- horizontally, vertically, or diagonally -- wins. If all 9 squares are filled and neither player 
has 3 in a row, the game ends in a tie.
'''

import random
import os

BOARD_LENGTH = 3
MOVES_AVAILABLE = BOARD_LENGTH * BOARD_LENGTH
# MAX_SCORE = 3

def winner(board):
    ''' checks the board vertically, horizonatlly, and diagonally then 
    returns the mark of the winning player '''
    # checking diagonally (first checks right diagonal and then left)
    mid = BOARD_LENGTH // 2
    if board[mid][mid] != ' ' and \
        (len({board[i][i] for i in range(BOARD_LENGTH)}) == 1 or \
         len({board[i][BOARD_LENGTH - 1 - i] for i in range(BOARD_LENGTH)}) == 1):
        return board[mid][mid]

    for i in range(BOARD_LENGTH):
        if board[i][i] != ' ':
            # checking horizontally first and then vertically
            if len(set(board[i])) == 1 or len({row[i] for row in board}) == 1:
                return board[i][i]

    return None

def update_scores(winner_mark, player_mark, scores):
    ''' updates the score of the player based on the person who won by comparing the mark of each
        player against the winning mark '''
    for player, mark in player_mark.items():
        if mark == winner_mark:
            scores[player] += 1

            if player == 'user':
                print('Congrats! You are the winner of this game.')
            else:
                print("You Lost!")

            break

def display_board(board):
    ''' displays the board '''
    print('\n---> Board Currently\n')
    for i in range(BOARD_LENGTH):
        for j in range(BOARD_LENGTH):
            print(f'  {board[i][j]}', end="")
            if j < (BOARD_LENGTH - 1):
                print('     |', end="")

        print()
        if i < (BOARD_LENGTH - 1):
            print('--------+' * (BOARD_LENGTH))

def find_empty_positions(board):
    ''' returns the positions that are still empty and available '''
    indexes = [(row_index, col_index) for row_index in range(BOARD_LENGTH)
               for col_index in range(BOARD_LENGTH)
               if board[row_index][col_index] == ' ']
    positions = [(item[0] * BOARD_LENGTH) + item[1] + 1 for item in indexes]
    return positions

def get_row_col(move_position):
    ''' calculates row and column from the position chosen to make the process 
    of retrieval and modification easier and simpler '''
    row = (move_position - 1) // BOARD_LENGTH
    col = (move_position - 1) % BOARD_LENGTH
    return row, col

# def valid_move(board, position):
#     ''' checks whether the position chosen for the move is valid or not,
#     make sures that it's within the range of the board and it's empty'''
#     row, col = get_row_col(position)
#     return (1 <= position <= MOVES_AVAILABLE) and (board[row][col] == ' ')

def user_move(board, player_mark):
    ''' asks user to choose their move, and marks the move on the board '''
    print("YOUR TURN")
    moves_available = find_empty_positions(board)

    while True:
        try:
            move = int(input(f"Please pick your move {', '.join(map(str, moves_available))} : "))
            if move not in moves_available:
                print("Error! Position is not wthin the range or available. ")
            else:
                print(f"Your Move : {move}")
                break

        except ValueError:
            print("Error! Incorrect Input.")

    row, col = get_row_col(move)
    board[row][col] = player_mark['user']

def computer_move(board, player_mark):
    ''' makes a random choice for a move within the range specified, and 
    marks the move on the board '''
    print("COMPUTER'S TURN")
    moves_available = find_empty_positions(board)
    move = random.choice(moves_available)
    row, col = get_row_col(move)
    board[row][col] = player_mark['computer']
    print(f"Computer's Move : {move}")

def choose_mark(player_mark):
    ''' asks the user to choose their sybmbol of choice and assigns it to them '''
    mark = ''
    while mark not in ['X', 'O']:
        mark = input("Choose your mark for the game (X or O) : ")
        mark = mark.strip().upper()

    player_mark['user'] = mark
    if mark == 'X':
        player_mark['computer'] = 'O'
    else:
        player_mark['computer'] = 'X'

    print(f"You are : '{player_mark['user']}'\nComputer is : '{player_mark['computer']}'")

def welcome():
    ''' displays welcome message and rules '''
    print('''\n\t\t\t\tWelcome to the game of Tic Tac Toe.
          1. It is a 2-player game played on a NxN grid called the board played against a computer.
          2. You can either choose 'X', or 'O' as your player mark.
          3. Each player takes a turn and marks a square on the board.
          4. The first player to get N squares in a row wins.''')

def goodbye():
    ''' prints a goodbye message '''
    print("Bye! It was nice playing with you.")

def winner_or_tie(board, scores, player_mark):
    ''' function to determine whether the game has met it's ending condition, i.e. 
    whether somebosy has won or the board is full and it's a tie '''
    display_board(board)
    game_winner = winner(board)
    if game_winner is not None:
        update_scores(game_winner, player_mark, scores)
        print(f'Your Score : {scores["user"]} \nComputer Score : {scores["computer"]}')
        return True

    if len(find_empty_positions(board)) == 0:
        print("It's a TIE!")
        return True

    return False

def main():
    ''' main function that contains the executional flow of the program '''
    welcome()
    scores = {
    'user' : 0,
    'computer' : 0
    }
    player_mark = {
        'user' : '',
        'computer' : ''
    }
    choose_mark(player_mark)

    while True:
        board = [[' '] * BOARD_LENGTH for _ in range(BOARD_LENGTH)]

        while not winner_or_tie(board, scores, player_mark):
            user_move(board, player_mark)

            if winner_or_tie(board, scores, player_mark):
                break

            computer_move(board, player_mark)

        again = ''
        while again not in ['y', 'n', 'yes', 'no']:
            again = input("Do you want to play again? (y/n) ")
            again = again.strip().lower()

        os.system('cls || clear')
        if again[0] == 'n':
            goodbye()
            break


if __name__ == "__main__":
    main()
