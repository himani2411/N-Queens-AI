#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [HIMANI ANIL DESHPANDE AND HDESHPA@IU.EDU]
#
# Based on skeleton code provided in CSCI B551, Spring 2021.


import sys
import json

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Return a string with the board rendered in a human/pichu-readable format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

	# Return only moves that are within the board and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]



# Finding the route or path from initial to goal state. We get the route in context to the previous move.
# So if the agent has moved up(U), down(D), left(L) or right(R)
# we are appending the same to the path or route of the previous move and creating a path for the current move.
# Note that the previous move will have its own path or route and we will be appending to it
def find_route(previous_move, curr_move, route):
    if previous_move[0] == curr_move[0]: #rows index is same for left and right
        if previous_move[1] - 1 == curr_move[1]:
            return route + "L"              #Appending to the path
        elif previous_move[1] + 1 == curr_move[1]:
            return route + "R"

    elif previous_move[1] == curr_move[1]:  #Column index is same for up and down move
        if previous_move[0] - 1 == curr_move[0]:
            return route + "U"
        elif previous_move[0] + 1 == curr_move[0]:
            return route + "D"


# Function checks if there are any invalid characters in the map.
# Raises an exception when we find any character which is not '.','p','@' and 'X'
def check_valid_map(house_map):

    for r in range(0,len(house_map)):
            for c in range(0,len(house_map[0])):
                if house_map[r][c] not in '.p@X':
                    raise Exception('Found Invalid Character in map at location  (%d ,%d)' % (r,c))
                    return False


    return True




# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
#    We check if the house map is valid. Get pichu Location i
#   Performing BFS using queue to find the shortest distance between pichu and @.
#   We have used a visited list to implement the queue functionality.

def search(house_map):


    try:
        if check_valid_map(house_map):
            # Find pichu start position
            pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]

            fringe=[(pichu_loc,0,"")] #Keeps tuples of 3 values( node location/position in map, distance from start, path from start
            #Visited list to keep track of the moves we have made
            visited = []


            while fringe:
                    (curr_move, curr_dist,route)=fringe.pop(0) #Used BFS Search algorithm
                    #Adding the  move in visited
                    visited.append(curr_move)
                    #Getting the successor moves
                    for move in moves(house_map, *curr_move):
                            #Checking if we reached goal state
                            if house_map[move[0]][move[1]]=="@":
                                    # Returns a shortest distance and path till the goal state
                                    return (int(curr_dist+1), str(find_route(curr_move,move,route)))
                            else:
                                    #Adding the move in Fringe only if it has not been visited before
                                    if move not in visited:
                                            #Adding the child moves in fringe
                                            fringe.append((move, curr_dist + 1,find_route(curr_move,move,route)))
    except AttributeError as ae:
        print("A ", str(ae), " exception occurred")
    except TypeError as te:
        print("A ", str(te), " exception occurred")
    except IndexError as ie:
        print("A ", str(ie), " exception occurred")
    except Exception as e:
        print("A ", str(e), " exception occurred")

    return (-1,"")

# Main Function
if __name__ == "__main__":
    #try:
        house_map=parse_map(sys.argv[1])
        print("Routing in this board:\n" + printable_board(house_map) + "\n")
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + str(solution[1]))

    # except Exception as e:
    #     print("Exception is ", str(e))
