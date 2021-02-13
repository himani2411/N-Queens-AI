#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [HIMANI ANIL DESHPANDE AND HDESHPA@IU.EDU]
#
# Based on skeleton code in CSCI B551, Spring 2021
#


import sys
#import pdb


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
# Adding condition for checking the diagonal condition for extraCredit
# Adding the function call for checking if we can add the pichu at a given position
# Added diagonalFlag to check for extraCredit Functionality
def add_pichu(board, row, col, diagonalFlag):

    checkCostForDiag = 0
    checkcostforrowCol = 0

    #Extra Credit
    if diagonalFlag == 1:
        checkCostForDiag = safe_to_place_diagoally(board, row, col)

    # No need to check if refused by diagonal checks for extra credit
    # We will always check the row and column condition as the parameter will always be initialized as 0 when number
    # of pichus is not 0
    if checkCostForDiag == 0:
        checkcostforrowCol = safe_to_place_pichus_in_rows_cols(board, row, col)

    # If the sum is 0 then we can add the pichu as we will get >0 only if we encountered a pichu
    if (checkcostforrowCol + checkCostForDiag == 0):
        return board[0:row] + [board[row][0:col] + ['p', ] + board[row][col + 1:]] + board[row + 1:]
    else:
        return board

# Function checks if it is safe to place the pichu in index (row,col) of the board.
# So searching only the row and column that is given as a parameter, to decide if a pichu can be added.
# We do this by keeping 4 variables which will indicate if 1 that a pichu was found and hence not safe to add at the position (row,col)
def safe_to_place_pichus_in_rows_cols(board, row, col):
    # check for pichus in a col and rows

    countinRowfromStart = 0
    countInaRowTillEnd = 0

    countColfromStart = 0
    countColTillEnd = 0

    # Keeping row same and checking till the column index (So till end index point)
    # So scanning the rows from left end of the board to the points position(excluding the point)
    for i in range(0, col, 1):
        if board[row][i] == '@' or board[row][i] == 'X':
            countinRowfromStart = 0
        if board[row][i] == 'p':
            countinRowfromStart = 1

    # Keeping the row same and checking the column from end of the board to the given value
    # So scanning the rows from right end of the board to the points position(excluding the point)
    for j in range(len(board[0]) - 1, col, -1):
        if board[row][j] == '@' or board[row][j] == 'X':
            countInaRowTillEnd = 0
        if board[row][j] == 'p':
            countInaRowTillEnd = 1

    # Keeping the Column same and checking the Column from 0 to given value
    # So scanning the columns from top end of the board to the points position(excluding the point)
    for k in range(0, row, 1):
        if board[k][col] == '@' or board[k][col] == 'X':
            countColfromStart = 0
        if board[k][col] == 'p':
            countColfromStart = 1

    # Keeping the Column index same and checking the columns from end of the board to the given row value
    # So scanning the columns from bottom end of the board to the points position(excluding the point)
    for l in range(len(board) - 1, row, -1):
        if board[l][col] == '@' or board[l][col] == 'X':
            countColTillEnd = 0
        if board[l][col] == 'p':
            countColTillEnd = 1

        #If the sum is 0 then we can add the pichu as we will get >0 only if we encountered a pichu
    return countinRowfromStart + countInaRowTillEnd + countColfromStart + countColTillEnd

#Checking all the diagonals that a node or position can have.
# Keeping track of this by keeping 4 variables to track the four different direction.
# We keep this variable as 1 then it indicates that we found a pichu and its not safe to add any pichu to the position.
# Found the diagonal looping from https://www.geeksforgeeks.org/python-program-for-n-queen-problem-backtracking-3/
def safe_to_place_diagoally(board, row, col):
    checkfortopDiagForw = 0
    checkfortopDiagback = 0
    checkfordownDiagback = 0
    checkfordownDiagForw = 0

    # This works for forward Movement of top left to bottom right
    for i, j in zip(range(row + 1, len(board), 1),
                    range(col + 1 , len(board[0]), 1)):

        if board[i][j] == 'p':
            checkfortopDiagForw = 1

    # This works for backward Movement of top left to bottom right
    for i, j in zip(range(row -1 , -1, -1),
                    range(col -1, -1, -1)):
        if board[i][j] == 'p':
            checkfortopDiagback = 1

    # This Code works for backward movement of bottom left to top right
    for i, j in zip(range(row + 1, len(board), 1),
                    range(col - 1, -1, -1)):
        if board[i][j] == 'p':
            checkfordownDiagback = 1

    # This Code works for forward movement of bottom left to top right
    for i, j in zip(range(row - 1, -1, -1),
                    range(col + 1, len(board[0]), 1)):
        if board[i][j] == 'p':
            checkfordownDiagForw = 1

        # If the sum is 0 then we can add the pichu as we will get >0 only if we encountered a pichu
    return checkfortopDiagback + checkfortopDiagForw + checkfordownDiagForw + checkfordownDiagback


# Get list of successors of given board state. Added diagonalFlag to check for extraCredit Functionality
def successors(board, diagonalFlag):
    try:
        return [add_pichu(board, r, c, diagonalFlag) for r in range( 0,len(board), 1) for c in range( 0,len(board[0]),1) if board[r][c] == '.']
    except IndexError as ie:
        print("Exception ", str(ie) , "occured")
    except TypeError as te:
        print("Exception ", str(te), "occured")
    except AttributeError as ae:
        print("Exception ", str(ae), "occured")
    except Exception as e:
        print("Exception ", str(e), "occured")

# check if board is a goal state
def is_goal(board, k):
    return count_pichus(board) == k


def check_valid_map(initial_board):

    for r in range(0,len(initial_board)):
            for c in range(0,len(initial_board[0])):
                if initial_board[r][c] not in '.p@X':
                    raise Exception('Found Invalid Character in map at location  (%d ,%d)' % (r,c))
                    return False


    return True


# Solving Extra Credit by doing the same thing that we do in the original solve code except for k and diagonal Flag.
# Adding diagonal Flag which specifies that if 1 then check for diagonal.

def extra_credit(initial_board, k, diagonalFlag):
    fringe = [initial_board]

    visited = []

    while len(fringe) > 0:

        for s in successors(fringe.pop(), diagonalFlag):  # Used DFS algorithm
            if is_goal(s, k):
                return (s, True)
            else:
                if s not in visited:
                    visited.append(s)
                    fringe.append(s)

    return ([], "None")

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_map, success), where:
# - new_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_board, k):


    try:
        if isinstance(k,int):

            if check_valid_map(initial_board):
                diagonalFlag = 0
                fringe = [initial_board]
                visited = []
                if k == 0:
                    diagonalFlag = 1
                    #Solving once to get success as True and run the below while loop
                    (extraCreditboard, success) = solve(house_map, k + 1)

                    while success == True:
                        # if k==5 :
                        #     pdb.set_trace()  #For resolving extra Credit Didnt work
                        k = k + 1
                        #There will be an instance of k for which the success will be false and we will get out of the loop
                        (extraCreditboard, success) = extra_credit(initial_board, k, diagonalFlag)

                    #Once we are out of the loop, we solve for the last instance for which the extracredit solution was true
                    (extraCreditboard, success) = extra_credit(initial_board, k - 1,diagonalFlag)

                    return (extraCreditboard, success)


                elif k > 0:
                    while len(fringe) > 0:
                        for s in successors(fringe.pop(),diagonalFlag):
                            if is_goal(s, k):
                                return (s, True)
                            else:
                                # Adding the board in Fringe only if it has not been visited before
                                if s not in visited:
                                    visited.append(s)
                                    fringe.append(s)
                # elif k < 0:
                #     print("Please provide a valid non-negative number ")
        else:
            raise Exception (" Please Provide numbers")
    except AttributeError as ae:
        print("A ", str(ae), " exception occurred")
    except ValueError as ve:
        print("A ", str(ve), " exception occurred")
    except TypeError as te:
        print("A ", str(te), " exception occurred")
    except IndexError as ie:
        print("A ", str(ie), " exception occurred")
    except Exception as e:
            print("A ",str(e)," exception occurred")
    return ([], "None")



# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
try:
    # This is K, the number of agents
    k = int(sys.argv[2])
    print(house_map, "Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    (newboard, success) = solve(house_map, k)

    print(printable_board(newboard))
    print(success)
except Exception as e:
    print("Exception ", str(e))
