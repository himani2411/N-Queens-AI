##### **Report**

###### **Part 1:Route Pichus**


 
 **State Space:**
 The state space is the number of '.' on which the pichus can be placed. So according to map.txt the state space is 26 and according to map2.txt the state space is 26 as well.
 
 **Initial State:**
 The Initial state of the search abstraction is the map that we gave when we are running and testing the code. Also, only one single pichu is part of the map.
 We can assume that there is always exactly one p and one @ in the map.
 
 **Goal State:**
 The goal state of route pichu is "@". We have to find the shortest route or path from the agent(pichu) to me(@ position in the map).
 The shortest path should be provided using (L, R, D, and U for left, right, down, and up) from the picchu's position in the map(i.e agents position to the @ position)
 
 **Successor Function:**
 The successor function is the moves function, which provides all the moves that the pichu can make in the four principal compass directions
  (L, R, D, and U for left, right, down, and up). This function also checks if the above four moves are valid or not and returns only those which are valid and safe.
   This is done by calling the valid_index function, which will check if we are inside or on the boundary of the map. 
 
 
 **Search Function:**
 The function follows the BFS Search algorithm where we have used LIFO i,e stack for storing 3 parameter; our current move, the distance from agent till the goal state and
 the path or route
		
		
**Cost Function:**
I have kept the cost of moving from one location to its immediate neighbouring location as uniform. So, if the agent moves in any of the four directions the cost will increase by one.
		
		
**Search Strategy:**

I am checking if the map contains any invalid characters. Nothing other that '.', 'p', '@' and 'X' should be in the map. If we get an invalid map,
I have raised an exception specifying the location where I found the invalid character. 
If the map is valid, I get the Pichu location (initial Location) and then create a fringe, which is a queue, implemented using List for First In First out (FIFO) functionality.
So, the BFS algorithm is used to find the shortest path from initial to goal state.
The fringe is maintaining 3 different parameters for every move. 

`->`The move itself, 

`->`The distance of the move from the initial state 

`->`The route of the move from the initial state to itself.

The **find_route()** is used for comparing the previous move and the current moves,
The column index remains the same when we are moving up and down,  we check the row index to find if we have moved from up or down.
if the row index is "-1" from the previous moves's row index it means we have moved "Up"
if the row index is "+1" from the previous moves's row index it means we have moved "Down"

And similarly the row index remains the same when we are moving left and right.
Then we check the column index, if the column index is -1 from the previous move then we have moved "Left"
if column index is +1 from the previous moves column index then we have moved "Right"

The program will pop the fringe and will do so till its empty. Immediately I add the node(move) into the visited fringe
The program then calls the successor function, where we are moving up, down, left and right and only if we are inside or on the boundary of the map.
So if an agent is inside the map then I will have four valid moves. If the agent is on the boundary of the map it will have 3 valid moves. If an agent is at any corner location it will have only 2 moves. These moves will get reduced depending if there are any obstacles(X) in any of the successor moves. We will not consider the Obstacle successor move as it we will not be able to move in that direction.

We loop through all the  valid successors of every node we visit. So we are visiting the child nodes and checking if they are goal states.
Once we reach a goal state we return the distance and the route we took for reaching it from the start state.
If we don't get any goal state then we keep on looping till we reach one. We keep doing this till the fringe is empty.

If we don't reach the goal state the response we send is "-1"

######  **Part 2: Arrange Pichus and Extra Credit**
**State Space:**
The state space is the number of '.' on which the pichus can be placed. So according to map.txt the state space is 26 and according to map2.txt the state space is 26 as well.

**Initial state**
 The Initial state of the search abstraction is the map that we gave when we are running and testing the code. Also, only one single pichu is part of the map.
 We can assume that there is always exactly one p and one @ in the map.
	
**Goal State:**	
The goal state for arrange pichus is such that we have to arrange all the pichus which has been given as a runtime argument. 
The arrangement has to follow a below constraints

`->` Two or Pichus need to have and X or @ between them

`->` The above condition should be applied when the pichus are in a row as well as columns.

So the goal state will be when the new map will have the same number of pichu's as given during runtime.
We have to return the new map in which all the pichus are placed without violating each other. If this cannot be arranged we give the response as "None"

**Successor Function:**
The successor function is the one giving me boards where the pichu at any location is not violating another pichu.
Two pichus in a row or column cannot have only a succession of '.' between them.
Two or more pichus need and X or @ between them for them to be in valid state.

The cost of moving from one node to another node in a board has been kept uniform.


**Strategy**
In the solve function, we check if the input (K) is an integer. If it is not we are raising an exception
If K is an integer, we are checking if the map given during the runtime is a valid map. It should have only ".", "p", "@" and "X" characters.
I have kept diagonalFlag, for extra credit functionality, initialized to 0. 

`->`diagonalFlag = 0 means that we are not going to do the extraCredit Functionality

`->`diagonalFlag = 1 means we are going to do the extra credit functionality


Our Fringe is a stack of boards. We are looping through this fringe till it's empty.
We are keeping track of the visited boards as well.
I am looping through all the successor boards. The successor is looping through the board passed to it and then finding the “.” position and sending this position to add_Pichu,
which is adding the pichu to the board and sending this new board.

In add_pichu, **I have called safe_to_place_diagonally function only if diagonalFlag = 1**
Otherwise, I am only calling safe_to_place_pichus_in_rows_cols, which is scanning the row and column of the position I have given to check if it has any Pichus. 
So from the point or location, we are scanning up, down, left and right for that point’s row and column and not all the rows and columns. 
So, basically scanning looks like a “+” when the point is inside the map. At the corner locations of the map it looks like and L.

If I find a pichu, I have kept a variable which will be either 1 or 0
1 specifies that we have a pichu and 0 specifies that we have an “X” or “@”
At the end I need a sum of 0 form all the direction, so to specify that I did not find any other pichus violating that position. 
And therefore, it will be safe for me to add the pichu in that location.
If **The diagonalFlag == 1 means I have to check if the diagonals are safe for a pichu to be added.**
So I scan the diagonals of the position as I did the rows. If the position is at the middle of the map then the scanning looks like and X. 
So I scan the diagonals in all the four directions and if I get any pichu I keep the variable as 1.
If at the end I get the sum of these 4 variables as 0, it means no pichu was encountered and it’s safe to add the pichu there.


I am checking if k > 0, which is part 2 where only rows and columns are checked.
We are looping through all the boards that we got as successors. 
If they do not have the number of pichus mentioned during the runtime then we keep on looping till we empty the fringe.
We keep adding the successor boards,which have not been visited,  in the fringe as well as visited.
If the fringe is empty and we haven't reached the goal state then we return “None”
If we reach the goal state we return the board which is the goal board.


****_I am checking if k == 0, which is extra credit functionality_****

We have kept the diagonal Flag as 1.
We increase K to 1 and call the solve (itself) again. 
If I get success for adding even one Pichu, I will be able to loop and call the extraCredit() function which behaves the same as the when K !=0 in terms of fringe and calling the other functions.
However, the only difference is the diagonal flag is 1 and so as explained above we will check the diagonals.

We keep on incrementing the k value till we get a false and we call the same function to get the 
Board with k-1 value.

__What am I proud of?__
 
`->`I could understand and even code in Python.

`->`I tried a different approach of doing arrange pichus where I was trying to find valid boards. However, I changed the approach and was able to do the extra credit as well.






**Citations:**
_For looping through diagonally for Extra Credit_
https://www.geeksforgeeks.org/python-program-for-n-queen-problem-backtracking-3/


_For Exception Handling:_
https://wiki.python.org/moin/HandlingExceptions
https://www.programiz.com/python-programming/exception-handling


