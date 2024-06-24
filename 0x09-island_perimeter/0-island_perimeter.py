#!/usr/bin/python3
"""
This is the function that returns the perimeter of the island
described in grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.

    Args:
        grid (list of list of int): a 2D grid where 0 represents water
        and 1 represents land.

    Returns:
        int: The perimeter of the island.

    The function iterates over each cell in the grid. For each land cell (1),
    it checks its four neighbors (top, bottom, left, right) to determine if
    they are water or out of bounds, and increments the perimeter accordingly.
    """

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four possible sides
                if r == 0 or grid[r - 1][c] == 0:  # Check top
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # Check bottom
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # Check left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # Check right
                    perimeter += 1

    return perimeter
