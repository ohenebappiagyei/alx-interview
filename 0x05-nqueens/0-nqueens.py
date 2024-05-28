#!/usr/bin/python3
"""
This function is to solve the n-queens problem
"""
import sys


def print_usage_and_exit():
    """
    Print the usage message and exit the program with status 1.
    """
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message):
    """
    Print an error message and exit the program with status 1.

    Args:
        message (str): The error message to print.
    """
    print(message)
    sys.exit(1)


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the board position (row, col).

    Args:
        board (list): The board represented as a list
        where the index is the row
                      and the value is the column of the placed queen.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem and return all possible solutions.

    Args:
        n (int): The size of the chessboard (n x n) and the number of queens.

    Returns:
        list: A list of solutions, where each solution is represented as a list
              of column positions for each row.
    """
    def solve(row):
        """
        Recursive function to solve the N-Queens problem using backtracking.

        Args:
            row (int): The current row to place a queen.
        """
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    board = [-1] * n  # Initialize the board
    solutions = []    # List to store all the solutions
    solve(0)          # Start solving from the first row
    return solutions


def print_solutions(solutions):
    """
    Print all solutions in the specified format.

    Args:
        solutions (list): A list of solutions to the N-Queens problem.
    """
    for solution in solutions:
        formatted_solution = []
        for i in range(len(solution)):
            formatted_solution.append([i, solution[i]])
        print(formatted_solution)


def main():
    """
    Main function to handle input,
      solve the N-Queens problem, and print solutions.
    """
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if N < 4:
        print_error_and_exit("N must be at least 4")

    solutions = solve_nqueens(N)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
