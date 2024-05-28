# 0x05. N Queens

## Project Description

The N Queens project is a classic problem in computer science and mathematics. The challenge is to place N non-attacking queens on an N×N chessboard. This project involves implementing a solution using the backtracking algorithm to find all possible configurations for the given N.

## Usage

```sh
./0-nqueens.py N

N must be an integer greater than or equal to 4.
The program prints every possible solution, one solution per line.
Solutions are not required to be printed in a specific order.

## Example
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]


## Requirements
The program should be implemented in Python.
Only the sys module is allowed to be imported.

## Error Handling
If the user provides the wrong number of arguments, print:
Usage: nqueens N
and exit with status 1.

If N is not an integer, print:
N must be a number
and exit with status 1.

If N is less than 4, print:
N must be at least 4

N must be at least 4
and exit with status 1.

## Implementation Details
### Functions
`print_usage_and_exit()`: Prints the usage message and exits the program.
`print_error_and_exit(message)`: Prints the specified error message and exits the program.
`is_safe(board, row, col)`: Checks if it's safe to place a queen at the specified row and column.
`solve_nqueens(n)`: Solves the N Queens problem and returns all possible solutions.
`print_solutions(solutions)`: Prints all solutions in the specified format.


## Main Algorithm
The main algorithm uses a backtracking approach to place queens on the board row by row, ensuring that no two queens can attack each other. The algorithm checks for safety before placing each queen and backtracks if a valid configuration is not found.

Authors
Dr. Appiagyei - For ALX
