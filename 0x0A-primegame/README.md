# Prime Game

This project simulates a game played by Maria and Ben. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file is mandatory
- Code must follow PEP 8 style (version 1.7.x)
- All files must be executable

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your_username/alx-interview.git

2. Navigate to the project directory:
    ```sh
    cd alx-interview/0x0A-primegame

## Usage
To use the program, create a Python script with the following content:

```
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Expected output: "Ben"
```

Make the script executable:
```sh
chmod +x main_0.py
```
Run the script:
```sh
./main_0.py
```

## Example
The following example demonstrates how to determine the winner of multiple rounds:

```
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(3, [4, 5, 1])))  # Output: "Ben"
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Output: "Ben"
```

# Explanation
The isWinner function determines the winner of each round based on the given rules. Maria and Ben take turns picking prime numbers and removing them and their multiples from the set. The player who cannot make a move loses the game. The function returns the name of the player who won the most rounds.

# Files
- `0-prime_game.py`: Contains the implementation of the `isWinner` function.
- `README.md`: Provides an overview of the project, usage instructions, and examples.
- `main_0.py`: Example script to test the function.

# Author
This project was implemented as part of the ALX software engineering program.

