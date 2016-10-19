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
    move = input("Enter 'quit' to exit game \nTo move, choose spot to play (1-9).\nPlayer {}, you're up: ".format(which_player))
    return move

def verify_input(input):
    if input in [1,2,3,4,5,6,7,8,9]:
        return input
    elif input == "quit":
        quit()

def make_move(move,player_turn):

    return(player_turn)

clearscreen()
player_turn = 1
board = [[1,2,3],[4,5,6],[7,8,9]]
print('Welcome to the classic game of Tic Tac Toe \n')
print_board(board)
while True:
    move = next_turn(player_turn)
    verified = verify_input(move)
    player_turn = make_move(verified,player_turn)


'''
To Do:
Create something that contains all possible ways to win for either player
Function to make move:
    After checking move hasn't been made before
        If has been made, state so, take input and pass thru verify function
    Checks if player has won
    Changes global player variable
make sure board update takes into account and updates the player
'''