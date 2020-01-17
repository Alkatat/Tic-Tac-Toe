import sys
import os


#INPUT: user_logic has 3 parameters:
#Gameboard initial state - use output_gameboard(gameboard) for testing
#[0, 0, 0]
#[0, 0, 0]
#[0, 0, 0]

# gameBoard - current game board representing either a 0, 1, or 2 (0 = empty, 1 = computer, 2 = player)
# visualBoard - represents the visual aspect of the game represented by x or o (x = computer, o = player)
# playerMove - Holds int value 1-9 to determine where the player has chosen the next move to be
def user_logic(gameboard, visualboard, playerMove):

    if playerMove < 4 and gameboard[0][playerMove - 1] == 0:
        gameboard[0][playerMove - 1] = 2
        visualboard[0][playerMove - 1] = "o"

    elif playerMove < 7 and gameboard[1][playerMove - 4] == 0:
        gameboard[1][playerMove - 4] = 2
        visualboard[1][playerMove - 4] = "o"

    elif playerMove < 10 and gameboard[2][playerMove - 7] == 0:
        gameboard[2][playerMove - 7] = 2
        visualboard[2][playerMove - 7] = "o"
    #def:
        #print("Error - Enter values 1-9")
        #TODO: Error check for non ints, string values, out of range ints



#OUTPUT: output_visualBoard will output the current status of the gameboard by representing an x or o as a string
def output_visualboard(visualboard):
    for i in range(len(visualboard)):
            print("\t")
            print(visualboard[i])

#OUTPUT: output_gameBoard is to better understand how the gameboard is represented and changed.
def output_gameboard(gameboard):
    for i in range(len(gameboard)):
            #print("\t")
            print(gameboard[i])
            print("\t")


