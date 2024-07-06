# Source: https://www.geeksforgeeks.org/2048-game-in-python/

# Importing the logic.py file where all the functions located
import logic

# Driver code
if __name__ == '__main__':

    # calling the start_game function to initialize the matrix
    matrix = logic.start_game()
    print('')
    for i in range(len(matrix)):
        print(matrix[i])
    

while(True):

    # taking the user input for next step
    userInput = input("Your command: ")

    # the user moves up
    if(userInput == 'W' or userInput == 'w'):

        # call the 'up' function
        matrix, flag = logic.up(matrix)

        # get the current state and print it
        status = logic.get_current_state(matrix)
        print(status)

        # if game is not over then continue and add a new 2
        if(status == ''):
            logic.add_new_2(matrix)

        # else break the loop
        else:
            break

    # The above process will be followed in case of each type of moves below

    # the user moves down
    elif(userInput == 'S' or userInput == 's'):
        matrix, flag = logic.down(matrix)
        status = logic.get_current_state(matrix)
        print(status)

        if(status == ''):
            logic.add_new_2(matrix)
        else:
            break
    
    # the user moves left
    elif(userInput == 'A' or userInput == 'a'):
        matrix, flag = logic.left(matrix)
        status = logic.get_current_state(matrix)
        print(status)

        if(status == ''):
            logic.add_new_2(matrix)
        else:
            break

    # the user moves right
    elif(userInput == 'D' or userInput == 'd'):
        matrix, flag = logic.right(matrix)
        status = logic.get_current_state(matrix)
        print(status)

        if(status == ''):
            logic.add_new_2(matrix)
        else:
            break
    
    else:
        print("Invalid Key Pressed")

    # print the matrix after each move
    print('')
    for i in range(len(matrix)):
        print(matrix[i])