# Scotty Dog Starter File

# NOTE: You can run this file locally to test if your program is working.

#=============================================================================

# INPUT FORMAT: board

# board: A 15 x 15 2D array, where each element is:
#   0 - an empty square
#   1 - the current position of Scotty
#   2 - a naturally generated barrier
#   3 - a player placed barrier

# Example Input:

# board: See "SAMPLE_BOARD" below.

#=============================================================================

# OUTPUT FORMAT when scotty_bot is called:

# A list of two integers [dx, dy], designating in which
# direction you would like to move. Your output must satisfy

# -1 <= dx, dy <= 1

# and one of the following, where board[y][x] is Scotty's current position:

# max(x + dx, y + dy) >= 15 OR min(x + dx, y + dy) < 0 (move off the board)
# OR
# board[y + dy][x + dx] < 2 (move to an empty square or stay still)

# Invalid outputs will result in Scotty not moving.

#=============================================================================

# OUTPUT FORMAT when trapper_bot is called:

# A list of two integers [x, y], designating where you would
# like to place a barrier. The square must be currently empty, i.e.
# board[y][x] = 0

# Invalid outputs will result in no barrier being placed.

### WARNING: COMMENT OUT YOUR DEBUG/PRINT STATEMENTS BEFORE SUBMITTING !!!
### (this file uses standard IO to communicate with the grader!)

#=============================================================================

# Write your bots in the scotty_bot and trapper_bot classes. Helper functions
# and standard library modules are allowed, and can be written before/inside
# these classes.

# You can define as many different strategies as you like, but only the classes
# currently named "scotty_bot" and "trapper_bot" will be run officially.


# Example Scotty bot that makes a random move:
import random

class scotty_bot:
    
    def __init__(self):
        # You can define global states (that last between moves) here
        pass

    def find_scotty(self, board):
        # Helper function that finds Scotty's location on the board
        for y in range(15):
            for x in range(15):
                if board[y][x] == 1:
                    return (x, y)
    

    def exitPoints():
      availablePoints = []
      #searches top row for exit points
      for t in range(15):
        if (board[0][t] == 0):
          availablePoints.append(0,t)
      #searches bottom row for exit points
      for b in range(15):
        if board[14][t] == 0:
          availablePoints.append(14,t)
      #searches leftmost column for exit points
      for l in range(15):
        if board[t][0] == 0:
          availablePoints.append(t,0)
      #searches rightmost column for exit points
      for r in range(15):
        if board[t][14] == 0:
          availablePoints.append(t,14)
      return availablePoints

    def move(self, board):
        # You should write your code that moves every turn here
        
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                 (1, 1), (1, 0), (1, -1), (0, -1)]
        x, y = self.find_scotty(board)
        while moves:
            dx, dy = moves.pop(random.randrange(len(moves)))
            if max(x + dx, y + dy) >= 15 or min(x + dx, y + dy) < 0:
                return (dx, dy)
            elif board[y + dy][x + dx] == 0:
                return (dx, dy)
        return (0, 0)

# Example trapper bot that places a barrier randomly:

class trapper_bot:

    def __init__(self):
        # You can define global states (that last between moves) here
        pass
    
    def move(self, board):
        # You should write your code that moves every turn here
        moves = [(x, y) for x in range(15) for y in range(15)]
        while moves:
            x, y = moves.pop(random.randrange(len(moves)))
            if board[y][x] == 0:
                return (x, y)
        return (0, 0)

#=============================================================================

# Local testing parameters

# If you would like to view a turn by turn game display while testing locally,
# set this parameter to True

LOCAL_VIEW = True

# Sample board your game will be run on (flipped vertically)
# This file will display 0 as ' ', 1 as '*', 2 as 'X', and 3 as 'O'

SAMPLE_BOARD = [
    [0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 0, 0, 2, 2, 2],
    [0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 2, 0, 0, 2, 0, 2, 2, 0, 0, 2, 0, 2, 0, 2],
    [0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2],
    [0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 2, 0, 2, 2, 2, 0, 2, 0, 0],
    [2, 2, 0, 2, 2, 2, 0, 1, 0, 0, 2, 0, 0, 2, 0],
    [2, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0],
    [2, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 2],
    [0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0]]

#=============================================================================












































# You don't need to change any code below this point

import json
import sys

def WAIT():
    return json.loads(input())

def SEND(data):
    print(json.dumps(data), flush=True)

def dispboard_for_tester(board):
    print()
    print('\n'.join(''.join(map(lambda x:' *XO'[x],i))for i in reversed(board)))
    print()

def find_scotty_for_tester(board):
    for y in range(15):
        for x in range(15):
            if board[y][x] == 1:
                return (x, y)

def trapped_for_tester(board):
    pos = find_scotty_for_tester(board)
    moves = [*zip([0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1])]
    trap = True
    for i in moves:
        if 0 <= pos[0] + i[0] < 15 and 0 <= pos[1] + i[1] < 15:
            if board[pos[1] + i[1]][pos[0] + i[0]] == 0:
                trap = False
                break
        else:
            trap = False
            break
    return trap

def PLAY(scotty, trapper, board):
    result = -1
    while True:
        try:
            val = trapper.move(board)
            if not (val[0] == int(val[0]) and 0 <= val[0] < 15
                and val[1] == int(val[1]) and 0 <= val[1] < 15
                and board[val[1]][val[0]] == 0):
                raise Exception('invalid move')
            board[val[1]][val[0]] = 3
        except Exception as e:
            print(f'Your trapper has an error: {e}! Doing nothing instead.')
            val = -1
        if trapped_for_tester(board):
            result = 1
            break
        if LOCAL_VIEW:
            dispboard_for_tester(board)
            input("Enter to continue (change LOCAL_VIEW to toggle this)")
        try:
            val = scotty.move(board)
            if not (val[0] == int(val[0]) and -1 <= val[0] <= 1
                and val[1] == int(val[1]) and -1 <= val[1] <= 1):
                    raise Exception('invalid move')
        except Exception as e:
            print(f'Your Scotty has an error: {e}! Doing nothing instead.')
            val = (0, 0)
        pos = find_scotty_for_tester(board)
        if 0 <= pos[0] + val[0] < 15 and 0 <= pos[1] + val[1] < 15:
            if board[pos[1] + val[1]][pos[0] + val[0]] == 0:
                board[pos[1] + val[1]][pos[0] + val[0]] = 1
                board[pos[1]][pos[0]] = 0
        else:
            board[pos[1]][pos[0]] = 0
            result = 0
            break
        if LOCAL_VIEW:
            dispboard_for_tester(board)
            input("Enter to continue (change LOCAL_VIEW to toggle this)")
    print(["Scotty", "Trapper"][result], "won!")
    if not LOCAL_VIEW:
        print("Change LOCAL_VIEW to True to see a turn by turn replay")

if len(sys.argv) < 2 or sys.argv[1] != 'REAL':
    PLAY(scotty_bot(), trapper_bot(), SAMPLE_BOARD)
    input()

else:
    scotty = scotty_bot()
    trapper = trapper_bot()
    while True:
        data = WAIT()
        board = data["board"]
        role = data["role"]
        if role == "trapper":
            SEND(trapper.move(board))
        else:
            SEND(scotty.move(board))