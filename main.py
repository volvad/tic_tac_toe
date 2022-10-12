##############################
#  main.py                   #
#                            #
#  console tic-tac-toe game  #
#  made by volvad(<0/>@D)    #
##############################


# initialization global variables


gameField = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
tupleInput = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

##############################


# drawing the current situation on the field
def functionField():
    for row in gameField:
        for field in row:
            print(field, end=' ')
        print()

##############################


# player1 input validation
def inputPlayer1():
    while True:
        stringPlayer1 = input('Player 1 (Enter a number from 1 to 9): ')
        if (stringPlayer1 in tupleInput):
            global numberPlayer1
            numberPlayer1 = int(stringPlayer1)
            break
        print('Input ERROR. Enter a number from 1 to 9')

##############################


# player2 input validation
def inputPlayer2():
    while True:
        stringPlayer2 = input('Player 2 Enter a number from 1 to 9): ')
        if (stringPlayer2 in tupleInput):
            global numberPlayer2
            numberPlayer2 = int(stringPlayer2)
            break
        print('Input ERROR. Enter a number from 1 to 9')

##############################


# writing field 'X' to array for Player1
def functionPlayer1():
    while True:
        if (numberPlayer1 == 1) & (gameField[0][0] == '1'):
            gameField[0][0] = 'X'
            break
        elif (numberPlayer1 == 2) & (gameField[0][1] == '2'):
            gameField[0][1] = 'X'
            break
        elif (numberPlayer1 == 3) & (gameField[0][2] == '3'):
            gameField[0][2] = 'X'
            break
        elif (numberPlayer1 == 4) & (gameField[1][0] == '4'):
            gameField[1][0] = 'X'
            break
        elif (numberPlayer1 == 5) & (gameField[1][1] == '5'):
            gameField[1][1] = 'X'
            break
        elif (numberPlayer1 == 6) & (gameField[1][2] == '6'):
            gameField[1][2] = 'X'
            break
        elif (numberPlayer1 == 7) & (gameField[2][0] == '7'):
            gameField[2][0] = 'X'
            break
        elif (numberPlayer1 == 8) & (gameField[2][1] == '8'):
            gameField[2][1] = 'X'
            break
        elif (numberPlayer1 == 9) & (gameField[2][2] == '9'):
            gameField[2][2] = 'X'
            break
        # check if array is full
        print('This field is busy. Select another field or all fields are occupied.')
        inputPlayer1()

##############################


# writing field 'O' to array for Player2
def functionPlayer2():
    while True:
        if (numberPlayer2 == 1) & (gameField[0][0] == '1'):
            gameField[0][0] = 'O'
            break
        elif (numberPlayer2 == 2) & (gameField[0][1] == '2'):
            gameField[0][1] = 'O'
            break
        elif (numberPlayer2 == 3) & (gameField[0][2] == '3'):
            gameField[0][2] = 'O'
            break
        elif (numberPlayer2 == 4) & (gameField[1][0] == '4'):
            gameField[1][0] = 'O'
            break
        elif (numberPlayer2 == 5) & (gameField[1][1] == '5'):
            gameField[1][1] = 'O'
            break
        elif (numberPlayer2 == 6) & (gameField[2][2] == '6'):
            gameField[1][2] = 'O'
            break
        elif (numberPlayer2 == 7) & (gameField[2][0] == '7'):
            gameField[2][0] = 'O'
            break
        elif (numberPlayer2 == 8) & (gameField[2][1] == '8'):
            gameField[2][1] = 'O'
            break
        elif (numberPlayer2 == 9) & (gameField[2][2] == '9'):
            gameField[2][2] = 'O'
            break
        # check if array is full
        print('This field is busy. Select another field or all fields are occupied.')
        inputPlayer2()


##############################


# main program
print('New Game')
print(functionField())
while True:
    inputPlayer1()
    functionPlayer1()
    print(functionField())
    inputPlayer2()
    functionPlayer2()
    print(functionField())

    # print('Game over')
    # break

##############################


# 000 001 010 011 100 101 110 111
# 000 001 010 011 100 101 110 111
# 000 001 010 011 100 101 110 111

# 000 001 010 011 100 101 110 111
# 000 001 010 011 100 101 110 111
# 000 001 010 011 100 101 110 111
