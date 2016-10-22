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
    return map


def print_board(board):
    for row in board:
        for column in row:
            print(column, end='')
        print(end='\n')
    print('\n')

def take_turn(which_player,moves_made):
    move = input("To move, choose spot to play (1-9).\nEnter 'quit' to exit game \nPlayer 1 = X, Player 2 = O\nPlayer {}, you're up: ".format(which_player))
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
    position = map.get(move)
    if player_turn == 1:
        board[position[0]][position[1]]='X'
    else:
        board[position[0]][position[1]] = 'O'

    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1

    return(player_turn)

# NEED TO CLEAN UP THIS FUNCTION!!

def winner_test(player_turn,previous_player):
    if player_turn == 1:
        test = 'O'
    else:
        test = 'X'
    test = test*3

    if test == str(board[0][0])+ str(board[0][1]) + str(board[0][2]):
        print('Player {} is the winner!!'.format(previous_player))
        quit()
    elif test == str(board[1][0])+ str(board[1][1]) + str(board[1][2]):
        print('Player {} is the winner!!'.format(previous_player))
        quit()
    elif test == str(board[2][0])+ str(board[2][1]) + str(board[2][2]):
        print('Player {} is the winner!!'.format(previous_player))
        quit()
    elif test == str(board[0][0])+ str(board[1][0]) + str(board[2][0]):
        print('Player {} is the winner!!'.format(previous_player))
        quit()
    elif test == str(board[0][1])+ str(board[1][1]) + str(board[2][1]):
        print('Player {} is the winner!!'.format(previous_player))
        quit()
    elif test == str(board[0][2])+ str(board[1][2]) + str(board[2][2]):
        print('Player {} is the winner!!'.format(previous_player))
        quit()
    elif test == str(board[0][0])+ str(board[1][1]) + str(board[2][2]):
        print('Player {} is the winner!!'.format(previous_player))
        quit()
    elif test == str(board[2][0])+ str(board[1][1]) + str(board[0][2]):
        print('Player {} is the winner!!'.format(previous_player))
        quit()



player_turn = 1
board = [[1,2,3],[4,5,6],[7,8,9]]
clearscreen()
moves_made = []
map = move_map(board)
print('Welcome to the classic game of Tic Tac Toe \n')
print_board(board)
while True:
    move = take_turn(player_turn,moves_made)
    previous_player = player_turn
    player_turn = make_move(move,player_turn)
    clearscreen()
    print_board(board)
    winner_test(player_turn,previous_player)
    moves_made.append(move)
