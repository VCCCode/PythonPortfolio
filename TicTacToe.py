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
        elif len(placeMsg) == 0: 
            print("There are no more posible moves, game tied")
            raise SystemExit  
        else:
            print('That is not a valid place, please try again')
            enter_move(placeDict, boardList)
    except ValueError:
        print('That is not a valid value, please try again')
        enter_move(placeDict, boardList)        
    return boardList, playerMoves
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
    


def victory_for(boardList, possible_moves = 8, playerMoves = [], pcMoves = []):
    pcColumn = []
    pcRow = []
    playerColumn = []
    playerRow = []
    if possible_moves == 0:
        print("There are no more posible moves, game tied")
        display_board(boardList)
        raise SystemExit
    if ((0, 0) in pcMoves and (1, 1) in pcMoves and (2, 2) in pcMoves) or ((1, 1) in pcMoves and (0, 2) in pcMoves and (2, 0) in pcMoves):
        print("PC Wins")
        display_board(boardList)
        raise SystemExit
    elif ((0, 0) in playerMoves and (1, 1) in playerMoves and (2, 2) in playerMoves) or ((1, 1) in playerMoves and (0, 2) in playerMoves and (2, 0) in playerMoves):
        print("Player Wins")
        display_board(boardList)
        raise SystemExit
    else:
        for i in pcMoves:
            pcColumn.append(i[0])
            pcRow.append(i[1])
        print(pcColumn)
        print(pcRow)
        print(pcColumn.count(0))
        print(pcColumn.count(1))
        print(pcColumn.count(2))
        if pcColumn.count(0) > 2 or pcColumn.count(1) > 2 or pcColumn.count(2) > 2 or \
            pcRow.count(0) > 2 or pcRow.count(1) > 2 or pcRow.count(2) > 2:
            print("PC Wins")
            display_board(boardList)
            raise SystemExit
        for j in playerMoves:
            playerColumn.append(j[0])
            playerRow.append(j[1])
        if playerColumn.count(0) > 2 or playerColumn.count(1) > 2 or playerColumn.count(2) > 2 or \
            playerRow.count(0) > 2 or playerRow.count(1) > 2 or playerRow.count(2) > 2:
            print("Player Wins")
            display_board(boardList)
            raise SystemExit

    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board, possible_moves, move_list):
    # The function draws the computer's move and updates the board.
    # Get a random number from a list of possible moves
    cpuList = []
    for i in placeDict.keys():
        cpuList.append(i)
    cpuChoice = random.choice(cpuList)
    movePlaceCPU = placeDict[cpuChoice]
    pcMoves.append(movePlaceCPU)
    boardList[movePlaceCPU[0]][movePlaceCPU[1]] = letX
    return boardList, pcMoves
    # The function draws the computer's move and updates the board.


while gameEnd == False:
    display_board(boardList) 
    possible_moves, moveList, placeDict = make_list_of_free_fields(boardList)
    boardList, playerMoves = enter_move(placeDict, boardList)
    display_board(boardList)
    victory_for(boardList, possible_moves, playerMoves)
    possible_moves, moveList, placeDict = make_list_of_free_fields(boardList) 
    boardList, pcMoves = draw_move(boardList, possible_moves, moveList)
    victory_for(boardList, possible_moves, playerMoves, pcMoves)
    display_board(boardList) 
    
