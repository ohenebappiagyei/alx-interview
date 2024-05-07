# Minimum Operations

This project provides a Python function to calculate the minimum number of operations needed to achieve a desired number of characters in a text file using only 'Copy All' and 'Paste' operations.

## Installation

No installation is required. Simply include the `minOperations` function in your Python script and call it with the desired number of characters as the argument.

## Usage

```python
def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve exactly n H characters 
    in a text file using only 'Copy All' and 'Paste' operations.

    Args:
        n (int): The desired number of H characters in the file.

    Returns:
        int: The minimum number of operations needed. If achieving n H characters is
             impossible, returns 0.
    """
    if n <= 1:
        return 0
    
    # Initialize an array to store the minimum operations for each number of characters
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(1, i):
            # Check if j divides i evenly
            if i % j == 0:
                # If it does, it means we can copy the characters formed in j operations
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n] if dp[n] != float('inf') else 0

# Example usage:
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
