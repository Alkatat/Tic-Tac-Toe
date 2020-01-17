import sys
import numpy as npy
from copy import copy

class TTT_Board(object):

    # CONSTANTS
    ROWS = 3
    COLS = 3
    # used for Min Max
    INFINITY = 9999999999
    NEG_INFINITY = -9999999999
    # used for board symbols
    X = 1
    O = 2
    POSSIBLE_WINS = npy.array([
        [0,1,2], # top row
        [3,4,5], # mid row
        [6,7,8], # bot row
        [0,3,6], # left col
        [1,4,7], # mid col
        [2,5,8], # right col
        [0,4,8], # diagonal tl-br
        [2,4,6]]) # diagonal tr-bl
    # AI DEPTH
    LOOK_AHEAD = 2  # seemed most optimal based on tests

    def __init__(self):
        # init board to zeros
        self.reset()

    # GAME UTILITY METHODS
    def reset(self):
        self.board = npy.zeros( (self.ROWS, self.COLS) )
        self.heuristicTable = npy.zeros( (self.ROWS + 1, self.COLS + 1) )
        self.numWinPos = self.ROWS + self.COLS + 2 
        for i in range(0,self.ROWS+1):
            # exponentiation of 10 for heuristic Table to initialize:
            # -1   |   -10  |  -100  | -1000
            # 10   |     0  |     0  |     0
            # 100  |     0  |     0  |     0
            # 1000 |     0  |     0  |     0
            self.heuristicTable[i,0]=10**i
            self.heuristicTable[0,i]=-10**i
        # print(self.heuristicTable)
        

    def makeMove(self, position, symbol):
        row,col = self.translatePlayerMove(position)

        if( row >= self.ROWS or col >= self.COLS):
            return False

        targetSpace = self.board[row, col]
        if( targetSpace == 0):
            self.board[row,col] = symbol
            return True
        else:
            return False

    # player input:
    #   1 | 2 | 3
    #   4 | 5 | 6
    #   7 | 8 | 9
    def translatePlayerMove(self, input):
        if input == 1:
            return 0, 0
        elif input == 2:
            return 0, 1
        elif input == 3:
            return 0, 2
        elif input == 4:
            return 1, 0
        elif input == 5:
            return 1, 1
        elif input == 6:
            return 1, 2
        elif input == 7:
            return 2, 0
        elif input == 8:
            return 2, 1
        elif input == 9:
            return 2, 2

    def isWinner(self, symbol):
        return ((self.board[0,0]  == symbol and self.board[0,1] == symbol and self.board[0,2] == symbol) or #top row
                (self.board[1,0]  == symbol and self.board[1,1] == symbol and self.board[1,2] == symbol) or #middle row
                (self.board[2,0]  == symbol and self.board[2,1] == symbol and self.board[2,2] == symbol) or #bot row
                (self.board[0,0]  == symbol and self.board[1,0] == symbol and self.board[2,0] == symbol) or #left column
                (self.board[0,1]  == symbol and self.board[1,1] == symbol and self.board[2,1] == symbol) or #middle column
                (self.board[0,2]  == symbol and self.board[1,2] == symbol and self.board[2,2] == symbol) or #right column 
                (self.board[0,0]  == symbol and self.board[1,1] == symbol and self.board[2,2] == symbol) or #topLeft diagonal
                (self.board[0,2]  == symbol and self.board[1,1] == symbol and self.board[2,0] == symbol))   #topRight diagonal

    def showBoard(self):
        for i in range(0, self.ROWS):
            for j in range(0, self.COLS):
                if self.board[i,j]==0:
                    print(' - ', end = '')
                elif self.board[i,j]==1:
                    print(' X ', end = '')
                else:
                    print(' O ', end = '')
                if (j < self.COLS-1):
                    print('|', end ='')
            if (i < self.ROWS-1):
                print('\n-----------')
            else:
                print('')

    def yesOrNo(self, question):
        answer = input(question + "(y/n): ").lower().strip()
        print("")
        while not(answer == "y" or answer == "yes" or answer == "n" or answer == "no"):
            print("Input yes or no")
            answer = input(question + "(y/n):").lower().strip()
            print("")
        if answer[0] == "y":
            return True
        else:
            return False
    
    def askReplay(self):
        replay = self.yesOrNo('Play Again?')
        if (replay):
            self.reset()
            self.runGame()
        else:
            return
    
    # AI METHODS        
    # heuristic table evaluation function -> summation of the "closeness" each player is to the 8 possible win states
    def getHeuristicsFor(self, boardState):
        # numpy ravel -> unravels a 2d array into contiguous 1d array (https://www.geeksforgeeks.org/numpy-ravel-python/)
        tempState = copy( boardState.ravel() )
        heuristic = 0
        for i in range(0, self.numWinPos):
            maximizer = 0
            minimizer = 0
            # evaluate heuristic of closeness to winning
            for j in range(0, self.ROWS):
                if tempState[self.POSSIBLE_WINS[i,j]] == self.O:
                    maximizer += 1
                elif tempState[self.POSSIBLE_WINS[i,j]] == self.X:
                    minimizer += 1
            evalHeuristic = self.heuristicTable[maximizer][minimizer]
            # print( 'max: ' + str(maximizer) + ' min: ' + str(minimizer) + ' heur: ' + str(evalHeuristic))
            # add up heuristic valueation for possible win state
            heuristic += evalHeuristic
        # print('heuristic val: ', heuristic)
        return heuristic

    # minimax based of geeksforgeeks pseudocode
    def minimax(self, boardState, alphaVal, betaVal, isMax, depth, maxSymbol, minSymbol):
        # recursive exit -> depth evaluation limit
        if (depth == 0):
            return self.getHeuristicsFor(boardState), boardState
        
        # determine rows and columns that can be moved to
        remainRows, remainCols = npy.where(boardState == 0)
        newBoardState = copy(boardState)

        # if 0 rows remain, exit
        if (remainRows.shape[0] == 0):
            return self.getHeuristicsFor(boardState), newBoardState

        
        if isMax:
            # maximizer route
            bestVal = self.NEG_INFINITY
            # loop through columns
            for i in range( 0, remainCols.shape[0]):
                # temp board for manipulation
                tempBoard = copy(boardState)
                # maximizer's potential move
                tempBoard[remainRows[i],remainCols[i]] = maxSymbol
                # minimizer's potential next turn
                nextHeurVal, nextBoardState = self.minimax(tempBoard, alphaVal, betaVal, False, depth-1, maxSymbol, minSymbol)
                #print(nextBoardState)
                # alpha beta evaluation for max
                if (nextHeurVal > bestVal):
                    #change weight
                    bestVal = nextHeurVal
                    newBoardState = copy(tempBoard)
                # re-assigning alpha checks
                if (bestVal > alphaVal):
                    alphaVal = bestVal
                # prune check
                if (alphaVal >= betaVal):
                    break
            # print('best max val: ' + str(bestVal) + ' found in state\n' + str(newBoardState))
            return bestVal, newBoardState

        else:
            # minimizer route
            bestVal = self.INFINITY
            # loop through rows
            for i in range( 0, remainRows.shape[0]):
                # temp board for manipulation
                tempBoard = copy(boardState)
                # minimizer's potential move
                tempBoard[remainRows[i],remainCols[i]] = minSymbol
                # maximizer's potential next turn
                nextHeurVal, nextBoardState = self.minimax(tempBoard, alphaVal, betaVal, True, depth-1, maxSymbol, minSymbol)
                #print(nextBoardState)
                # alpha beta evaluation for max
                if (nextHeurVal < bestVal):
                    #change weight
                    bestVal = nextHeurVal
                    newBoardState = copy(tempBoard)
                # re-assigning beta check
                if (bestVal < betaVal):
                    betaVal = bestVal
                # prune check
                if (alphaVal >= betaVal):
                    break
            # print('best min val: ' + str(bestVal) + ' found in state\n' + str(newBoardState))
            return bestVal, newBoardState


    # GAME DRIVER
    def runGame(self):
        # game run logic goes here
        print('Welcome to Tic-Tac-Toe! \nPlayer Symbol: X\nCPU Symbol: O')
        print('Player Move Guide:\n 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9')
        goesFirst = self.yesOrNo('Would you like to go first?')
        goesFirstVal = int(goesFirst)
        #print('goes first ' + goFirst)
        # NOTE: tic-tac-toe game only has a total of ROW*COL (usually 3*3) possible turns
        # NOTE: if after all turns and no winner, game results in draw
        for turnNum in range(0, self.ROWS*self.COLS):
            # if player's turn
            if ( (turnNum + goesFirstVal)%2 == 1 ):
                # Get player's input
                # print('goes first val: ', goesFirst)
                if (goesFirst == True):
                    self.showBoard()
                    goesFirst = False
                inVal = int(input('\nEnter Move (1-9): '))
                validMove = self.makeMove( inVal, self.X)
                while not(validMove):
                    print('invalid move - try again')
                    self.showBoard()
                    inVal = int(input('\nEnter Move (1-9): '))
                    validMove = self.makeMove( inVal, self.X)

                self.showBoard()
                #check if player won
                if (self.isWinner(self.X)):
                    print('You Win! Congrats')
                    self.askReplay()
                    return
                
            # else computer's turn
            else:
                print('\nComputer moving....')
                # perform minimax and get board state and heuristic value of move
                value, resultingBoard = self.minimax(self.board, self.NEG_INFINITY, self.INFINITY, True, self.LOOK_AHEAD, self.O, self.X)
                # print('computer moved heuristic value: ', value)
                self.board = copy(resultingBoard)
                self.showBoard()
                # check if computer won
                if (self.isWinner(self.O) ):
                    print('GAME OVER - Computer Wins!')
                    self.askReplay()
                    return

        print(' BOARD FULL - DRAW GAME!')
        self.askReplay()
        return


