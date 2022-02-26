# File:         proj1.py
# Author:       Nick Stommel
# Date:         11/09/15
# Section:      Lab - 24, Lecture - 19
# E-mail:       stommel1@umbc.edu
# Description:  This program is an automated version of Conway's Game of Life, complete with a test library of pre-built board patterns and a menu interface.

# getValid(name, instructions, limit, allowQuit, allowZero) is a flexible function used to obtain valid user input in different situations.
# It is critical to prevent crashing without using try/catch statements and removes the need for excess or repeated while loops.
# When valid input is provided, valid input is returned. By default, the third argument limit is equal to the integer 0, the fourth argument
# allowQuit is set to False, and the fifth argument allowZero is set to false. Defaults are set so that the function only requires two arguments.
# Inputs: The user enters in a string. The function also takes up to five arguments (but only needs the first two) that allow customization of
# the instructions, error message, maximum value for user input, whether zero is a valid input, and whether or not returning the string 'q' to quit
# (instead of a positive integer)is allowed.
# Outputs: the first valid input in the form of a positive integer (sometimes within a limit), zero (when allowed), or the string 'q' (when allowed)
def getValid(name, instructions, limit=0, allowQuit=False, allowZero=False):

    invalid = True
    while invalid:

        # The user must first provide input.
        userInput = input(instructions)

        # If the user enters the string 'q' and quitting is allowed, return the string 'q'
        if userInput == "q" and allowQuit == True:
            invalid = False

        # If the user enters a zero and zero is allowed (for other purposes we wouldn't want zero to be valid. For example, we can't have an existent
        # board of 0 rows or 0 columns.), then return the integer 0.
        elif userInput == "0" and allowZero == True:
            userInput = int(userInput)
            invalid = False

        # If the user enters in a positive integer, test for whether the value equals or exceeds the limit (if specified) and return that positive integer
        # if it's within the valid range.
        elif userInput.isnumeric() == True and userInput != "0":
            userInput = int(userInput)
            if limit != 0:
                if userInput >= limit:
                    print("Invalid " + name + ", value is too large.")
                else:
                    invalid = False
            else:
                invalid = False

        # Otherwise, if the user enters a negative number or a string other than q, print a customized error statement depending on whether zero is allowed
        # as in input value.
        else:
            if allowZero == True:
                print("Invalid " + name + ", enter zero or a positive integer.")
            else:
                print("Invalid " + name + ", enter a positive integer.")
            
    return userInput


# getBoard() This function populates a rectangular board of the user's design with dead cells ('.') and live cells ('A').
# Inputs: total row number, total column number, coordinates (row, column) for alive cells
# Outputs: the completed starting board
def getBoard():
    
    rowCount = getValid("row count", "Enter number of rows: ")

    columnCount = getValid("column count", "Enter number of columns: ")
    print()

    # These two for loops are used to initialize a 2D board list full of 'dead' cells (periods)
    board = []
    for num in range(rowCount):
        board.append([])
    for row in board:
        for num in range(columnCount):
            row.append(".")

    # Statement added for clarification of the concept of indexing to the average user.
    print("!!! Please note that columns and rows are numbered starting with 0, so if the board is for example 10 rows x 10 columns, the first row would be row 0 and the last row would be row 9 (columns would also be numbered the same way). !!!")
    
    # While loop used to prompt the user to enter coordinates of 'alive' cells to turn on.
    cellPrompt = True
    while cellPrompt:
        rowNumber = getValid("row number", "Enter row number of a cell to turn on (or 'q' to exit): ", limit=rowCount, allowQuit=True, allowZero=True)
        # Closes loop if input is 'q'.
        if rowNumber == "q":
            cellPrompt = False
        else:
            columnNumber = getValid("column number", "Enter the corresponding column number (or 'q' to abort entry): ", limit=columnCount, allowQuit=True, allowZero=True)
            # If the user aborts entry, nothing happens and the loop is re-executed.
            if columnNumber == "q":
                print("Entry aborted.")
            else:
                board[rowNumber][columnNumber] = "A"
                print()

    return board

# printBoard(board) This function takes in a 2D board list and prints it out in appropriately colored unicode characters.
# Inputs: 2D board list
# Outputs: printed board
def printBoard(board):

    # I obtained the three lines of code needed to color text in the terminal for better visibility using this helpful source:
    # http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    # This site also explains ANSI escape codes in detail:
    # http://jafrog.com/2013/11/23/colors-in-terminal.html
    # I also found the unicode character codes at http://unicode-table.com

    # CSI stands for Control Sequence Indicator, composed of a hexadecimal ASCII ESC character code and a square bracket [
    # The CSI is used to color printed characters in the terminal.
    CSI = "\x1B["
    reset = CSI + "m"
    print()
    print(board)
    # Nested for loops used to iterate through every cell in the board.
    for row in board:
        print("  ", end = "")
        for cell in row:
            if cell == "A":
                print(CSI + "36;1m" + "\u25cf" + CSI + "0m", end=" ") # Prints blue, filled-in circle.
            else:
                print(CSI + "30;1m" + "\u25cb" + CSI + "0m", end=" ") # Prints gray, empty circle.
        print()
    print()

# checkBoard(board) This function checks every cell in the original board and returns a new, corresponding board composed of integers (live neighbor counts).
# Inputs: original board
# Outputs: board of live neighbor counts
def checkBoard(board):

    # Nested for loops used to iterate through every cell in the board.
    liveCountBoard = []
    for rowNum in range(len(board)):
        rowList = []
        for cellNum in range(len(board[0])):
            liveCount = 0

            # Every neighboring cell state checked, except when the index to check does not exist (as in the case where a cell is located on the border)
            # If the cell is alive, then the live count for that cell is incremented by 1.
            leftIndex = cellNum - 1
            if leftIndex > -1:
                if board[rowNum][leftIndex] == "A":
                    liveCount += 1
            rightIndex = cellNum + 1
            if rightIndex < len(board[0]):
                if board[rowNum][rightIndex] == "A":
                    liveCount += 1
            upIndex = rowNum - 1
            if upIndex > -1:
                if board[upIndex][cellNum] == "A":
                    liveCount += 1
            downIndex = rowNum + 1
            if downIndex < len(board):
                if board[downIndex][cellNum] == "A":
                    liveCount += 1
            if upIndex > -1 and rightIndex < len(board[0]):
                if board[upIndex][rightIndex] == "A":
                    liveCount += 1
            if upIndex > -1 and leftIndex > -1:
                if board[upIndex][leftIndex] == "A":
                    liveCount += 1
            if downIndex < len(board) and rightIndex < len(board[0]):
                if board[downIndex][rightIndex] == "A":
                    liveCount += 1
            if downIndex < len(board) and leftIndex > -1:
                if board[downIndex][leftIndex] == "A":
                    liveCount += 1
            # The live count for the cell is appended to a list for that row.    
            rowList.append(liveCount)
        # The row list is appended to the live count board list, then the live count board is returned below.    
        liveCountBoard.append(rowList)

    return liveCountBoard
                
# nextIteration(board) This integral function tests the live count board returned by the checkBoard function and returns a new board based on Conway's rules.
# Inputs: the current board
# Outputs: the next board
def nextIteration(board):

    # Live count board obtained by calling the checkBoard function with the provided board argument.
    liveCountBoard = checkBoard(board)

    # Nested for loops used to iterate through every live count in the board.
    for rowNum in range(len(liveCountBoard)):
        for cellNum in range(len(liveCountBoard[0])):
        # Conway's rules are tested and the board altered accordingly.

            # Cell state is checked (dead '.' or alive 'A')
            if board[rowNum][cellNum] == "A":
                # A live cell with fewer than two live neighbors dies, changing to a '.'.
                if liveCountBoard[rowNum][cellNum] < 2:
                    board[rowNum][cellNum] = "."
                # A live cell with two or three live neighbors lives on to the next generation.
                if liveCountBoard[rowNum][cellNum] == 2 or liveCountBoard[rowNum][cellNum] == 3:
                    board[rowNum][cellNum] = "A"
                # A live cell with more than three neighbors dies, changing to a '.'.
                if liveCountBoard[rowNum][cellNum] > 3:
                    board[rowNum][cellNum] = "."
            else:
                # A dead cell with exactly three live neighbors becomes a live cell, changing to an 'A'.
                if liveCountBoard[rowNum][cellNum] == 3:
                    board[rowNum][cellNum] = "A"

    return board

# iterateBoard(board) This function iterates and prints the board a specified number of times using a while loop and the nextBoard and printBoard functions.
# Inputs: original board
# Outputs: printed series of iterated boards
def iterateBoard(board):

    iterationLimit = getValid("iteration limit", "Enter the number of iterations: ", allowZero=True)
    print()
        
    # While loop used to print and iterate through boards the specified number of times. 
    iteration = 1
    while iteration < (iterationLimit + 1):
        nextBoard = nextIteration(board)
        underline("Iteration #" + str(iteration))
        printBoard(nextBoard)
        iteration += 1

# underline(text) This function takes in a string, then prints and underlines it with em dashes.
# Inputs: a string
# Outputs: the underlined string
def underline(text):

    print(text + "\n" + "—" * len(text))

    
# The two functions below are used for reading in board pattern files.
# -----------------------------------------------------------------------------------------------------------------------
# patternSelector(choice) This function returns a board text file depending on user choice.
# Inputs: an integer representing the selection
# Outputs: the actual board text file
def patternSelector(choice):

    if choice == 1:
        boardFile = "pulsar.txt"
    elif choice == 2:
        boardFile = "pentadecathlon.txt"
    elif choice == 3:
        boardFile = "octagon.txt"
    elif choice == 4:
        boardFile = "koksgalaxy.txt"
    elif choice == 5:
        boardFile = "beluchenko5-4.txt"
    elif choice == 6:
        boardFile = "beluchenko-37.txt"

    return boardFile

# patternSelector(boardFile) This function reads in a board file and returns a usable 2D board list.
# Inputs: board file
# Outputs: 2D board list
def patternReader(boardFile):
    
    # board files are contained in the directory 'board_patterns/' which is located within the directory containing the project file    
    readFile = open("board_patterns_proj1/" + boardFile)

    # For loop assembles 2D board list from board file.
    board = []
    for line in readFile:
        row = line.split()
        board.append(row)

    return board
# -----------------------------------------------------------------------------------------------------------------------


# main() The main() function calls all the preceding functions and ties together the program into a menu interface with a sub-menu for selecting board patterns
# Inputs: user choice(s) as integers or the string 'q' to quit
# Outputs: the menu, sub-menu, instruction prompts, and iterated printed boards
def main():
    
    underline("Conway's Game of Life")
    print()
    
    # Main Menu loop
    menuLoop = True
    while menuLoop:
        
        # Menu heading and user intructions
        underline("Menu")
        print("(1) Create custom game board\n(2) Choose a pre-built game board")
        
        choice = getValid("choice", "Enter your choice or 'q' to quit: ", limit=3, allowQuit=True)
        print()
        
        # Closes loop.
        if choice == "q":
            menuLoop = False

        # If the user chooses the first option, this block gets the board from user, prints the starting board, then iterates it.
        elif choice == 1:
            board = getBoard()
            print()
            underline("Starting Board")
            printBoard(board)
            iterateBoard(board)

        # If the user chooses the second option, the sub-menu is displayed and pre-built boards can be selected.
        elif choice == 2:

            # Sub-Menu/Board Selection Menu loop
            subMenuLoop = True
            while subMenuLoop:

                # Sub-menu heading and user instructions
                underline("Board Selection Menu")
                print("(1) Pulsar\n(2) Pentadecathlon\n(3) Octagon\n(4) Kok's Galaxy\n(5) Beluchenko Snowflake 1\n(6) Beluchenko 37-Period Galaxy")
                choice = getValid("choice", "Enter your choice or 'q' to quit to main menu: ", limit=7, allowQuit=True)

                # Closes loop.
                if choice == "q":
                    print()
                    subMenuLoop = False
                    
                # Reads in chosen board file, prints the starting board, then iterates it.
                else:
                    boardFile = patternSelector(choice)
                    board = patternReader(boardFile)
                    print()
                    underline("Starting Board")
                    printBoard(board)
                    iterateBoard(board)
                    
# Finally, main is called to run the program.
main()
