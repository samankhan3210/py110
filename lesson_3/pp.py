BOARD_LENGTH = 5
board = [['- '] * BOARD_LENGTH for _ in range(BOARD_LENGTH)]
# position = 3
# row = (position - 1) // board_len
# col = (position - 1) % board_len
# board[row][col] = 'X'
# print(row, col)
# print(board)
board = [
    ['X', 'X', 'O', 'X', 'X'],
    ['O', 'X', ' ', 'X', 'X'],
    ['O', ' ', 'X', 'X', 'X'],
    ['O', 'X', ' ', 'X', 'X'],
    [' ', 'X', 'X', 'X', 'X']
]

indexes = [(row_index, col_index) for row_index in range(BOARD_LENGTH)
               for col_index in range(BOARD_LENGTH)
               if board[row_index][col_index] == ' ']
positions = [(item[0] * BOARD_LENGTH) + item[1] + 1 for item in indexes]
print(positions)