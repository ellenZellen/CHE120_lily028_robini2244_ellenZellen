# Sonar Treasure Hunt

#Lines 4-__ annotated by LY 
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
    for x in range(60): # The main list is a list of 60 lists.
        board.append([])
    #To get the first list to contain 60 lists, this for loop will add 60 blank lists to the board
        for y in range(15): # Each list in the main list has 15 single-character strings.
        #This for loop is used to add 15 single-character strings
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
    #Thie string will be the first row of the board
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

def getRandomChests(numChests): #This function is to randomly generate the position of the chests on the map
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
