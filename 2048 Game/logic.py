# Source: https://www.geeksforgeeks.org/2048-game-in-python/

# This file needs to be imported into 2048.py file

# Importing random package to generate random numbers
import random

# This function is to initialize game / grid 
# at the beginning
def start_game():

    # delcaring an empty list then
    # appending 4 list each with four elements as 0
    matrix = []
    for i in range(4):
        matrix.append([0] * 4)
    
    # printing controls and how to play
    print("Commands:")
    print("'W' or 'w': Move Up")
    print("'S' or 's': Move Down")
    print("'A' or 'a': Move Left")
    print("'D' or 'd': Move Right")

    # calling the function to add a new 2 at a
    # random spot in the grid after every step
    add_new_2(matrix)
    return matrix


# Function to add a new 2 in the grid
# at a random empty cell
def add_new_2(matrix):

    # choosing a random index for row and column
    row = random.randint(0, 3)
    column = random.randint(0, 3)

    # while loop will break as the random cell chosen
    # will be empty (or contains zero)
    while(matrix[row][column] != 0):
        row = random.randint(0, 3)
        column = random.randint(0, 3)

    # Place a '2' at that empty random cell
    matrix[row][column] = 2


# Function to get the current state of the game
def get_current_state(matrix):

    # if any cell contains 2048: you won
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] == 2048):
                return 'YOU WON!'

    # if there are still left with at least one empty
    # cell, then game is not over yet
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] == 0):
                return ''

    # If no cell is empty now, but if after any move 
    # left, right, up or down; if any two cells gets
    # merged and creates an empty cell then game is 
    # also not over
    for i in range(3):
        for j in range(3):
            if(matrix[i][j] == matrix[i+1][j] or matrix[i][j] == matrix[i][j+1]):
                return ''

    for j in range(3):
        if(matrix[3][j] == matrix[3][j+1]):
            return ''

    for i in range(3):
        if(matrix[i][3] == matrix[i+1][3]):
            return ''

    # Else, you lost the game
    return 'YOU LOST!'


# ---All the functions below are for left swap initially---

# Function to compress the grid after every step before and
# after merging cells
def compress(matrix):

    # bool variable to determine if any change happened or not
    change = False

    # empty grid
    new_matrix = []

    # with all cells empty
    for i in range(4):
        new_matrix.append([0] * 4)

    # we will shift entries of each cell to it's extreme
    # left row by row
    # loop to traverse rows
    for i in range(4):
        position = 0

        # loop to traverse each column in respective row
        for j in range(4):
            if(matrix[i][j] != 0):

                # if cell is not empty then we will shift
                # it's number to previous empty cell in that
                # row denoted by 'position' variable
                new_matrix[i][position] = matrix[i][j]

                if(j != position):
                    change = True
                position += 1

    # returning new compressed matrix and the flag vairable
    return new_matrix, change


# Function to merge the cells in matrix after compressing
def merge(matrix):

    change = False
    
    for i in range(4):
        for j in range(3):

            # if current cell has the same value as 
            # next cell in the row and they are non
            # empty then
            if(matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0):

                # double current cell value and empty the next cell
                matrix[i][j] = matrix[i][j] * 2
                matrix[i][j+1] = 0

                # make bool variable become True, indicating the
                # new grid after merging is different
                change = True
    
    return matrix, change


# Function to reverse the matrix, means reversing the content
# of each row (reversing the sequence)
def reverse(matrix):
    
    new_matrix = []
    for i in range(4):
        new_matrix.append([])
        for j in range(4):
            new_matrix[i].append(matrix[i][3-j])
    
    return new_matrix


# Function to get the transpoe of matrix, means interchanging
# rows and columns
def transpose(matrix):

    new_matrix = []
    for i in range(4):
        new_matrix.append([])
        for j in range(4):
            new_matrix[i].append(matrix[j][i])
    
    return new_matrix


# Function to update the matrix when move LEFT
def left(grid):

    # first compress the grid
    new_grid, changed1 = compress(grid)

    # then merge the cells
    new_grid, changed2 = merge(new_grid)

    changed = changed1 or changed2

    # again, compress after merging
    new_grid, temp = compress(new_grid)

    # return new matrix and bool 'changed' telling
    # whether the grid is same or different
    return new_grid, changed


# Function to update the matrix when move RIGHT
def right(grid):

    # to move right we just reverse the matrix
    new_grid = reverse(grid)

    # then move left
    new_grid, changed = left(new_grid)

    # then again reverse matrix will give us desired result
    new_grid = reverse(new_grid)
    return new_grid, changed


# Function to update the matrix when move UP
def up(grid):

    # to move up we just take transpose of matrix
    new_grid = transpose(grid)

    # then move left (calling all included functions) then
    new_grid, changed =  left(new_grid)

    # again take transpose will give desired results
    new_grid = transpose(new_grid)
    return new_grid, changed


# Function to update the matrix when move DOWN
def down(grid):

    # to move down we take transpose
    new_grid = transpose(grid)

    # move right and then again
    new_grid, changed = right(new_grid)

    # take transpose will give desired results
    new_grid = transpose(new_grid)
    return new_grid, changed


# This file only contains all the logic functions to be
# called in the main function present in 2048.py