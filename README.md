# CMSC_201_Python_List_Processing_Projects

# Conway's Game of Life Project
The proj1.py program is an automated version of the algorithm Conway's Game of Life, complete with a test library of pre-built board patterns and a menu interface. It reads patterns from text files found in the board_patterns_proj1 directory. Boards are printed in blue unicode dots and also shown in pure list format when the program is run in a terminal.

For this project, you will be coding a simple cellular automata game, called
Conway's Game of Life. In this game, you have a grid where pixels can
either be on or off (dead or alive). In the game, as time marches on, there
are simple rules that govern whether each pixel will be on or off (dead or
alive) at the next time step. These rules are as follows:
Any live cell with fewer than two live neighbors dies.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies.
Any dead cell with exactly three live neighbors becomes a live cell.
To begin, you will ask the user for the size of the game board (rows first, then
columns). Next prompt them for any cells they would like to be “alive” when the
game begins. Finally, ask the user how many iterations of the game (number of
time steps) they would like to see run. You should then display these iterations.
“Live” cells are to be represented with the character “A” (capital ‘a’), and “dead”
cells are to be represented with the character “.” (a period).

# Auto-fill Recursive Function Project
The proj2.py program is designed to autofill empty spaces in a 2D board (a nested list) recursively with a provided character, the results of which are shown in terminal. The board itself is read in from a text file and is converted to a 2D list for processing. Each step of the recursion can be shown if that option is selected during runtime.

Prompt:

CMSC 201 – Computer Science I for Majors Page 2
Details
For this project, you will be implementing a tool called “Auto-fill”. If you’ve
ever used a basic image editing software (like MS Paint), you’ve likely seen a
similar function.
You will be given a text file full of characters that form an enclosed set of
spaces.
The grid may be any size, but will always be fully enclosed (there will be a
“border” of characters along the outer edges).
Your autofill program will ask the user to provide a point in the grid, and will
“fill” the entire space it belongs to using a character, also provided by the
user.
A space in the grid is only empty if it is occupied by a space character
(“ ”). All other characters count as the space being occupied.
