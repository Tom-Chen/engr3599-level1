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
CAR_LENGTHS = {"O" : 3}
CARS = {"o" : [1,3 , 'h', 2]}

def validate_move (brd,move):
    # FIX ME!
    # check that piece is on the board
    if CARS[move[0]]:
        if move[1] == "u" and CARS[move[0]] == "v":
            if (CARS[move[0]][0] - move[2] >= 0):
                print "yay you are in the boudries" 
            else:
                print "you done messed up now"
        if move[1] == "d" and CARS[move[0]] == "v":
            if (CARS[move[0]][0] + CARS[move[0]][3] + move[2] <= (GRID_SIZE)): 
                print "yay you are in the boudries" 
            else:
                print "you done messed up now"
        if move[1] == "l" and CARS[move[0]] == "h":
            if (CARS[move[0]][1] - move[2] >= 0): 
                print "yay you are in the boudries" 
            else:
                print "you done messed up now"
        if move[1] == "r" and CARS[move[0]] == "h":
            if (CARS[move[0]][1] + CARS[move[0]][3] + move[2] <= (GRID_SIZE)):  
                print "yay you are in the boudries" 
            else:
                print "you done messed up now"
        else:
            print "car is in the wrong direction"
    else:
        print "car is a lie"
    print "oh no!!! that is not a valid car :("
    # check that piece placed so it can move in that direction
    # check that piece would be in bound
    # check that path to target position is free
    return False


def read_player_input (brd):
    move = raw_input("Select Car, Direction, and Distance")
    if move.len() != 3:
        print "Please input needed information"
    else:
        return move



    return None


def update_board (brd,move):
    # FIX ME!
    return brd


def print_board (brd):
    # FIX ME!
    print "<some output of the board>"

    
def done (brd):
    # FIX ME!
    return True


# initial board:
# Board positions (1-6,1-6), directions 'r' or 'd'
#
# X @ (2,3) r
# A @ (2,4) r
# B @ (2,5) d
# C @ (3,6) r
# O @ (4,3) d
# P @ (6,4) d


def create_initial_level ():
    board = [0] * (GRID_SIZE * GRID_SIZE)

    return None


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
