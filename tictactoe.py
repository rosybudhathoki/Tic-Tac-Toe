#----------------------------------------------------
# Numerical Tic Tac Toe class
# Author: Rosy Budhathoki
# Collaborators: None
# References: None
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
     
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        
        # shows 0 value grids as empty space
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    self.board[i][j] = ' '
                    
        #Prints the values from the grid as required for the game           
        print("   0   1   2  ")
        print('0  '+str(self.board[0][0]) + ' | ' + str(self.board[0][1]) + ' | ' + str(self.board[0][2]))
        print('  -----------')
        print('1  '+str(self.board[1][0]) + ' | ' + str(self.board[1][1]) + ' | ' + str(self.board[1][2]))
        print('  -----------')
        print('2  '+str(self.board[2][0]) + ' | ' + str(self.board[2][1]) + ' | ' + str(self.board[2][2]))
        
        # shows empty space value back to 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 0        
        

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        self.empty = False
        self.row = row
        self.col = col
        if self.board[self.row][self.col] == 0:
            self.empty = True
            self.update(row,col,num)
            
        return self.empty

    
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        self.num = num
        if self.empty == True:
            self.board[self.row][self.col] = self.num
            return self.board
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        self.full = False
        empty_digit = 0
        if empty_digit in self.board:
            self.full = True
        return self.full
        
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        first_index = 0   #This represents the first row/col
        middle_index = 1  #This represents the second row/col
        last_index = 2    #This represents the last row/col
        self.win = False
        
        # TO DO: delete pass and complete method
        
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][first_index]+self.board[i][middle_index]+self.board[i][last_index] == 15:   #checks for horizontal sum
                    self.win = True
                elif self.board[first_index][j]+self.board[middle_index][j]+self.board[last_index][j] == 15: #checks for vertical sum
                    self.win = True
                elif self.board[first_index][first_index]+self.board[middle_index][middle_index]+self.board[last_index][last_index] == 15:   #checks for diagonal sum from top left to bottom right
                    self.win = True
                elif self.board[first_index][last_index]+self.board[middle_index][middle_index]+self.board[last_index][first_index] == 15:   #checks for diagonal sum from top right to bottom left
                    self.win = True
        return self.win
            
     


if __name__ == "__main__":
    '''
    This is the main Program. It will create a new object myBoard and 
    check for all required conditions to see if a move is valid and check for a winner
    '''    
    
    myBoard = NumTicTacToe()
    myBoard.drawBoard()
    print('\n')
    
    #asks for input until the board is not full
    while not myBoard.boardFull():
        
        row = int(input('Row Number: '))
        col = int(input('Column Number: '))
        num = int(input('Number: '))   
        print('\n')
        
        #if a grid is empty, updates the grid and displays the new board
        if myBoard.squareIsEmpty(row,col):
            myBoard.update(row, col, num)
            myBoard.drawBoard()
            
        #if a player gets required three grids to equal to 15. The winner is decided and the game stops
        if myBoard.isWinner():
            break
            
