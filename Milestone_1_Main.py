#! /usr/bin/python3

def clearscreen():
    print("\n" * 100)


def print_board(board):
    for row in board:
        for column in row:
            print(column, end='')
        print(end='\n')
    print('\n')

def next_turn(which_player):
    move = input("Enter 'reset' to start over and 'quit' to exit game \nTo move, choose spot to play (1-9).\nPlayer {}, you're up:".format(which_player))
    return move

def verify_input_player1(input):
    if input in [1,2,3,4,5,6,7,8,9]:
        update_board_player1(input)
    #elif input == "reset":


clearscreen()
player_turn = 1
board = [[1,2,3],[4,5,6],[7,8,9]]
print('Welcome to the classic Tic Tac Toe game \n \n')
print_board(board)
while True:
    next_turn(player_turn)


''' use while True: when it gets to the end, it will cycle back to just under this statement, your loop
Make sure to plant exits when appropriate probably an unindented line that says exit()'''