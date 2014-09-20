#!/usr/bin/env python

#
# Game Programming, Level 1 Project
#
# RUSH HOUR
#
# A simple puzzle game, based on the physical game of the same name 
# by Binary Arts Corp
#

from graphics import *
from math import floor

# fail somewhat gracefully

def fail (msg):
    raise StandardError(msg)

GRID_SIZE = 6
CARS = {}
WIN = GraphWin("My Square", 400, 400)


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
        if move[1] == 'u' and CARS[move[0]][2] == 'd':
            if (CARS[move[0]][0] - int(move[2]) >= 0):
                return check_path(brd, move) 
            else:
                print 'you done messed up now'
                return False
        elif move[1] == 'd' and CARS[move[0]][2] == 'd':
            if (CARS[move[0]][0] + CARS[move[0]][3] + int(move[2]) <= (GRID_SIZE)): 
                return check_path(brd, move) 
            else:
                print 'you done messed up now'
                return False
        elif move[1] == 'l' and CARS[move[0]][2] == 'r':
            if (CARS[move[0]][1] - int(move[2]) >= 0): 
                return check_path(brd, move) 
            else:
                print 'you done messed up now'
                return False
        elif move[1] == 'r' and CARS[move[0]][2] == 'r':
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

def draw_car(car, color):
  if car[2] == 'r':
    c = Rectangle(Point(car[1]*50+30,car[0]*50+30), Point(car[1]*50+20+50*car[3], car[0]*50+70))
    c.setFill(color)
    c.draw(WIN)
  elif car[2] == 'd':
    c = Rectangle(Point(car[1]*50+30,car[0]*50+30), Point(car[1]*50+70, car[0]*50+20+50*car[3]))
    c.setFill(color)
    c.draw(WIN)

def read_player_input (brd):
  point = WIN.getMouse()
  carname = brd[(point.getY()-30)/50][(point.getX()-30)/50]
  if carname != ".":
    draw_car(CARS[carname], "yellow")
    move = WIN.getKey()
    if move == "Up" or "Down" or "Left" or "Right":
      if validate_move(brd, carname+move[0].lower()+"1"):
        update_board(brd,carname+move[0].lower()+"1")
      draw_board()
    else :
      print "that is not a valid move"
    
    



def update_board (brd,move):
    row = CARS[move[0]][0]
    col = CARS[move[0]][1]
    leng = CARS[move[0]][3]
    # delete old bitz
    if (CARS[move[0]][2] == 'r'):
      for spot in range(0,leng):
        brd[row][col+spot] = '.' 
    elif (CARS[move[0]][2] == 'd'):
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



    
def done (brd):
    if (check_path(brd, 'xr' + str(GRID_SIZE - CARS['x'][0] - 1))):
      return True



def create_initial_level ():
    board = []
    for i in range(0, GRID_SIZE):
      board.append(['.'] * GRID_SIZE)
    for carname, car in CARS.items():
      if car[2] == 'r':
        for spot in range(0,car[3]):
          board[car[0]][car[1]+spot] = carname
      elif car[2] == 'd':
        for spot in range(0,car[3]):
          board[car[0]+spot][car[1]] = carname
    return board

def draw_board():
  c = Rectangle(Point(20,20), Point(330, 330))
  c.setFill("grey")
  c.draw(WIN)

  d = Polygon(Point(340,130), Point(340,170), Point(370,150))
  d.setFill("green")
  d.draw(WIN)

  for i in range(0,6):
    for j in range(0,6):
      c = Rectangle(Point(i*50+30,j*50+30),Point(i*50 + 70,j*50 +70))
      c.setFill("white")
      c.draw(WIN)

  for carname, car in CARS.items():
    draw_car(car, car[4])

def main ():
    global CARS
    CARS = {'a' : [3,1 , 'r', 2, "blue"],
            'b' : [4,1 , 'd', 2, "blue"],
            'c' : [5,2 , 'r', 2, "blue"],
            'o' : [0,3 , 'd', 3, "purple"],
            'p' : [3,5 , 'd', 3, "purple"],
            'x' : [2,1 , 'r', 2, "red"],}
    draw_board()
    brd = create_initial_level()

    while not done(brd):
        move = read_player_input(brd)
        #brd = update_board(brd,move)

    print 'YOU WIN! (Yay...)\n'
    WIN.close()

def main_with_initial(desc):
    import string
    desc = desc.lower()
    for i in xrange(0,len(desc),4):
      if (string.lowercase.index(desc[i]) <= 9):
        CARS[desc[i]] = [int(desc[i+2])-1, int(desc[i+1])-1, desc[i+3], 2, "blue"]
      elif (string.lowercase.index(desc[i]) == 23):
        CARS[desc[i]] = [int(desc[i+2])-1, int(desc[i+1])-1, desc[i+3], 2, "red"]
      else:
        CARS[desc[i]] = [int(desc[i+2])-1, int(desc[i+1])-1, desc[i+3], 3, "purple"]
    draw_board()   
    brd = create_initial_level()

    while not done(brd):
        move = read_player_input(brd)
        brd = update_board(brd,move)


    print 'YOU WIN! (Yay...)\n'

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        main_with_initial (sys.argv[1])
    else:
        main()