
from game_states import output_gameboard

#UPDATE:  best_move(board) will return the next best turn for the computer by using the minimax algorithm
#         it currently returns (return bestRow, bestCol) the next best row & col for the gameboard 
#         The current gameboard is represented by a total of 3 values:
#         0 - EMPTY     1 - COMPUTER MOVE     2 - Player Move
#
#         
#         Download my branch for testing


# evaluate(board) will check the current board columns, rows, and diagonal line for a winning case
# 1: Represents computer player holding value of x
# 2: Represents user player holding value of o

#Return  10 for maximizer win
#Return -10 for minimizer win
#Return   0 for draw

def evaluate(board):


    #Row Check: Check for a victory in the current game board
    for row in range(0, 3):

        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != 0 and board[row][2] != 0:

            if board[row][0] == 1:
                return 10
            elif board[row][0] == 2:
                return -10

    # Column Check: Check for a victory in the current game board
    for col in range(0, 3):

         if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] !=0 and board[2][col] !=0:

             if board[0][col] == 1:
                 return 10
             elif board[0][col] == 2:
                return -10


    check_diagonal(board)

    return 0




# Diagonal Check: check_diagonal(board) will check for a diagonal victory in the current game board
def check_diagonal(board):

   if board[1][1] !=0:

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:

        if board[0][0] == 1:
            return 10
        elif board[0][0] == 2:
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:

        if board[0][2] == 1:
            return 10
        elif board[0][2] == 2:
            return -10


def full_board_check(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:

                return True
    #print("Board is full and there is no more room")
    return False




def minimax(board, isMax, depth):

    #Determine if there is a winning play
    score = evaluate(board)

    bestRow = 0
    bestCol = 0
    currentBest = -1000
    currentMiniBest = 1000


    if score == 10:
       # print("Maximizer has won")

        return score

    if score == -10:
        #print("Minimizer has won")
        return score

    if full_board_check(board) == False:
       # print("Draw")
        return 0



    if isMax is True:

        best = -1000
        minimumBest = -1000
        #currentBest = -1000


        for i in range(len(board)):

            for j in range(len(board)):

                #If board value is empty set play
               if board[i][j] == 0:

                    board[i][j] = 1 #1 set board 1 REPRESENT max Recursive

                   # output_gameboard(board)

                    best = max(best, minimax(board, False, depth + 1))

                    #undo the move
                    board[i][j] = 0


        return best

    else:

            minBest = 1000
            miniBest = 1000

            for i in range(len(board)):

                for j in range(len(board)):

                    # If board value is empty set play
                    if board[i][j] == 0:

                        board[i][j] = 2  # 2 set board 2 REPRESENT min Recursive - User Player

                        #output_gameboard(board)

                        minBest = min(minBest, minimax(board, True, depth + 1))

                        # undo the move
                        board[i][j] = 0


            return minBest


    return 0



def best_move(board):


    best = -1000
    bestRow = 0
    bestCol = 0

    for i in range(len(board)):

        for j in range(len(board)):

            # If board value is empty set play
            if board[i][j] == 0:

                board[i][j] = 1  # 1 set board 1 REPRESENT max Recursive

                # output_gameboard(board)

                move = minimax(board, False, 0)

                # undo the move
                board[i][j] = 0

                if move > best:
                    print("i: ",i,"j: ",j)
                    print(move)
                    best = move
                    board[i][j] = 1 #Changing the actual value of the gameboard for the computer(x)
                                    #Future Note:
                                    #This can be moved to tic_tac_toe.py (remove board[i][j] = 1 an add gameboard[x][y] = 1)
                                    #to tic_tac_toe.py 
                    bestRow = i
                    bestCol = j

    return bestRow, bestCol

