#!/usr/bin/env python
# 

#
# Game Programming, Level 2 Project
#
# TIC-TAC-TOE 4
#
# A simple strategy game, an extension of the standard 3x3 tic-tac-toe
#
from graphics import *
import sys
WIN = GraphWin("My Square", 400, 400)

WIN_SEQUENCES = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15],
    [0,4,8,12],
    [1,5,9,13],
    [2,6,10,14],
    [3,7,11,15],
    [0,5,10,15],
    [3,6,9,12]
]

MARK_VALUE = {
    'O': 1,
    '.': 0,
    'X': 10
}

def fail (msg):
    raise StandardError(msg)

def makeCoordinates(pos):
    x = (pos % 4) + 1
    y = (pos // 4) + 1
    return (x,y)

def makePos(coord):
  return ((coord[1]-1)*4+coord[0]-1)

def create_board (stri):
    board = []
    if len(stri) == 16:
        for letter in stri:
            if letter != '.' and 'X' and 'O':
                print "invalid symbol on board, please re input values"
            else:
                board.append(letter)
    else:
        print "that is not a valid board, please reinput values"
    return board



def has_mark (board,x,y):
    space = board[makePos((x,y))]
    if space == ".":
        return False
    else:
        return space

def has_win (board):
    for positions in WIN_SEQUENCES:
        s = sum(MARK_VALUE[board[pos]] for pos in positions)
        if s == 4:
            return 'O'
        if s == 40:
            return 'X'
    return False

def done (board):
    return (has_win(board) or not [ e for e in board if (e == '.')])

def print_board (board):
    for i in range(0,4):
        print '  ',board[i*4],board[i*4+1],board[i*4+2],board[i*4+3]
    print

def read_player_input (board, player):
    valid = [ i for (i,e) in enumerate(board) if e == '.']
    while True:
        move = raw_input('1-4,1-4: ')
        if move == 'q':
            exit(0)
        if len(move)>0 and ((int(move[2])-1)*4+int(move[0])-1) in valid:
            return (int(move[0]),int(move[2]))

def wait_player_input (board,player):
    point = WIN.getMouse()
    pos = board[(point.getY()-30)/50*4 + (point.getX()-30)/50]
    if pos == ".":
        return((point.getX()-30)/50+1, (point.getY()-30)/50+1)


def make_move (board,move,player):
    print(move)
    new_board = board[:]
    new_board[makePos(move)] = player
    return new_board


def computer_move (board,player):
    best_move_pos = best_move(board,player)
    return (best_move_pos)

def best_move (board,player):
    pos, val = min_max(board,player)
    return pos[val.index(min(val))]
    
def other (player):
    if player == 'X':
        return 'O'
    return 'X'

def utility (board,player):
    if has_win(board) == player:
        return -1
    if has_win(board) == other(player):
        return 1
    elif has_win(board) == False:
        return 0

def min_max(board,player):
    possible_moves = [ makeCoordinates(i) for (i,e) in enumerate(board) if e == '.']
    current = []

    ally = player
    enemy = other(player)
    
    def min_value (board,player):
        if (' ' not in board) or utility(board) != 0:
            return utility(board,ally)
        smallestBranch = 2
        for move in possible_moves:
            tempValue = max_value(make_move(board,move,ally),enemy)
            if tempValue < smallestBranch:
                smallestBranch = tempValue
        return(smallestBranch)

    def max_value (board,player):
        if (' ' not in board) or utility(board) != 0:
            return utility(board, other(player))
        largestBranch = -2
        for move in possible_moves:
            tempValue = min_value(make_move(board,move,enemy),ally)
            if tempValue > largestBranch:
                largestBranch = tempValue
        return(largestBranch)

    all_moves = []
    all_results = []
    for move in possible_moves:
        current = []
        all_results.append(max_value(make_move(board,move,ally),enemy))
        all_moves.append(move)
    print all_moves
    print all_results
    return all_moves, all_results

def run (str,player,playX,playO): 

    board = create_board(str)

    print_board(board)
    draw_board(board)
    while not done(board):
        if player == 'X':
            move = playX(board,player)
        elif player == 'O':
            move = playO(board,player)
        else:
            fail('Unrecognized player '+player)
        board = make_move(board,move,player)
        print_board(board)
        draw_board(board)
        player = other(player)

    winner = has_win(board)
    if winner:
        print winner,'wins!'
    else:
        print 'Draw'
        
def draw_board(board):
    c = Rectangle(Point(20,20), Point(230, 230))
    c.setFill("dark grey")
    c.draw(WIN)

    for i in range(0,4):
        for j in range(0,4):
            c = Rectangle(Point(i*50+30,j*50+30),Point(i*50 +70,j*50 +70))   
            c.setFill("white")
            c.draw(WIN)

            if board[(j)*4+i] != ".":
                d = Text(Point(i*50+50, j*50+50),board[(j)*4+i])
                d.setFill("black")
                d.draw(WIN)

def main ():
    run('.' * 16, 'X', wait_player_input, computer_move)
    # run('.' * 16, 'X', read_player_input, computer_move)

PLAYER_MAP = {
    'human': wait_player_input,
    # 'human': read_player_input,
    'computer': computer_move
}

if __name__ == '__main__':

  try:
      str = sys.argv[1] if len(sys.argv)>1 else '.' * 16
      player = sys.argv[2] if len(sys.argv)>3 else 'X'
      playX = PLAYER_MAP[sys.argv[3]] if len(sys.argv)>3 else wait_player_input
      # playX = PLAYER_MAP[sys.argv[3]] if len(sys.argv)>3 else read_player_input
      playO = PLAYER_MAP[sys.argv[4]] if len(sys.argv)>4 else computer_move

  except:
    print 'Usage: %s [starting board] [X|O] [human|computer] [human|computer]' % (sys.argv[0])
    exit(1)
  run(str,player,playX,playO)
