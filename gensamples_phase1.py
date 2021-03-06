#!/usr/bin/env python3
# Phase 1 of Neural Network sample generation, by making two random number generators compete; stdout should be fed to stdin of second phase sample generation.
import random
import sys

lastColumn = -1
width, height = 7, 6

# board = [[0 for x in range(width)]for y in range (height)]
board = [[0 for y in range(width)] for x in range(height)]


# Matrix positions
# [5][0] [5][1] [5][2] [5][3] [5][4] [5][5] [5][6]
# [4][0] [4][1] [4][2] [4][3] [4][4] [4][5] [4][6]
# [3][0] [3][1] [3][2] [3][3] [3][4] [3][5] [3][6]
# [2][0] [2][1] [2][2] [2][3] [2][4] [2][5] [2][6]
# [1][0] [1][1] [1][2] [1][3] [1][4] [1][5] [1][6]
# [0][0] [0][1] [0][2] [0][3] [0][4] [0][5] [0][6]

# This is the function used to make a move.
# The function recieves the column (that is going to be given by the intelligent algorithm), and the player number that is making the move.
# If the move can't be made, the function returns -1, else: it returns the col in which it was placed.
def place(column, player_number):
    global board, width, height
    if (column >= width or column < 0):
        return -1
    partial_height = height - 1
    while (partial_height >= 0 and board[partial_height][column] == 0):
        partial_height -= 1
    if (partial_height + 1 < height):
        board[partial_height + 1][column] = player_number
        return partial_height + 1
    return -1


# Function used to check whether game has finished or not
# Return values:
# -1 -> game tie
# 0  -> game continues
# 1  -> game won by player_number

# Possible t's:

#   010     111     10      01      100     001     101     101
#   111     010     11      11      010     010     010     010
#                   10      01      101     101     001     100

def gameFinished(player_number):
    global board, width, height
    available_moves = False
    for pos in range(width):
        if (board[height - 1][pos] == 0):
            available_moves = True
            break

    if (checkAnyT(player_number)):
        return 1

    if (not available_moves):
        return -1

    return 0

def genResultMatrix(at):
    retval = [0] * width
    retval[at] = "X"
    return retval

# Function for printing the game board
def printGame():
    global board, width, height, lastColumn
    sys.stdout.write("[")
    for row in range(height - 1, -1, -1):
        for col in range(0, width):
            if col == width - 1 and row == 0:
                sys.stdout.write(str(board[row][col]) + "], " + str(genResultMatrix(lastColumn)))
            else:
                print (board[row][col], end=", ")
    print()

# Function for printing the game board
def printGame2():
    global board, width, height
    for row in range(height - 1, -1, -1):
        for col in range(0, width):
            # if(board[x][y] == 0):
            #   print (" ")
            print (board[row][col], end=" ")
        print ("\n")
    print ("\n")

def checkAnyT(player_number):
    global board, width, height
    for r in range(0, height):
        for c in range(0, width):
            if (board[r][c] == player_number):
                if (checkHorizontal(r, c, player_number)
                    or checkVertical(r, c, player_number)
                    or checkDiagonalLeft(r, c, player_number)
                    or checkDiagonalRight(r, c, player_number):
                    return True
    return False



def checkHorizontal(row, col, player_number):
    global board, width, height
    if (col + 3 >= width): return False
    if (board[row][col + 1] == player_number and board[row][col + 2] == player_number and
            board[row][col + 3] == player_number): return True
    return False

def checkVertical(row, col, player_number):
    global board, width, height
    if (row + 3 >= height): return False
    if (board[row + 1][col] == player_number and board[row + 2][col] == player_number and
            board[row + 3][col] == player_number): return True
    return False

    .
  .
 .
.
def checkDiagonalLeft(row, col, player_number):
    global board, width, height
    if (col + 3 >= width or row + 3 >= height): return False
    if (board[row + 1][col + 1] == player_number and board[row + 2][col + 2] == player_number and
            board[row + 3][col + 3] == player_number): return True
    return False

def checkDiagonalRight(row, col, player_number):
    global board, width, height
    if (col + 3 >= height or row - 3 < 0): return False
    if (board[row - 1][col + 1] == player_number and board[row - 2][col + 2] == player_number and
            board[row - 3][col + 3] == player_number): return True
    return False


def intelligentFunction1(turn, board):
    global lastColumn
    lastColumn = random.randint(0,6)
    return lastColumn


def intelligentFunction2(turn, board):
    global lastColumn
    lastColumn = random.randint(0,6)
    return lastColumn


def main():
    global board
    turn = 1
    loser = 0
    while (gameFinished(turn) == 0):
        printGame()
        if (turn == 1):
            turn = 2
        else:
            turn = 1
        if (turn == 1):
            column = intelligentFunction1(turn, board)
        if (turn == 2):
            column = intelligentFunction2(turn, board)
        if (place(column, turn) == -1):
            loser = turn
            break

    # Game is a tie
    if (gameFinished(turn) == -1): print("USELESS")
    elif not (loser == 0): print ("USELESS")
    else:
        printGame()
        print (turn)


if __name__ == '__main__':
    main()
