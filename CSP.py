# Name: Amit Singh
# File: CSP.py
# Date: 11.7.2016
# Desciption: This file contains implementation for a sudoku solver. It uses recursion to handle all the bookkeeping.
#   Essentialy, this uses DFS using the OS's stack as the graph, and each individual stack frame as a node

import sys

# returns true if move would be unique in its row, column, and unit; false otherwise
def unique(board, pos, move):
    return False if move in board[(pos//9)*9:((pos//9)*9+9)] or move in board[(pos%9)::9] or move in [ a for b in [ board[27*(pos//27)+3*int(pos%9>2)+3*int(pos%9>5)+i*9:27*(pos//27)+3*int(pos%9>2)+3*int(pos%9>5)+3+i*9] for i in range(3) ] for a in b ] else True


# recursively gets the next open position in the board starting from position pos. returns -1 if the position is above 80.
# which represeents the end of the board
def get_next(board, pos=0):
    if pos > 80: return -1
    return get_next(board, pos+1) if board[pos] != '-' else pos


# recrusive sudoku function. solves sudoku puzzle by using DFS, essentially. starting at the first open node, 
# try to fill in numbers in the board (if they're unique in their row, column, and unit) and then call the 
# function on the next position. 

# When the base case is reached, a true will be returned, and propogated up, which stops the recursion
# if all numbers 1-9 are tried, the position is reset to an empty space, and then a false is returned.
# The false is propogated up, forcing the previous empty position to try other numbers. If it tries all
# numbers 1-9, the same process is repeated (backtracking)
def sudoku(board, pos=0):

    # call get next on the position (recursive call uses the current position, so this is necessary
    # also prevents sudoku() being called on a filled position
    if board[pos] != "-": pos = get_next(board, pos)
    
    # base case - print the solution, and return true
    if pos == -1:               
        for i in range(9):
            for j in range(9):
                print(board[9*i + j], end="")
            print()
        return True        

    # domain is used to map the integers to a string (since thats how the board is stored)
    domain = "-123456789"            

    # recurive case - loop through all possible numbers. For the first valid one that you find,
    #   call sudoku() on the next position. Propogate true if it is returned (AKA the end of the board
    #   is reached and a solution has been found). If a false is returned, reset the position and try 
    #   the rest of the domain before returning a false (signalling the previous empty position to 
    #   backtrack
    for i in range(1,10):        
        if (unique(board, pos, domain[i])):
            board[pos] = domain[i]
            if sudoku(board, pos):
                return True 
            board[pos] = '-'
    return False


# board is a 1D list of all positions. Entries are stored as strings rather than ints (just for simplicity)
sudoku([ a for b in [line.strip() for line in open(sys.argv[1])] for a in b] )
