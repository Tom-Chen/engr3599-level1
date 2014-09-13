#!/usr/bin/env python

#
# Game Programming, Level 1 Project
#
# RUSH HOUR
#
# A simple puzzle game, based on the physical game of the same name 
# by Binary Arts Corp
#



# fail somewhat gracefully

def fail (msg):
    raise StandardError(msg)

GRID_SIZE = 6
CAR_LENGTHS = {'o' : 3}
CARS = {'a' : [3,1 , 'h', 2],
        'b' : [4,1 , 'v', 2],
        'c' : [5,2 , 'h', 2],
        'o' : [0,3 , 'v', 3],
        'p' : [3,5 , 'v', 3],
        'x' : [2,1 , 'h', 2],}

def validate_move (brd,move):
    # check that piece is on the board
    # check that piece placed so it can move in that direction
    # check that piece would be in bound
    if CARS[move[0]]:
        if move[1] == 'u' and CARS[move[0]][2] == 'v':
            if (CARS[move[0]][0] - int(move[2]) >= 0):
                print 'yay you are in the boundaries' 
            else:
                print 'you done messed up now'
        elif move[1] == 'd' and CARS[move[0]][2] == 'v':
            if (CARS[move[0]][0] + CARS[move[0]][3] + int(move[2]) <= (GRID_SIZE)): 
                print 'yay you are in the boundaries' 
            else:
                print 'you done messed up now'
        elif move[1] == 'l' and CARS[move[0]][2] == 'h':
            if (CARS[move[0]][1] - int(move[2]) >= 0): 
                print 'yay you are in the boundaries' 
            else:
                print 'you done messed up now'
        elif move[1] == 'r' and CARS[move[0]][2] == 'h':
            if (CARS[move[0]][1] + CARS[move[0]][3] + int(move[2]) <= (GRID_SIZE)):  
                print 'yay you are in the boundaries' 
            else:
                print 'you done messed up now'
        else:
            print 'car is in the wrong direction'
    else:
        print 'car is a lie'
    # check that path to target position is free
    return False


def read_player_input (brd):
    move = raw_input('Select Car, Direction, and Distance: ')
    if len(move) != 3:
        print '3 characters plz'
    else:
        return validate_move(brd, move)



    return None


def update_board (brd,move):
    # FIX ME!
    return brd


def print_board (brd):
    # FIX ME!
    print '<some output of the board>'

    
def done (brd):
    # FIX ME!
    return True



def create_initial_level ():
    board = []
    for i in range(0, GRID_SIZE):
      board.append(['.'] * GRID_SIZE)
    for carname, car in CARS.items():
      if car[2] == 'h':
        for spot in range(0,car[3]):
          # print car[0], car[1]+spot, board[car[0]]
          board[car[0]][car[1]+spot] = carname
      elif car[2] == 'v':
        for spot in range(0,car[3]):
          # print car[0]+spot, car[1], board[car[0]+spot]
          board[car[0]+spot][car[1]] = carname
    for row in board:
      print(row)
    return None


def main ():

    brd = create_initial_level()

    print_board(brd)

    while done(brd):
        move = read_player_input(brd)
        brd = update_board(brd,move)
        print_board(brd)

    print 'YOU WIN! (Yay...)\n'
        

if __name__ == '__main__':
    main()
