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

def check_path(brd, move):
    row = CARS[move[0]][0]
    col = CARS[move[0]][1]
    leng = CARS[move[0]][3]
    if move[1] == 'u':
        for spot in range(0,int(move[2])):
            if brd[row-spot-1][col] != '.':
                return False
    elif move[1] == 'd':
        for spot in range(0,int(move[2])):
            if brd[row+spot+leng][col] != '.':
                return False
    elif move[1] == 'l':
        for spot in range(0,int(move[2])):
            if brd[row][col-spot-1] != '.':
                return False
    elif move[1] == 'r':
        for spot in range(0,int(move[2])):
            if brd[row][col+spot+leng] != '.':
                return False
    else:
        print "that is not a valid move"
        return False
    return True

def validate_move (brd,move):
    # check that piece is on the board
    # check that piece placed so it can move in that direction
    # check that piece would be in bound
    if move[0] in CARS:
        if move[1] == 'u' and CARS[move[0]][2] == 'v':
            if (CARS[move[0]][0] - int(move[2]) >= 0):
                return check_path(brd, move) 
            else:
                print 'you done messed up now'
                return False
        elif move[1] == 'd' and CARS[move[0]][2] == 'v':
            if (CARS[move[0]][0] + CARS[move[0]][3] + int(move[2]) <= (GRID_SIZE)): 
                return check_path(brd, move) 
            else:
                print 'you done messed up now'
                return False
        elif move[1] == 'l' and CARS[move[0]][2] == 'h':
            if (CARS[move[0]][1] - int(move[2]) >= 0): 
                return check_path(brd, move) 
            else:
                print 'you done messed up now'
                return False
        elif move[1] == 'r' and CARS[move[0]][2] == 'h':
            if (CARS[move[0]][1] + CARS[move[0]][3] + int(move[2]) <= (GRID_SIZE)):  
                return check_path(brd, move)  
            else:
                print 'you done messed up now'
                return False
        else:
            print 'car is in the wrong direction'
            return False
    else:
        print 'car is a lie'
        return False


def read_player_input (brd):
    move = raw_input('Select Car, Direction, and Distance: ')
    if len(move) != 3:
        print '3 characters plz'
    else:
        if(validate_move(brd, move)):
          return move
    # dummy move
    return 'xr0'


def update_board (brd,move):
    row = CARS[move[0]][0]
    col = CARS[move[0]][1]
    leng = CARS[move[0]][3]
    # delete old bitz
    if (CARS[move[0]][2] == 'h'):
      for spot in range(0,leng):
        brd[row][col+spot] = '.' 
    elif (CARS[move[0]][2] == 'v'):
      for spot in range(0,leng):
        brd[row+spot][col] = '.' 
    # add new bitz
    if (move[1] == 'd'):
      CARS[move[0]][0] = row + int(move[2])
      for spot in range(0,leng):
        brd[row+spot+int(move[2])][col] = move[0]
    elif (move[1] == 'r'):
      CARS[move[0]][1] = col + int(move[2])
      for spot in range(0,leng):
        brd[row][col+spot+int(move[2])] = move[0]
    elif (move[1] == 'u'):
      CARS[move[0]][0] = row - int(move[2])
      for spot in range(0,leng):
        brd[row+spot-int(move[2])][col] = move[0]
    elif (move[1] == 'l'):
      CARS[move[0]][1] = col - int(move[2])
      for spot in range(0,leng):
        brd[row][col+spot-int(move[2])] = move[0]
    
    return brd


def print_board (brd):
    for row in brd:
      print(row)

    
def done (brd):
    if (check_path(brd, 'xr' + str(GRID_SIZE - CARS['x'][0]))):
      return True



def create_initial_level ():
    board = []
    for i in range(0, GRID_SIZE):
      board.append(['.'] * GRID_SIZE)
    for carname, car in CARS.items():
      if car[2] == 'h':
        for spot in range(0,car[3]):
          board[car[0]][car[1]+spot] = carname
      elif car[2] == 'v':
        for spot in range(0,car[3]):
          board[car[0]+spot][car[1]] = carname
    return board


def main ():

    brd = create_initial_level()

    print_board(brd)

    while not done(brd):
        move = read_player_input(brd)
        brd = update_board(brd,move)
        print_board(brd)

    print 'YOU WIN! (Yay...)\n'
        

if __name__ == '__main__':
    main()
