

board = [[1,2,3],[4,5,6],[7,8,9]]
def print_board(board):
    for column in board:
        for row in column:
            print(row, end='')
        print(end='\n')

def verify_input_player1(input):
    if input in [1,2,3,4,5,6,7,8,9]:
        update_board_player1(input)
    elif if input == "reset":
