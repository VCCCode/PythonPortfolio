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

from random import randrange

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
pcMoves = []
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
    

def enter_move(placeDict, boardList):
    placeKeys = placeDict.keys()
    placeMsg = []
    for i in placeKeys:
        placeMsg.append(i)
    print(placeKeys)
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
                move_list.append(indTuple)
                placeDict.update({j: indTuple})
            # Update multiple index variables
            indJ += 1
            num += 1
        indI += 1
    # Know the amount of possible moves left
    poss_moves = len(move_list)
    print(placeDict)
    # Give back the amount of moves and the list of available locations
    return(poss_moves, moveList, placeDict)
    


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board, possible_moves, placeDict):
    cpuChoice = randrange(0, possible_moves)
    print(cpuChoice)
    for i in placeDict.keys():
        if cpuChoice == i:
            movePlaceCPU = placeDict[i]
            print(movePlaceCPU)
            boardList[movePlaceCPU[0]][movePlaceCPU[1]] = letX
        else: continue
    countCpu = 0
    for i in boardList:
        for t in i:
            if t == letX:
                pcMoves.append(placeDict[countCpu])
            countCpu += 1
    print(pcMoves)
    print(boardList)
    # The function draws the computer's move and updates the board.

possible_moves = 0
move_list = []
possible_moves, moveList, placeDict = make_list_of_free_fields(boardList)
print(possible_moves)
print(move_list)
print(placeDict)
enter_move(placeDict, boardList)
draw_move(boardList, possible_moves, placeDict)
display_board(boardList) 