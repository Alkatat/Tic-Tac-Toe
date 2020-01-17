# Tic Tac Toe
We will be creating a Tic Tac Toe game where the player versus an AI. 
``We will be utilizing minimax alpha-beta pruning with a closest-to-winning Heuristic to achieve this.``

A heuristic board evaluation function was used to evaluate the positions, idea based on [NTU case study](https://www.ntu.edu.sg/home/ehchua/programming/java/javagame_tictactoe_ai.html#zz-1.3).
The board evaluation function assigns weight based on how close the opponent and computer is to a win.
* +/- 1000 indicates three in same line -> a win
* +/- 100 indicates two in same line
* +/- 10 indicates 1 in a line
* +/- 1 indicates

The evaluation function is a summation of the "closeness" each player is to the 8 possible win states.


# Developers
1. Mustafa Al-Katat (Manager)
   1. Made a Taco
   1. Project Planning and Organization
   1. Heuristic Evaluation Code
2. Bradley Dodds (Reflector)
   1. Ate a Taco
   1. Game State Code
   1. Documentation
3. Jeffery Lo(Presenter)
   1. Trashed a Taco
   1. Basic Game I/O, Printing, and Board Win Recognition
   1. Documentation
1. Taco (Recorder)
   1. Bought
   2. Half eaten
   3. Discarded 
   
# Technical implementation

## Data Structures
* Graph Data Structure for Game States

## Algorithms
* MinMax and Alpha-Beta Pruning Algorithms for AI Decisions
  * helpful link - [geeksforgeeks: alpha-beta pruning](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)

## Language
* Python 3.6

## Dependencies
* Numpy - ``pip3 install numpy``
  * used for board data structure and heuristic evaluation

# Development
## Helpful Links
* File Structure: 
  * https://stackoverflow.com/questions/43635209/how-to-link-multiple-python-classes-in-a-separate-main-python-file
## Milestone 1
* Finish ReadME
* Establish Heuristic, Algorithms, Data Structures
## Milestone 2
* Basic Board I/O
* Recognition of Win States to End Game
* State Space Data Structure
* Delayed due to discussions of which heuristic to use and related alogirthm: min max vs alpha beta pruning.
  * State Heuristic Evaluation
  * Min-Max Algorithm Implementation
## Milestone 3
* Couple together Features
* Allow Options for who starts
   * Adjust Max/Min for AI depending on who starts



# Usage
* From project root directory run main.py -- ```python3 main.py```
