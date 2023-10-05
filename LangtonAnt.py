# Author: Brent Thomas
# Date: 8/5/2021
# Description: This program makes a virtual Langton's Ant simulation based on input parameters of a square board size,
#              ant starting location, ant starting orientation, and the number of steps. Then prints out the resulting
#              game board with black("#") and white ("_") spaces and current ant location ("8").


def main():
    """This function is the main function of this program and starts by initializes an Ant in a
    specific location and direction and board size based on user inputs"""

    print("Welcome to the virtual Langton’s ant simulation!\n")
    print("""    This program makes a virtual Langton's Ant simulation based on input parameters of a square board size, 
    ant starting location, ant starting orientation, and the number of steps. Then prints out the resulting
    game board with black ('#') and white ('_') spaces and the current ant location ('8').\n""")

    print("First, please enter a number no larger than 100 for the size of the square board:")
    square_board_size = int(input())                                       # initializes the size of the gameboard
    print("Choose the ant’s starting location, please enter a number as the starting row number "
          "(where 0 is the first row from the top):")
    ant_start_location_row = int(input())  # initializes the ant start position row
    print("Please enter a number as the starting column number (where 0 is the first column from the left):")
    ant_start_location_col = int(input())                               # initializes the ant start position column
    print("Please choose the ant’s starting orientation, 0 for up, 1 for right, 2 for down, 3 for left:")
    ant_start_orientation = int(input())

    make_ant = Ant(ant_start_location_row, ant_start_location_col, ant_start_orientation)  # initializes the ant

    print("Please enter the number of steps for the simulation:")
    number_of_steps = int(input())                                  # accepts a number of steps for the ant to move

    initial_board = make_board(square_board_size)                 # initializes the blank board based on input parameter

    board = run_simulation(number_of_steps, ant_start_location_row, ant_start_location_col, ant_start_orientation, initial_board)
                                                                                               # runs the simulation
    print_board(board)   # passes the updated board to a program to print it out


class Ant:
    """This class makes an Ant based on Langton's Ant"""

    def __init__(self, ant_row, ant_col, ant_orientation):
        """This initializes the ant based on the parameters from the main function: start location, row and column,
        and ant orientation"""

        self._ant_start_location_row = ant_row
        self._ant_start_location_col = ant_col
        self._ant_start_orientation = ant_orientation


def make_board(board_size):
    """This initializes the square game board with all white spaces '_' based the input parameters"""

    board = []    # blank board

    for num in range(1, board_size + 1):
        row = []     # creates rows, each row will be a list, inside of the board list

        for number in range(1, board_size + 1):
            row.append("_")

        board.append(row)

    return board


def run_simulation(number_of_steps, ant_start_location_row, ant_start_location_col, ant_start_orientation, initial_board):
    """This runs the Langton's Ant simulation based on the input parameters"""

    counter = 0     # initialize counter to keep track of steps
    ant_row = ant_start_location_row
    ant_col = ant_start_location_col
    ant_orientation = ant_start_orientation
    board = initial_board

    while counter < number_of_steps:

        if board[ant_row][ant_col] == "_":   # checks if board space is white

            if ant_orientation == 3:     # changes ant orientation from 3 left to 0 up
                ant_orientation -= 3

            else:
                ant_orientation += 1
                # otherwise changes ant orientation 90 to the right, + 1
            board[ant_row][ant_col] = "#"  # changes the current ant location to "#" before moving

            ant_row, ant_col = ant_move(ant_row, ant_col, ant_orientation, board)  # this passes the current parameters
                                                                          # to a function to updates the ant's location
        else:  # otherwise assumes the space is black

            if ant_orientation == 0:   # changes ant orientation from 0 up to 3 left
                ant_orientation += 3

            else:
                ant_orientation -= 1       # otherwise changes ant orientation 90 to the left, - 1

            board[ant_row][ant_col] = "_"  # changes the current ant location to "_" before moving

            ant_row, ant_col = ant_move(ant_row, ant_col, ant_orientation, board)  # this passes the current parameters
                                                                            # to a function to update the ant's location
        counter += 1    # updates the counter to keep track of steps

    board[ant_row][ant_col] = "8"    # puts the ant, "8", at its last location on the game board
    return board


def ant_move(ant_row, ant_col, ant_orientation, board):
    """This function updates the location of the ant based on the inputs passed to it"""

    if ant_orientation == 0:
        if ant_row == 0:           # checks to see if the ant is at the edge of the board and flips it so the other side
            ant_row = (len(board) - 1)
        else:
            ant_row -= 1

    if ant_orientation == 1:
        if ant_col == (len(board) - 1):   # checks if the ant is on the edge
            ant_col = 0
        else:
            ant_col += 1

    if ant_orientation == 2:
        if ant_row == (len(board) - 1):    # checks edge condition
            ant_row = 0
        else:
            ant_row += 1

    if ant_orientation == 3:
        if ant_col == 0:
            ant_col = (len(board) - 1)
        else:
            ant_col -= 1

    return ant_row, ant_col


def print_board(board):
    """This prints the final board after running the simulation"""

    board_row = ""

    for row_list in board:

        for columne in row_list:
            if board_row == "":
                board_row = columne

            else:
                board_row += columne

        print(board_row)
        board_row = ""


if __name__ == '__main__':
    main()
