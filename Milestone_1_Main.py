#! /usr/bin/python3


def clearscreen():
    print("\n" * 100)

def move_map(board):
    map = {}
    for row in board:
        for column in row:
            map.update({column: 0})

    for i in range(1, 9):
        for key in map:
            map[key] = next((i, position.index(key))
                            for i, position in enumerate(board)
                            if key in position) #If this gives errors check indentation


def print_board(board):
    for row in board:
        for column in row:
            print(column, end='')
        print(end='\n')
    print('\n')

def take_turn(which_player,moves_made):
    move = input("Enter 'quit' to exit game \nTo move, choose spot to play (1-9).\nPlayer {}, you're up: ".format(which_player))
    if move in ['1','2','3','4','5','6','7','8','9']:
        move = int(move)
        if move in moves_made:
            clearscreen()
            print_board(board)
            print('    That move has already been made, try again!')
            return take_turn(which_player, moves_made)
        return move
    elif move == "quit":
        quit()
    else:
        clearscreen()
        print_board(board)
        print('    !!!!Not a valid input, try again!!!!')
        return take_turn(which_player,moves_made)


def make_move(move,player_turn):

    return(player_turn)



player_turn = 1
board = [[1,2,3],[4,5,6],[7,8,9]]
clearscreen()
moves_made = []
map = move_map(board)
print('Welcome to the classic game of Tic Tac Toe \n')
print_board(board)
while True:
    move = take_turn(player_turn,moves_made)
    #win_test = make_move(move,player_turn)
    #moves_made.append(move)

'''
To Do:
Create something that contains all possible ways to win for either player:
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
0,0 1,0 2,0
0,1, 1,1 2,1
0,2 1,2 2,2
0,0 1,1 2,2
2,0 1,1 0,2
or:
1,2,3
4,5,6
7,8,9
1,4,7
2,5,8
3,6,9
1,5,9
7,5,3
Function to make move:
    After checking move hasn't been made before
        If has been made, state so, take input and pass thru verify function
    Make move
    Checks if player has won
    Changes global player variable
make sure board update takes into account and updates the player
'''