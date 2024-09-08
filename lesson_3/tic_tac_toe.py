'''
Tic Tac Toe is a 2-player game played on a 3x3 grid called the board. 
Each player takes a turn and marks a square on the board. The first player to get 3 squares in a row 
-- horizontally, vertically, or diagonally -- wins. If all 9 squares are filled and neither player 
has 3 in a row, the game ends in a tie.
'''

import random
import os

BOARD_LENGTH = 3
MAX_SCORE = 3
# first gets list of horizontal winnong moves, then vertical, and then finally each diagonal
WINNING_MOVES = [[(i, j) for i in range(BOARD_LENGTH)] for j in range(BOARD_LENGTH)] + [
    [(j, i) for i in range(BOARD_LENGTH)] for j in range(BOARD_LENGTH)] + [
    [(i, i) for i in range(BOARD_LENGTH)]] + [
    [(j, BOARD_LENGTH - 1 - j) for j in range(BOARD_LENGTH)]]

#numbered board to help understand the positioning on the board
INITIAL_BOARD = [[str(i * BOARD_LENGTH + j + 1) for j in range(BOARD_LENGTH)]
            for i in range(BOARD_LENGTH)]

def get_horizontal_coordinates(board, board_row_index, mark, max_move_len):
    ''' returns the horizontal coordinates of a player on the board in a row 
    that are either winning or about to win, we can set this based on the 
    max_move_len argument '''
    horizontal_moves = []
    for j in range(BOARD_LENGTH):
        if board[board_row_index][j] == mark:
            horizontal_moves.append((board_row_index, j))

        if board[board_row_index][j] not in [mark, " "]:
            horizontal_moves = []
            break

    return horizontal_moves if len(horizontal_moves) == max_move_len else []

def get_vertical_coordinates(board, board_col_index, mark, max_move_len):
    ''' same as get_horizontal_coordinates() but it checks 
    vertically in each column of the board '''
    vertical_moves = []
    for j in range(BOARD_LENGTH):
        if board[j][board_col_index] == mark:
            vertical_moves.append((j, board_col_index))

        if board[j][board_col_index] not in [mark, " "]:
            vertical_moves = []
            break

    return vertical_moves if len(vertical_moves) == max_move_len else []

def get_diagonal_coordinates(board, mark, max_move_len):
    ''' same as get_horizontal_coordinates() but it checks but
    it returns the diagonal coordinates of the player '''
    diagonal_1 = []
    diagonal_2 = []
    for i in range(BOARD_LENGTH):
        if board[i][i] == mark:
            diagonal_1.append((i, i))

        if board[i][BOARD_LENGTH - 1 - i]  == mark:
            diagonal_2.append((i, BOARD_LENGTH - 1 - i))

        if board[i][i] not in [mark, " "]:
            diagonal_1 = []

        if board[i][BOARD_LENGTH - 1 - i] not in [mark, " "]:
            diagonal_2 = []

    if len(diagonal_1) == max_move_len:
        return diagonal_1

    if len(diagonal_2) == max_move_len:
        return diagonal_2

    return []

def finding_player_coordinates(board, mark, max_move_len = BOARD_LENGTH):
    ''' finds the player coordinates for each case and then returns the
    ones that matches our senario, i.e. winning or about to win coordinates'''
    for i in range(BOARD_LENGTH): # in every iteration we're checking each direction
        horizontal = get_horizontal_coordinates(board, i, mark, max_move_len)
        vertical = get_vertical_coordinates(board, i, mark, max_move_len)
        if horizontal or vertical:
            return horizontal or vertical

    return get_diagonal_coordinates(board, mark, max_move_len) or None

def finding_winner(board, player_marks):
    ''' calls finding_player_coordinates() for both players, and if any coordinates are
    returned by a player then it returns that, else it returns None'''
    if finding_player_coordinates(board, player_marks['user']):
        return "user"

    if finding_player_coordinates(board, player_marks['computer']):
        return "computer"

    return None

def update_scores(winner_name, scores):
    ''' updates the score of the player based on the person who won '''
    scores[winner_name] += 1
    if winner_name == 'user':
        print('Congrats! You are the winner of this round.')
    else:
        print("You Lost!")

def display_board(board, player_mark):
    ''' displays the board '''
    print(f"\nYou are {player_mark['user']} and "
          f"Computer is {player_mark['computer']}\n")
    for i in range(BOARD_LENGTH):
        for j in range(BOARD_LENGTH):
            print(f'  {board[i][j]}', end="")
            if j < (BOARD_LENGTH - 1):
                print('     |', end="")

        print()
        if i < (BOARD_LENGTH - 1):
            print('--------+' * (BOARD_LENGTH))
    print()

def join_or(lst, delimeter = ', ', last_word = 'or'):
    ''' joins and returns a new list based on the delimeter and last word provided'''
    lst_copy = lst[:]
    lst_copy[len(lst) - 1] = last_word + " " + str(lst[len(lst) - 1])
    str_lst = delimeter.join(map(str, lst_copy))
    return str_lst

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

def find_missing_move(board, move_list):
    ''' returns the missing winning move that need to be made in order to win
    a game, finds it from the difference of two sets (winning moves and mmoves made) 
    to find the missing one '''
    if move_list:
        moves_made_set = set(move_list)
        for item in WINNING_MOVES:
            winning_move_set = set(item)

            if len(winning_move_set & moves_made_set) == len(moves_made_set):
                missing_move = winning_move_set - moves_made_set
                move = missing_move.pop()

                return move if move and (board[move[0]][move[1]] == " ") else None
    return None

def user_move(board, player_mark):
    ''' asks user to choose their move, and marks the move on the board '''
    print("YOUR TURN")
    moves_available = find_empty_positions(board)

    while True:
        try:
            move = int(input(f"Please pick your move from following "
                             f"{join_or(moves_available)} : "))
            if move not in moves_available:
                print("Error! Position is not wthin the range or available. ")
            else:
                break

        except ValueError:
            print("Error! Incorrect Input.")

    row, col = get_row_col(move)
    board[row][col] = player_mark['user']

def computer_ai(board, players_marks):
    '''
    first we check if there's any way we can make an offensice move and then check for
    defense. if we have neither then we return None.
    in order to check for offensive move we first find the coordinates of the computer
    using finding_player_coordinates(), and then try and find the missing winning move 
    through find_missing_move(). 
    we do the same for defense logic, but instead of finding computer's move we find user's
    '''
    comp_moves = finding_player_coordinates(board, players_marks["computer"], BOARD_LENGTH - 1)
    ofense_move = find_missing_move(board, comp_moves)

    user_moves = finding_player_coordinates(board, players_marks["user"], BOARD_LENGTH - 1)
    defense_move = find_missing_move(board, user_moves)

    return ofense_move or defense_move or None

def computer_move(board, player_mark):
    ''' makes a random choice for a move within the range specified, and 
    marks the move on the board '''
    print("COMPUTER'S TURN")

    ai_move = computer_ai(board, player_mark)
    if ai_move:
        row, col = ai_move[0], ai_move[1]

    else:
        moves_available = find_empty_positions(board)
        move = random.choice(moves_available)
        row, col = get_row_col(move)

    board[row][col] = player_mark['computer']

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

    print(f"You are '{player_mark['user']}' and "
          f"Computer is '{player_mark['computer']}.'")

def welcome():
    ''' displays welcome message and rules '''
    print('''\n\t\t\t\tWelcome to the game of Tic Tac Toe.
          1. It is a 2-player game played on a NxN grid called the board played against a computer.
          2. You can either choose 'X', or 'O' as your player mark.
          3. Each player takes a turn and marks a square on the board.
          4. The first player to get N squares in a row wins.\n''')

def goodbye():
    ''' prints a goodbye message '''
    print("Bye! It was nice playing with you.")

def win_or_tie(board, scores, player_mark):
    ''' function to determine whether the game has met it's ending condition, i.e. 
    whether somebody has won, or the board is full and it's a tie '''
    game_winner = finding_winner(board, player_mark)
    if game_winner:
        update_scores(game_winner, scores)
        print(f"Your Score : {scores['user']}\n"
              f"Computer's Score : {scores['computer']}")
        return True

    if len(find_empty_positions(board)) == 0:
        print("It's a TIE!")
        return True

    return False

def play_again():
    ''' asks the user if he wants to play again or not '''
    again = ' '
    while again not in ['y', 'n', 'yes', 'no']:
        again = input("Do you want to play again? (y/n) ")
        again = again.strip().lower()

    if again[0] == 'n':
        goodbye()
        return False

    return True

def main():
    ''' main function that contains the executional flow of the program '''
    welcome()
    player_mark = {
        'user' : '',
        'computer' : ''
    }
    choose_mark(player_mark)

    while True:
        scores = {
        'user' : 0,
        'computer' : 0
        }
        game_round  = 1
        while game_round <= MAX_SCORE:
            board = [[' '] * BOARD_LENGTH for _ in range(BOARD_LENGTH)]
            print(f'\n---> Round {game_round}')

            while not win_or_tie(board, scores, player_mark):
                print("---> NUMBERED BOARD")
                display_board(INITIAL_BOARD, player_mark)

                print("---> CURRENT BOARD")
                display_board(board, player_mark)
                user_move(board, player_mark)

                if win_or_tie(board, scores, player_mark):
                    display_board(board, player_mark)
                    break

                computer_move(board, player_mark)
                os.system('cls || clear')

            game_round += 1

        if scores['user'] > scores['computer']:
            print('You are the winner of the overall match.')
        else:
            print('Computer is the winner of the overall match.')

        if not play_again():
            break

if __name__ == "__main__":
    main()
