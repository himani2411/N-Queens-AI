#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code in CSCI B551, Spring 2021
#


import sys


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Count total # of pichus on board
def count_pichus(board):
    return sum([row.count('p') for row in board])


# Return a string with the board rendered in a human-pichuly format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])


# Add a pichu to the board at the given position, and return a new board (doesn't change original)
def add_pichu(board, row, col, diagonalFlag):
    # print("row ", row, "column ", col)
    # print ("Add Pichu 1st part",board[0:row] )
    # print ("Add Pichu 2nd part",[board[row][0:col] + ['p',] + board[row][col+1:]] )
    # print ("add 3rdpart ",board[row+1:])
    checkCostForDiag = 0
    checkcostforrowCol = 0
    if diagonalFlag == 1:
        checkCostForDiag = safe_to_place_diagoally(board, row, col)

    if checkCostForDiag == 0: #No need to check if refused by digonal checks
        checkcostforrowCol = safe_to_place_pichus_in_rows_cols(board, row, col)

    if (checkcostforrowCol + checkCostForDiag == 0):
        return board[0:row] + [board[row][0:col] + ['p', ] + board[row][col + 1:]] + board[row + 1:]
    else:
        return board

def safe_to_place_pichus_in_rows_cols(board, row, col):
    # check for pichus in a col and then inside rows
    #         count_rowWise= 0
    #         count_colWise = 0

    countinRowfromStart = 0
    countInaRowTillEnd = 0

    countColfromStart = 0
    countColTillEnd = 0

    # Keeping row same and checking till the Column value given
    for i in range(0, col, 1):
        if board[row][i] == '@' or board[row][i] == 'X':
            countinRowfromStart = 0
        if board[row][i] == 'p':
            countinRowfromStart = 1

    # Keeping the row same and checking the column from given value till end
    for j in range(len(board[0]) - 1, col, -1):
        if board[row][j] == '@' or board[row][j] == 'X':
            countInaRowTillEnd = 0
        if board[row][j] == 'p':
            countInaRowTillEnd = 1

    # Keeping the Column same and checking the Column from 0 to given value
    for k in range(0, row, 1):
        if board[k][col] == '@' or board[k][col] == 'X':
            countColfromStart = 0
        if board[k][col] == 'p':
            countColfromStart = 1

    # Keeping the Column same and checking the columns from 0 to given value
    for l in range(len(board) - 1, row, -1):
        if board[l][col] == '@' or board[l][col] == 'X':
            countColTillEnd = 0
        if board[l][col] == 'p':
            countColTillEnd = 1

    return countinRowfromStart + countInaRowTillEnd + countColfromStart + countColTillEnd


def safe_to_place_diagoally(board, row, col):
    checkfortopDiagForw = 0
    checkfortopDiagback = 0
    checkfordownDiagback = 0
    checkfordownDiagForw = 0

    # This works for forward Movement of top left to bottom right
    for i, j in zip(range(row + 1, len(board), 1),
                    range(col + 1 , len(board[0]), 1)):
        print(" row ", i, "column", j)
        if board[i][j] == 'p':
            checkfortopDiagForw = 1
        if board[i][j] == 'X' or board[i][j] == '@':
            checkfortopDiagForw = 0

    # This works for backward Movement of top left to bottom right
    for i, j in zip(range(row -1 , -1, -1),
                    range(col -1, -1, -1)):
        if board[row][j] == 'p':
            checkfortopDiagback = 1
        if board[row][j] == 'X' or board[row][j] == '@':
            checkfortopDiagback = 0

    # This Code works for backward movement of bottom left to top right
    for i, j in zip(range(row + 1, len(board), 1),
                    range(col - 1, -1, -1)):
        if board[i][j] == 'p':
            checkfordownDiagback = 1
        if board[i][j] == 'X' or board[i][j] == '@':
            checkfordownDiagback = 0

    # This Code works for forward movement of bottom left to top right
    for i, j in zip(range(row - 1, -1, -1),
                    range(col + 1, len(board[0]), 1)):
        if board[i][j] == 'p':
            checkfordownDiagForw = 1
        if board[i][j] == 'X' or board[i][j] == '@':
            checkfordownDiagForw = 0

    return checkfortopDiagback + checkfortopDiagForw + checkfordownDiagForw + checkfordownDiagback


# Get list of successors of given board state
def successors(board, diagonalFlag):
    return [add_pichu(board, r, c, diagonalFlag) for r in range(0, len(board)) for c in range(0, len(board[0])) if
            board[r][c] == '.']


# check if board is a goal state
def is_goal(board, k):
    return count_pichus(board) == k


#
# def safe_to_place(board, row, col):
#     # loop for rows of matrix
#     # newboard = board
#     for i in range(0, len(board)):
#
#         # loop for column of matrix
#         for j in range(0, len(board[i]) + 1):
#
#             # loop for comparison and swapping
#             for k in range(len(board[i]) - j - 1):
#
#                 if (board[i][k] == '.' and board[i][k + 1] == 'X'):
#                     #     return False
#                     # if (board[i][j] =='.' and board[i][j+1] == 'X'):
#                     # print("safe to place board\n", printable_board(add_pichu(board, i, k)))
#                     # return add_pichu(board, i, k)
#                     # if (board[k][i] == '.' and board[k+1][i] == 'X'):
#                     print("safe to place board\n", printable_board(add_pichu(board, i, k)))
#                     return add_pichu(board, i, k)
#
# #Test for all the rows and columns of all the boards. So all nodes.
# def safe_to_placeColwise(board, row, col):
#     # loop for rows of matrix
#     # newboard = board
#     flagOne = 0
#     flagTwo = 0
#     for i in range(0, len(board)):
#
#         # loop for column of matrix
#         for j in range(0, len(board[0]) + 1):
#
#             # loop for comparison and swapping
#             for k in range(len(board[0]) - j - 1):
#
#                 if (board[i][k] == '.' and board[i][k + 1] == 'X'):
#
#                     # print("safe to place board\n", printable_board(add_pichu(board, i, k)))
#                     flagOne = 1
#
#                     for l in range(0, len(board)):
#
#                         # loop for column of matrix
#                         for m in range(0, len(board[0]) + 1):
#
#                             # loop for comparison and swapping
#                             for n in range(len(board[0]) - j - 1):
#
#                                 if (board[n][l] == '.' and board[l][k + 1] == 'X'):
#                                     # print("safe to place board\n", printable_board(add_pichu(board, i, k)))
#                                     flagTwo = 1
#                                     # add_pichu(board, i, k)
#                                     print("safe to place board\n", printable_board(add_pichu(board, i, k)))
#
#
#
# #Test for all the rows and columns of all the boards. So all nodes.
# def safe_to_place2(board, row, col):
#     # loop for rows of board
#     # newboard = board
#     for r in range(0, len(board)):
#
#         # loop for column of matrix
#         for c in range(0, len(board[0])):
#             if (board[r][c] == "X"):
#                 add_pichu(board, r, c)
#         # loop for comparison and swapping


# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_map, success), where:
# - new_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_board, k):
    diagonalFlag = 0
    fringe = [initial_board]
    visited = []
    if k == 0:
        diagonalFlag = 1
        while k >= 0:

            while len(fringe) > 0:
                for s in successors(fringe.pop(), diagonalFlag):
                    if is_goal(s, k):
                        print("maximum k is ", k)
                        return (s, True)
                    else:
                        if s not in visited:
                            visited.append(s)
                            fringe.append(s)
                k = k + 1
    else:
        while len(fringe) > 0:
            for s in successors(fringe.pop(),diagonalFlag):
                if is_goal(s, k):
                    return (s, True)
                else:
                    if s not in visited:
                        visited.append(s)
                        fringe.append(s)
    return ([], False)


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])

    # This is K, the number of agents
    k = int(sys.argv[2])
    print(house_map, "Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    # print("safe ","\n",printable_board( add_pichu(house_map,0,0)))

    # for r in range(0, len(house_map)):
    #     for c in range(0, len(house_map[0])):
    #         safe_to_place_diagonally(house_map, r, c)
    (newboard, success) = solve(house_map, k)
    print(printable_board(newboard) if success else "None")
    # if success:
    #     print("Here's what we found:")

    # else:
    #     print(success)
