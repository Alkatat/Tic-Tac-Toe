import sys
import os
import random

#Gameboard initial state - use output_gameboard(gameboard) for testing
#[0, 0, 0]
#[0, 0, 0]
#[0, 0, 0]
# represented as 1-9

  

      

def generatePossibleMoves( gameboard, targetSymbol ):
  possibleBoards = []
  gameboardTemplate = gameboard
  # get number of empty spaces to generate potential moves
  count = 0
  for row in range( len(gameboard) ):
    for col in range( len(gameboard[row]) ):
      if( gameboard[row][col] == 0 ):
        count += 1
        gameboardTemplate[row][col] = targetSymbol
        possibleBoards.append
        
    

# Most Wins Heuristic
def mostWins( gameboard, targetSymbol):
  # generate possible moves
  generatePossibleMoves( gameboard, targetSymbol )
  # evaluate most possible wins from each move

# How many steps to win Heuristic

