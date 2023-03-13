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

def display_board(boardList):
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
    print(board)
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(boardList):
    rightAns = False
    while not rightAns:
        playerMove = int(input("Write the position's number \n -> "))
        rightAns = playerMove >=1 and playerMove <= 9
        if not rightAns:
            print("Please enter a valid number")
            continue
        playerMove -= 1

        row = playerMove // 3
        column = playerMove % 3
        sign = boardList[row][column]
        rightAns = sign not in ['X', 'O']
        if not rightAns:
            print("Number is taken, please enter a free position")
            continue   
    boardList[row][column] = "O"
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(boardList):
    freeSpots = []
    for row in range(3):
        for column in range(3):
            if boardList[row][column] not in ['X', 'O']:
                freeSpots.append((row, column))
    return freeSpots
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(boardList, sign):
    victFreeSpots = make_list_of_free_fields(boardList)
    if sign == 'X':
        plyr = 'PC'
    if sign == 'O':
        plyr = 'You'
    
    for i in range(3):
        rowWin = boardList[i][0] == sign and boardList[i][1] == sign and boardList[i][2] == sign
        columnWin = boardList[0][i] == sign and boardList[1][i] == sign and boardList[2][i] == sign
        diag1Win = boardList[0][0] == sign and boardList[1][1] == sign and boardList[2][2] == sign
        diag2Win = boardList[1][1] == sign and boardList[0][2] == sign and boardList[2][0] == sign
        if rowWin or columnWin or diag2Win or diag1Win:
            print("Game Finished: ", end='')
            print(plyr, 'Win')
            display_board(boardList)
            keepPlayin = False
            return keepPlayin 
    if len(victFreeSpots) == 0:
        print("Game finished, it's a tie")
        display_board(boardList)
        keepPlayin = False
        return keepPlayin  
    else: 
        return True  
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(boardList):
    pcFree = make_list_of_free_fields(boardList)
    if len(pcFree) != 0:
        pcChoice = randrange(0, len(pcFree))
        pcValue = pcFree[pcChoice]
        boardList[pcValue[0]][pcValue[1]] = 'X'
        # The function draws the computer's move and updates the board.

boardList = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
boardList[1][1] = 'X'
display_board(boardList)
keepPlayin = True
playerTurn = True
while keepPlayin:
    frees = make_list_of_free_fields(boardList)
    if len(frees) == 0:
        keepPlayin = False
        continue
    display_board(boardList)
    if playerTurn:
        enter_move(boardList)
        keepPlayin = victory_for(boardList, 'O')
    if not playerTurn:
        draw_move(boardList)
        keepPlayin = victory_for(boardList, 'X')
    playerTurn = not playerTurn