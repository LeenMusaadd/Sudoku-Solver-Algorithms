
import time
import copy

def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------------------------- ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")



def is_valid(board, row, col, num):
    # Check the row and column for the same number
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check the 3x3 subgrid for the same number
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def forward_checking(board, variables):
    # Iterate through the list of variables (empty cells) one by one
    for var in variables:
        row, col = var
        if board[row][col] == 0:
            # Try assigning numbers from 1 to 9 to the empty cell
            for num in range(1, 10):
                # Check if the assignment is valid (doesn't violate Sudoku constraints)
                if is_valid(board, row, col, num):
                    # If the assignment is valid, update the board with the number
                    board[row][col] = num
                    # Recursively call the forward_checking function with the updated board and variables
                    if forward_checking(board, variables):
                        return True  # Continue to the next variable if a solution is found

                    board[row][col] = 0 # If the recursive call does not lead to a solution, backtrack by resetting the cell
            return False # If no valid assignment is found for the current cell, return False
    return True # If all variables have been assigned values without conflicts, return True to indicate success

def backTrack(array):
    #sending the array to the assign value
    assignTheValue(array)
    for r in range(9):
        for c in range(9):
            if array[r][c] ==0:
                print("No sloution")

    print("Solve using Backtrack\n")
    print_sudoku(array)

def assignTheValue(array):
    # r = Row
    # c = Coulmn
    for r in range(9):
        for c in range(9):
            if array[r][c] == 0:#if the index was zero that means it is empty and we need to give it a uniqe value
                for value in range(1, 10):
                    if is_valid(array, r, c, value):
                        array[r][c] = value#in this step it will assiang the value that is vaild in this satution
                        if assignTheValue(array):
                            return True
                        else:
                            array[r][c] = 0#BT
                return False
    return True
def MAC(board):
    queue = []
    # Find all the empty cells and add them to the queue
    for i in range(9):
       for j in range(9):
           if board[i][j] == 0:
                queue.append((i, j))
    while queue:
        row, col = queue.pop(0)
        if board[row][col] == 0:
            # Try the possible numbers from 1 to 9.
            for num in range(1, 10):
                # If the number is valid, place it on the board.
                if is_valid(board, row, col, num):
                    board[row][col] = num
                    # Check if the modified board is still solvable.
                    if MAC(board) == True:
                        return True
                    # If the modified board isn't solvable, backtrack by deleting the number.
                    board[row][col] = 0
            # If no valid number can be placed at the current position, backtrack.
            return False
    # If we filled all the positions, return True. The board is solved.
    return True


def main():
    variables = [(i, j) for i in range(9) for j in range(9)] #list of variables for the forward checking algorithm
    #Enter the Sudoku puzzle below, with empty cells represented by 0
    initial_board = [
        [0, 7, 0, 1, 3, 0, 6, 8, 0],
        [0, 0, 2, 0, 0, 0, 0, 3, 0],
        [5, 3, 0, 7, 0, 4, 0, 0, 9],
        [0, 0, 3, 0, 2, 0, 0, 6, 0],
        [0, 0, 0, 9, 1, 5, 0, 0, 2],
        [0, 0, 4, 0, 8, 3, 1, 9, 0],
        [0, 0, 5, 0, 0, 0, 9, 0, 6],
        [7, 0, 0, 3, 4, 0, 8, 5, 0],
        [8, 9, 0, 0, 5, 6, 0, 7, 3]
    ]
    # Create a deep copy of the initial board
    deep_copy_board = copy.deepcopy(initial_board)
    # Now, deep_copy_board is an independent copy of the initial_board
    # Modifying deep_copy_board will not affect the original board.
    print("Input Sudoku")
    print_sudoku(initial_board)
    while True:
        print("Sudoku Solver Menu:")
        print("1. Solve Sudoku using Forward Checking")
        print("2. Solve Sudoku using Bactracking")
        print("3. Solve Sudoku using MAC ")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            start_time = time.perf_counter()
            if forward_checking(deep_copy_board,variables):
                end_time = time.perf_counter()
                print("Solve using Forward checking:")
                print_sudoku(deep_copy_board)
                print(f"Time taken: {end_time - start_time:.6f} Seconds")
                deep_copy_board = copy.deepcopy(initial_board) #resetting the deep_copy_board
            else:
                print("No solution exists.")

        elif choice == "2":
            start_time = time.perf_counter()
            backTrack(deep_copy_board)
            end_time = time.perf_counter()
            print(f"Time taken: {end_time - start_time:.6f} Seconds")
            deep_copy_board = copy.deepcopy(initial_board) #resetting the deep_copy_board

        elif choice == "3":
            start_time = time.perf_counter()
            if MAC(deep_copy_board):
                end_time = time.perf_counter()
                print("Solve using MAC:")
                print_sudoku(deep_copy_board)
                print(f"Time taken: {end_time - start_time:.6f} Seconds")
                deep_copy_board = copy.deepcopy(initial_board) #resetting the deep_copy_board
            else:
                print("No solution exists.")

        elif choice =="4":
            print("Thank you for using our solver!")
            break

if __name__ == "__main__":
    main()
