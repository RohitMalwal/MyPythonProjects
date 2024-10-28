import random

board = ['-', '-', '-',
        '-', '-', '-',
         '-', '-', '-',] 

CurrentPlayer = 'X'
winner = None
gamerunning = True

# printing the board for game
def printBoard(board):
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('———|———|———')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('———|———|———')
    print(f' {board[6]} | {board[7]} | {board[8]}')

# take player input
def playerInput(board):
    inp = int(input('Selct a number between 1 to 9: '))
    if inp >= 1 and inp <= 9 and board[inp-1]=='-':
        board[inp-1]=CurrentPlayer
    else:
        print("you choose the wrong box\n")
    
# check for win or tie

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0]!='-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]!='-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]!='-':
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!='-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!='-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!='-':
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!='-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!='-':
        winner = board[2]
        return True


def checkTie(board):
    global gamerunning
    if '-' not in board:
        print("It's a Tie")
        gamerunning = False

def checkWin():
    global gamerunning
    if checkVertical(board) or checkHorizontal(board) or checkDiagonal(board) == True:
        printBoard(board)
        if winner == 'X':
            print('You Won')
            gamerunning = False
        elif winner == 'O':
            print('You Lose')
            gamerunning = False


# switch the player

def switchPlayer():
    global CurrentPlayer
    if CurrentPlayer == 'X':
        CurrentPlayer = 'O'
    else:
        CurrentPlayer = 'X'

# computer

def computer(board):
    if CurrentPlayer == 'O':
        position = random.randint(0, 8)
        while board[position] != '-':  # Keep generating a new position until an empty spot is found
            position = random.randint(0, 8)
        board[position] = 'O'
        switchPlayer()


# initiate function
def playing():
    ask = input('Manually or Computer  (M/C): ')
    while gamerunning:
        if ask == 'C':
            printBoard(board)
            playerInput(board)
            checkWin() 
            if not gamerunning:  # If game ends after player's win, don't check for tie
                break
            checkTie(board)
            if not gamerunning:
                break
            switchPlayer()
            computer(board)
            # printBoard(board)
            checkWin() 
            if not gamerunning:  # If game ends after computer's win, don't check for tie
                break
            checkTie(board)
            if not gamerunning:
                break
        elif ask == "M":         
            printBoard(board)
            playerInput(board)
            checkWin() 
            if not gamerunning:  # If game ends, don't check for tie
                break
            checkTie(board)
            if not gamerunning:
                break
            switchPlayer()
        else:
            print('You choose the wrong key')
            break


playing()


print(input('press ENTER to exit'))





## IT'S NOT WORKING AS I EXPECTED  ## 