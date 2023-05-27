This is a Python implementation of Numerical Tic Tac Toe game. It allows two players to take turns and make moves on a 3x3 grid. The goal of the game is for a player to create a line of three numbers that add up to 15, either horizontally, vertically, or diagonally.

Class Methods
The NumTicTacToe class provides the following methods:
__init__(): Initializes an empty Numerical Tic Tac Toe board.
drawBoard(): Displays the current state of the board.
squareIsEmpty(row, col): Checks if a given square is empty.
update(row, col, num): Assigns a number to the board at the provided row and column if the square is empty.
boardFull(): Checks if the board has any remaining empty squares.
isWinner(): Checks whether the current player has made a winning move.
