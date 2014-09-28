#!/usr/bin/env python
# 

#
# Game Programming, Level 2 Project
#
# TIC-TAC-TOE 4
#
# A simple strategy game, an extension of the standard 3x3 tic-tac-toe
#

import sys

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
    if board[(y-1)*4+x-1] == ".":
        return False
    else:
        return board[(y-1)*4+x-1]
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
        move = raw_input('(1-4,1-4): ')
        if move == 'q':
            exit(0)
        if len(move)>0 and ((int(move[3])-1)*4+int(move[1])-1) in valid:
            return (int(move[3]),int(move[1]))

def make_move (board,move,player):
    new_board = board[:]
    new_board[(move[1]-1)*4+move[0]-1] = player
    return new_board

def computer_move (board,player):
    return (2,2)


def other (player):
    if player == 'X':
        return 'O'
    return 'X'


def run (str,player,playX,playO): 

    board = create_board(str)

    print_board(board)

    while not done(board):
        if player == 'X':
            move = playX(board,player)
        elif player == 'O':
            move = playO(board,player)
        else:
            fail('Unrecognized player '+player)
        board = make_move(board,move,player)
        print_board(board)
        player = other(player)

    winner = has_win(board)
    if winner:
        print winner,'wins!'
    else:
        print 'Draw'
        
def main ():
    run('.' * 16, 'X', read_player_input, computer_move)


PLAYER_MAP = {
    'human': read_player_input,
    'computer': computer_move
}

if __name__ == '__main__':

  try:
      str = sys.argv[1] if len(sys.argv)>1 else '.' * 16
      player = sys.argv[2] if len(sys.argv)>3 else 'X'
      playX = PLAYER_MAP[sys.argv[3]] if len(sys.argv)>3 else read_player_input
      playO = PLAYER_MAP[sys.argv[4]] if len(sys.argv)>4 else computer_move
  except:
    print 'Usage: %s [starting board] [X|O] [human|computer] [human|computer]' % (sys.argv[0])
    exit(1)
  run(str,player,playX,playO)


