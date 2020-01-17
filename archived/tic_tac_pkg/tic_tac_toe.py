# tic_tac_toe.py
# code for in/out of game board

import random

from game_states import output_visualboard
from game_states import output_gameboard
from game_states import user_logic
from minimax import minimax
from minimax import best_move


#Run Code in Terminal: python tic_tac_toe.py
#TODO: Logic for computer is not yet set up


# gamePrompt: String - prompt user & demonstrate how to chose their next or current move
gamePrompt = """\nIt is your turn! Please choose 1-9 
x: computer
o: player\n

             1 | 2 | 3
             4 | 5 | 6
             7 | 8 | 9\n"""

gameboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
visualGameboard = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
gameHasEnded = False


# coinToss - Determines who has the initial turn between player & computer
coinToss = random.randint(1,2)
if coinToss == 1:
    computerTurn = True
else:
    computerTurn = False



while gameHasEnded == False:


    if computerTurn == False:
        print(gamePrompt)

        print("Game board:\n")
        output_gameboard(gameboard)

        print("Visual board:")
        output_visualboard(visualGameboard)

        computerTurn = True
        playerChoice = int(input("\nEnter your move (1-9): "))
        user_logic(gameboard, visualGameboard, playerChoice)



    else:
        computerTurn = False
        x, y = best_move(gameboard)
        visualGameboard[x][y] = "x"



    if gameHasEnded == True:
        break













