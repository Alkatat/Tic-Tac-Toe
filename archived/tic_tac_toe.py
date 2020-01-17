#tic_tac_toe.py
#Works barebones, doesn't check for winner or if space if free
#have functions implemented but unused
#loops infinitely

import random

class TicTacToe:

	#Game board
	def board(space):
	
		print( ' ' + space[7] + ' | ' + space[8] + ' | ' + space[9])
		print('----------')
		print( ' ' + space[4] + ' | ' + space[5] + ' | ' + space[6])
		print('----------')
		print( ' ' + space[1] + ' | ' + space[2] + ' | ' + space[3])

	
	#Player Input Function
	def PlayerInput():
		val = input("Choose a space (1-9)")
		print("You chose " + val)
		return int(val)

	#Assigns letter based on input from Player or AI
	def AssignSpace(letter, space, val):
		space[val] = letter

	#Generates Random Number so AI can move to that space
	#Implement heuristics here?
	def AIMove():
		val = random.randint(1,9)
		print(val)
		return int(val)

	def CheckSpace(board, val):
		return borad[val] == ' '


	#Checks if there is any winner
	def WinnerWinner(board, letter):
		return ((board[1]  == letter and board[2] == letter and board[3] == letter) or #bottom row
			(board[4]  == letter and board[5] == letter and board[6] == letter) or #middle row
			(board[7]  == letter and board[8] == letter and board[9] == letter) or #top row
			(board[1]  == letter and board[4] == letter and board[7] == letter) or #left column
			(board[2]  == letter and board[5] == letter and board[8] == letter) or #middle column
			(board[3]  == letter and board[6] == letter and board[9] == letter) or #right column 
			(board[3]  == letter and board[5] == letter and board[7] == letter) or #bottom diagonal
			(board[1]  == letter and board[5] == letter and board[9] == letter))   #up diagonal

	#Player will be 'O'
	#AI will be 'X'
	#Can implement choice if we have time
	while True:
		playerletter = 'O'
		ailetter = 'X'
		gameBoard = [' '] * 10
		gameOn = True
		board(gameBoard)
		while gameOn:
			print(' ')
			print(' ')
			val = PlayerInput()
			AssignSpace(playerletter, gameBoard, val)
			val2 = AIMove()
			AssignSpace(ailetter, gameBoard, val2)
			print(' ')
			print(' ')
			board(gameBoard)
