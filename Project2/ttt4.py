#!/usr/bin/env python
# 

#
# Game Programming, Level 2 Project
#
# TIC-TAC-TOE 4
#
# A simple strategy game, an extension of the standard 3x3 tic-tac-toe

# Thomas Chen + Jazmin Gonzalez-Rivero

# Note: Program always picks the first "best move", meaning it does not take number of moves to the win into account.
# This can lead to it ignoring an instant win but winning a few turns later.

# The program caches boards and all their rotations as it comes across them, so the first move takes the longest.
# The computer takes about four minutes to make its first move on our laptops since it's caching every single board
# Following computer moves are pretty fast since it's just looking up the move

# Requires you to specify a board if you want to change the first player or player mapping

from graphics import *
import sys
import cProfile
WIN = GraphWin("4x4 TicTacToe", 400, 400)
import math 
KNOWN_STATUS = {}

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
            if letter != '.' and letter != 'X' and letter != 'O':
                sys.exit("Invalid symbol on board, please re-input values.")
            else:
                board.append(letter)
    else:
        sys.exit("That is not a valid board, please re-input values.")
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
    while True:
      point = WIN.getMouse()
      try:
        pos = board[(point.getY())/100*4 + (point.getX())/100]
        if pos == ".":
            return ((point.getY())/100*4 + (point.getX())/100)
      except:
        continue


def make_move (board,move,player):
    new_board = board[:]
    new_board[move] = player
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

def possible_moves (board):
    return [i for (i,e) in enumerate(board) if e == '.']

def utility (board,player1, player2):
    if has_win(board) == player1:
        return -1
    if has_win(board) == player2:
        return 1
    elif has_win(board) == False:
        return 0

def min_max(board,player):
    current = []

    ally = player
    enemy = other(player)   
    
    def rotateSave(board, branch):
        boardString = "".join(board)
        testboard1 = []
        testboard2 = []
        testboard3 = []
        small = min(branch)
        large = max(branch)
        for i in range(0,16):
            testboard1.append(board[int(16 - (4 * ((i%4)+1)) + math.floor(i/4))])
            testboard2.append(board[int((4 * ((i%4)+1)) - (math.floor(i/4)+1))])     
            testboard3.append(board[int(15 - i)])
        KNOWN_STATUS["".join(testboard1)] = (small, large)
        KNOWN_STATUS["".join(testboard2)] = (small, large)
        KNOWN_STATUS["".join(testboard3)] = (small, large)
        KNOWN_STATUS[boardString] = (small, large)

    def min_value (board):
        boardString = "".join(board)
        if boardString in KNOWN_STATUS:
            s,l = KNOWN_STATUS[boardString]
            return s
        if ('.' not in board) or utility(board, ally, enemy) != 0:
            return utility(board,ally, enemy)
        smallestBranch = []
        for move in possible_moves(board):
            smallestBranch.append(max_value(make_move(board,move,ally)))
        rotateSave(board,smallestBranch)
        return min(smallestBranch)

    def max_value (board):
        boardString = "".join(board)
        if boardString in KNOWN_STATUS:
            s,l = KNOWN_STATUS[boardString]
            return l
        if ('.' not in board) or utility(board, ally, enemy) != 0:
            return utility(board, ally, enemy)
        largestBranch = []
        for move in possible_moves(board):
            largestBranch.append(min_value(make_move(board,move,enemy)))
        rotateSave(board, largestBranch)
        return max(largestBranch)

    all_moves = []
    all_results = []
    for move in possible_moves(board):
        current = []
        all_results.append(max_value(make_move(board,move,ally)))
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
            sys.exit('Unrecognized player '+player)
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
    # c = Rectangle(Point(0,0), Point(210, 210))
    # c.setFill("dark grey")
    # c.draw(WIN)
    for i in range(0,4):
        for j in range(0,4):
            c = Rectangle(Point(i*100,j*100),Point(i*100 +100,j*100 +100))   
            c.setFill("white")
            c.draw(WIN)

            if board[(j)*4+i] != ".":
                d = Text(Point(i*100+50, j*100+50),board[(j)*4+i])
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
      str = sys.argv[1].upper() if len(sys.argv)>1 else '.' * 16
      player = sys.argv[2] if len(sys.argv)>3 else 'X'
      playX = PLAYER_MAP[sys.argv[3]] if len(sys.argv)>3 else wait_player_input
      # playX = PLAYER_MAP[sys.argv[3]] if len(sys.argv)>3 else read_player_input
      playO = PLAYER_MAP[sys.argv[4]] if len(sys.argv)>4 else computer_move

  except:
    print 'Usage: %s [starting board] [X|O] [human|computer] [human|computer]' % (sys.argv[0])
    exit(1)
  # cProfile.run('r un(str,player,playX,playO)')
  run(str,player,playX,playO)
