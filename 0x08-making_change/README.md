# 0x08 Making Change

This project tackles the classic coin change problem, where the objective is to determine the minimum number of coins needed to make a given total amount using a list of coin denominations.

## Requirements

- Python 3.4.3
- PEP 8 style (version 1.7.x)
- All files must be executable

## Files

- `0-making_change.py`: Contains the `makeChange` function implementation.
- `0-main.py`: Contains test cases to validate the `makeChange` function.

## Function Prototype

```python
def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given amount total.

    Parameters:
    coins (list): A list of integers representing the denominations of the coins.
    total (int): The total amount of money to be made with the coins.

    Returns:
    int: The fewest number of coins needed to meet the total.
         If the total is 0 or less, return 0.
         If the total cannot be met by any number of coins, return -1.
    """
## Usage
To test the makeChange function, run:
./0-main.py


### Execution
1. Ensure both `0-making_change.py` and `0-main.py` are executable:
    ```bash
    chmod +x 0-making_change.py 0-main.py
    ```

2. Run the test file:
    ```bash
    ./0-main.py
    ```

This structure separates the implementation from the testing and provides clear documentation on how to use and test the `makeChange` function.


## Example Output
makeChange([1, 2, 25], 37) = 7 (Expected: 7)
makeChange([1256, 54, 48, 16, 102], 1453) = -1 (Expected: -1)
makeChange([1, 5, 10, 25], 30) = 2 (Expected: 2)
makeChange([2], 3) = -1 (Expected: -1)
makeChange([1, 3, 4], 6) = 2 (Expected: 2)

