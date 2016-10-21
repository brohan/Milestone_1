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


player_turn = 1
board = [[1,2,3],[4,5,6],[7,8,9]]
clearscreen()
moves_made = []
map = move_map(board)
print('Welcome to the classic game of Tic Tac Toe \n')
print_board(board)
while True:
    move = take_turn(player_turn,moves_made)
    player_turn = make_move(move,player_turn)
    print_board(board)
    #Check if player won (compare board to winning solutions)
    moves_made.append(move)

'''
Create something that contains all possible ways to win for either player, compares it to board after move:
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

'''