#!/usr/bin/python3
"""
This is the makeChange function that calculates the coins
needed to make up a given total amount using a list of coin denominations
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given amount total.


    Parameters:
    coins (list): A list of integers representing the denominations of coins.
    total (int): The total amount of money to be made with the coins.

    Returns:
    int: The fewest number of coins needed to meet the total.
         If the total is 0 or less, return 0.
         If the total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    # Initialize dp array with infinity and set dp[0] to 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over all coins and update the dp array
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] still infinity, then total cannot be made with given coins
    return dp[total] if dp[total] != float('inf') else -1
