# File: proj2.py
# Author: Nick Stommel
# Date: 12/03/15
# Section: Lab - 24, Lecture - 19
# Email: stommel1@umbc.edu
# Description: This program is designed to autofill empty spaces in a board recursively. The board itself is read in from a text file and 
# converted to a 2D list for processing.

# readBoard: This function reads in a boardfile, converting to and returning a 2D list.
# Inputs: the board file
# Outputs: 2D board list
def readBoard(boardFile):
    board = []
    for line in boardFile:
        row = []
        for char in line:
            if char != "\n":
                row.append(char)
        board.append(row)
    
    return board

# printBoard: This function prints a board in the terminal using a 2D board list.
# Inputs: the 2D board list
# Outputs: the printed board
def printBoard(board):
    for row in board:
        for cell in row:
            print(cell, end="")
        print()

# fill: This function fills an empty space recursively.
# fill() takes five arguments, which include the coordinate row and column, the board itself, the character chosen by the user,
# and the boolean showstep which controls the printing of the board.
# Inputs: row, column, board, char, showstep
# Outputs: the printed board and final returned board
def fill(row, column, board, char, showstep):
    
    # If statement prevents function from filling out of bounds and from attempting to fill a full space.
    if row > 0 and row < len(board)-1 and column > 0 and column < len(board[0])-1 and board[row][column] == " ": 

        # If the user wants, every step of the recursion is printed.
        if showstep:
            printBoard(board)

        # Change the space to the character.
        board[row][column] = char
        
        # move up
        fill(row - 1, column, board, char, showstep)
        # move right
        fill(row, column + 1, board, char, showstep)
        # move down
        fill(row + 1, column, board, char, showstep)
        # move left
        fill(row, column - 1, board, char, showstep)
    
    # Finally, the last board is returned.
    return board

# main: This function ties together the program and calls the above functions. Most of main is designed to obtain valid user input
# using try-except. 
# Inputs: file name, coordinate, print choice
# Outputs: printed board, printed error statements. 
def main():
    
    # Program identifier
    heading = "Board Autofill Program"
    # underlines heading
    print("\n" + heading + "\n" + "-" * len(heading))
    
    # try, except used inside a while loop to reprompt the user if a FileNotFoundError is raised.
    invalid = True
    while invalid:
        try:
            boardFilename = input("Enter board file name: ")
            boardFile = open("board_patterns_proj2/" + boardFilename)
            board = readBoard(boardFile)
            invalid = False
            
        except FileNotFoundError:
            # If the file does not exist, check to see whether the filename ends in '.dat' or '.txt'.
            if boardFilename[-4:] != ".dat" and boardFilename[-4:] != ".txt":
                print("Invalid file name, enter a file name that ends in '.txt' or '.dat'.")
            # If the file ends in the correct extension, but does not exist, prints file does not exist.
            else:
                print("File does not exist.")

    # While loop used to reprompt the user for a coordinate once an empty area is filled. 
    loop = True
    while loop:
            
        print()

        # try, except used to reprompt the user for a coordinate if an IndexError or ValueError is raised when a coordinate is input incorrectly. 
        invalid = True
        while invalid:
            try:
                coordinate = input("Enter a coordinate to start filling at in the form 'row,column' or 'q' to quit: ")
                if coordinate != "q":
                    coordinate = coordinate.split(",")
                    row = int(coordinate[0])
                    col = int(coordinate[1])
                    # Following if/elif statements used to rule out coordinates that are out of bounds or already occupied by part of the board.
                    if row < 0 or col < 0:
                        print("\nNegative values are invalid, enter two positive integers separated by a comma.\n")
                    elif row > (len(board)-1) or col > (len(board[0])-1):
                        print("\nThese coordinate values do not exist, input is too large.\nRows and columns are numbered starting from zero.\nThe board is " + 
                              str(len(board)) + " rows high and " + str(len(board[0])) + " columns wide.\n")
                    elif board[row][col] != " ":
                        print("\nThis coordinate is already occupied by an element of the board itself, choose an empty space.\n")
                    # Otherwise, if the coordinate is valid, keep the coordinate value and close the loop.
                    else:
                        invalid = False
                # If the user inputs 'q', keep 'q' and close the loop.
                else:
                    invalid = False

            except (IndexError, ValueError):
                print("\nInvalid input, enter two integers separated by a comma.\n")

        
        if coordinate != "q":

            # While loop used to reprompt the user for a valid character.
            invalid = True
            while invalid:
                char = input("Enter in a character to fill the space with: ")
                if len(char) > 1:
                    print("\nPlease enter a single character.\n")
                    
                # Accounting for whether the character is the same as an empty space is necessary, otherwise the program crashes.
                elif char == " ":
                    print("A space is an invalid character.")
                    
                else:
                    invalid = False

            # While loop used to reprompt the user for a valid choice for showing every step of the recursion.
            invalid = True
            while invalid:
                choice = input("Do you want to show each step of the recursion? (Enter 'yes' or 'no'): ")
                if choice not in ["yes", "y", "no", "n"]:
                    print("\nInvalid choice, enter 'yes' or 'no'.\n")
                else:
                    if choice == "yes" or choice == "y":
                        showstep = True
                    else:
                        showstep = False

                    invalid = False

            # print the final board returned from fill()
            printBoard(fill(row, col, board, char, showstep))
        
        # If the user enters in 'q' for the coordinate, the main while loop is closed.   
        else:
            loop = False

# Finally, call main()
main()
