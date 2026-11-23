# Sonar Treasure Hunt 

#Lines 4-84 annotated by LY 
import random
#random is needed to generate random numbers to create the ocean wave pattern, and decide where the treasure chests are hidden on the board.
import sys
#sys is needed for the exit() function, which stops any code in the line after it from running, stopping the program.
import math
#math is needed for the sprt() functoin, which is used when finding the closest treasure chest.

def getNewBoard():
    # Create a new 60x15 board data structure.
    board = []
    #The list below represents the x coordinates
    #To get the first list to contain 60 lists, this for loop will add 60 blank lists to the board    
    for x in range(60): # The main list is a list of 60 lists.
        board.append([])
        #This for loop is used to add 15 single-character strings       
        for y in range(15): # Each list in the main list has 15 single-character strings.
    # Use different characters for the ocean to make it more readable.
    #Randomly choose one of the following characters to make a unique board
            #If the return value of random.randint is 0, ~ will be used
            if random.randint(0, 1) == 0:
                board[x].append('~')
            #If the return value of random.randint is not 0, ` will be used
            else:
                board[x].append('`')
    #Returns the value in board            
    return board

# drawBoard will be called on to draw the actual board
def drawBoard(board):
    # Draw the board data structure.
    #This string will be the first row of the board
    #Creates a string with the numbers 
    tensDigitsLine = '    ' # Initial space for the numbers down the left side of the board
    #Loops variable i through numbers 1-5 and adds 9 spaces between them
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    # Print the numbers across the top of the board.
    #Prints string assigned to tensDigitsLine
    print(tensDigitsLine)
    #Prints three spaces so that the row lines up correctly, and prints the string 0123456789 six times

    print('   ' + ('0123456789' * 6))
    print()

    # Print each of the 15 rows (0-14)
    for row in range(15):
        # Single-digit numbers need to be padded with an extra space so that the board lines up correctly
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

    # Create the string for this row on the board.
        #starts an empty string
        boardRow = ''
        #Moves across the board from left to right
        for column in range(60):
            #Looks up the character stored in each spot as you move across the board  and adds it to the end of the text in boardRow 
            boardRow += board[column][row]
        #then, the string in boardRow is printed with the row numbers defined in row
        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

# Print the x-coordinates across the bottom of the board
    print()
    print('   ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):#This function is to randomly generate the position of the chests on the map
# Create a list of chest data structures (two-item lists of x, y int coordinates).
   #numChests parameter is the number of treasure chests the function should generate
    chests = []
    #The while loop will keep repeating until all the chests have been assigned locations
    while len(chests) < numChests:
        #Two random integers, between 0 and 59 for the x coordinate and between 0 and 14 for the y coordinate are chosen
        #The expression will become a list value
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests: # Makes sure a chest is not already in the chosen coordinates
            #modifies the original chest list to add the new chest coordinate
            chests.append(newChest)
    return chests


#line 88-133 annotated by RI
def isOnBoard(x, y):
    # Return True if the coordinates are on the board; otherwise, return False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    # Change the board data structure with a sonar device character. Remove treasure chests from the chests list as they are found.
    # Return False if this is an invalid move.
    # Otherwise, return the string of the result of this move.
    smallestDistance = 100 # Any chest will be closer than 100.
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        if distance < smallestDistance: # We want the closest treasure chest.
            smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
        # xy is directly on a treasure chest!
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return 'Treasure detected at a distance of %s from the sonar device.' % (smallestDistance)
        else:
            board[x][y] = 'X'
            return 'Sonar did not detect anything. All treasure chests out of range.'

def enterPlayerMove(previousMoves):
    # Let the player enter their move. Return a two-item list of int xy coordinates.
    print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('You already moved there.')
                continue
            return [int(move[0]), int(move[1])]

        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')


#line 139-263 annotated by EZ
#define a function to display the game rules and examples to the player
#this is a separated into a function so the main game flow stays clean and readable, and instructions are only shown if the user requests them
def showInstructions():
    print('''Instructions:
You are the captain of the Simon, a treasure-hunting ship. Your current mission
is to use sonar devices to find three sunken treasure chests at the bottom of
the ocean. But you only have cheap sonar that finds distance, not direction.

Enter the coordinates to drop a sonar device. The ocean map will be marked with
how far away the nearest chest is, or an X if it is beyond the sonar device's
range. For example, the C marks are where chests are. The sonar device shows a
3 because the closest chest is 3 spaces away.

1 2 3
012345678901234567890123456789012

0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
3 ````````~~~`````~~~`~`````~`~``~` 3
4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

012345678901234567890123456789012
1 2 3
(In the real game, the chests are not visible in the ocean.)

Press enter to continue...''')
#pause program execution using input() without storing the return value in order to prevent the second half of the instructions from scrolling past too quickly.
#so basically it gives the player time to read the first screen.
    input()
#the  print the second part of the instructions explaining what happens when a chest is found 
#other sonar readings update to point to the closest chest and the max sonar range (9 spaces)
    print('''When you drop a sonar device directly on a chest, you retrieve it and the other
sonar devices update to show how far away the next nearest chest is. The chests
are beyond the range of the sonar device on the left, so it shows an X.

1 2 3
012345678901234567890123456789012

0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
3 ````````~~~`````~~~`~`````~`~``~` 3
4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

012345678901234567890123456789012
1 2 3

The treasure chests don't move around. Sonar devices can detect treasure chests
up to a distance of 9 spaces. Try to collect all 3 chests before running out of
sonar devices. Good luck!

Press enter to continue...''')
#here pause again so the player can finish reading before the actual game board is drawn
    input()


#print the main title banner and a blank line for visual seperation when program starts
print('S O N A R !')
print()
#ask the player if they want to read the rules before starting
print('Would you like to view the instructions? (yes/no)')
#convert the input to lowercase and check if it starts with 'y'(ie. yes, Yes, Y...)
#to make sure user input flexible and prevent accidential skips due to capitalization
if input().lower().startswith('y'):
    showInstructions()

#main outer game loop: keeps restarting new rounds until the player explicitly choose to quit
while True:
    # Game setup
#reset all variables for a fresh round, give the player 20 turns to find 3 randomly placed chests
    sonarDevices = 20
    theBoard = getNewBoard()
#generate a clean 60x15 grid data structure
    theChests = getRandomChests(3)
#generate 3 unique (x,y) coordinates for hidden treasure chests
    drawBoard(theBoard)
#render the initial empty board to the console
    previousMoves = []
#initialize an empty list to record all valid (x,y) moves made by the player

#inner turn loop: runs as long as the player still has sonar devices(turns) remaining 
    while sonarDevices > 0:
        # Show sonar device and chest statuses.
#diplay current status so the player knows how many attempts and chests are left
#uses string formatting (%s) to dynamically insert the integer count and list length
        print('You have %s sonar device(s) left. %s treasure chest(s) remaining.' % (sonarDevices, len(theChests)))
#prompt the player for valid (x,y) coordinates that have not been guessed yet
        x, y = enterPlayerMove(previousMoves)
#record the new move in previousMoves because when a chest is found and removed, we must recalculate and update the distance numbers for all previously dropped sonar devices on the board
        previousMoves.append([x, y]) # We must track all moves so that sonar devices can be updated.
#place the sonar on the board, calculate distance to the nearest chest, and get the status message
        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
#then check if the player landed directly on a chest which removes that chest from theChests
            if moveResult == 'You have found a sunken treasure chest!':
                # Update all the sonar devices currently on the map.
#rerun makeMove for every past coordinate in previousMoves since one chest was just collected, all exixsting sonar markers on the map are now outdated and must be updated to show distances to the remaining chests
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
#redraw the updated map and print the result of the player's lastest move
            drawBoard(theBoard)
            print(moveResult)
#check if all chests have been removed from theChests list. If so, the player wins.
        if len(theChests) == 0:
            print('You have found all the sunken treasure chests! Congratulations and good game!')
#exist the inner turn loop immediately since the game is won
            break
#decrement the remaining sonar device count by 1 after a valid turn
        sonarDevices -= 1

#loss condition check: if the inner loop ended because sonarDevices reached 0 and not through 'break', let the player know they lost and reveal the coordinates of any undound chests
    if sonarDevices == 0:
        print('We\'ve run out of sonar devices! Now we have to turn the ship around and head')
        print('for home with treasure chests still out there! Game over.')
        print(' The remaining chests were here:')
#loop through the remaining (x,y) pairs in theChests and print their exact locations
        for x, y in theChests:
            print(' %s, %s' % (x, y))

#ask if the player wants to play another round after winning or losing
    print('Do you want to play again? (yes or no)')
#if the response does not start with 'y' or 'Y', terminiate the program.
    if not input().lower().startswith('y'):
        sys.exit()