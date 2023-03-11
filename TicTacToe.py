'''

    the computer (i.e., your program) should play the game using 'X's;
    the user (e.g., you) should play the game using 'O's;
    the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
    all the squares are numbered row by row starting with 1 (see the example session below for reference)
    the user inputs their move by entering the number of the square they choose − the number must be valid,
        i.e., it must be an integer, it must be greater than 0 and less than 10,
        and it cannot point to a field which is already occupied;
    the program checks if the game is over − there are four possible verdicts:
        the game should continue, the game ends with a tie, you win, or the computer wins;
    the computer responds with its move and the check is repeated;
    don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.

'''
import random
letO = 'O'
letX = 'X'
boardList = [[1, 2, 3], [4, letX, 6], [7, 8, 9]]
board = f' \
+-------+-------+-------+\n \
|       |       |       |\n \
|   {boardList[0][0]}   |   {boardList[0][1]}   |   {boardList[0][2]}   |\n \
|       |       |       |\n \
+-------+-------+-------+\n \
|       |       |       |\n \
|   {boardList[1][0]}   |   {boardList[1][1]}   |   {boardList[1][2]}   |\n \
|       |       |       |\n \
+-------+-------+-------+\n \
|       |       |       |\n \
|   {boardList[2][0]}   |   {boardList[2][1]}   |   {boardList[2][2]}   |\n \
|       |       |       |\n \
+-------+-------+-------+'
playerMoves = []
pcMoves = [(1, 1)]
gameEnd = False


def display_board(board):
    board = f' \
+-------+-------+-------+\n \
|       |       |       |\n \
|   {boardList[0][0]}   |   {boardList[0][1]}   |   {boardList[0][2]}   |\n \
|       |       |       |\n \
+-------+-------+-------+\n \
|       |       |       |\n \
|   {boardList[1][0]}   |   {boardList[1][1]}   |   {boardList[1][2]}   |\n \
|       |       |       |\n \
+-------+-------+-------+\n \
|       |       |       |\n \
|   {boardList[2][0]}   |   {boardList[2][1]}   |   {boardList[2][2]}   |\n \
|       |       |       |\n \
+-------+-------+-------+'
    
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(board)
    return board
    

def enter_move(placeDict, boardList):
    placeKeys = placeDict.keys()
    placeMsg = []
    for i in placeKeys:
        placeMsg.append(i)
    try:
        playerMove = int(input(f'Enter one of the following places {placeMsg} \n'))
        if playerMove in placeKeys:
            movePlace = placeDict[playerMove]
            playerMoves.append(movePlace)
            print(playerMoves)
            boardList[movePlace[0]][movePlace[1]] = letO
            print(boardList)
        else:
            print('That is not a valid place, please try again')
            enter_move(placeDict, boardList)
    except ValueError:
        print('That is not a valid value, please try again')
        enter_move(placeDict, boardList)        
    return boardList
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    # Create empty list, index values and comparison numbers for the f(x)
    moveList = []
    indI = 0
    num = 1
    placeDict = {}
    # The function browses the board
    for i in board:
        indJ = 0
        for j in i:
            # Create tuples, where each tuple is a pair of row and column numbers.
            indTuple = (indI, indJ)
            if j is num:
                # The list consists of tuples
                moveList.append(indTuple)
                placeDict.update({j: indTuple})
            # Update multiple index variables
            indJ += 1
            num += 1
        indI += 1
    # Know the amount of possible moves left
    poss_moves = len(moveList)
    print(placeDict)
    # Give back the amount of moves and the list of available locations
    return(poss_moves, moveList, placeDict)
    


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board, possible_moves, move_list):
    # The function draws the computer's move and updates the board.
    # Get a random number from a list of possible moves

    cpuList = []
    for i in placeDict.keys():
        cpuList.append(i)
        print(cpuList)
    print(cpuList)
    cpuChoice = random.choice(cpuList)
    print(cpuChoice)
    movePlaceCPU = placeDict[cpuChoice]
    print(movePlaceCPU)
    pcMoves.append(movePlaceCPU)
    boardList[movePlaceCPU[0]][movePlaceCPU[1]] = letX
    print(pcMoves)
    print(boardList)
    return boardList
    # The function draws the computer's move and updates the board.


while gameEnd == False:
    possible_moves, moveList, placeDict = make_list_of_free_fields(boardList)
    display_board(boardList) 
    boardList = enter_move(placeDict, boardList)
    display_board(boardList)
    possible_moves, moveList, placeDict = make_list_of_free_fields(boardList) 
    boardList = draw_move(boardList, possible_moves, moveList)
    display_board(boardList) 
    keepPlayin = input("enter another move? (enter: yes; anything: no) ")
    if keepPlayin != "":
        break