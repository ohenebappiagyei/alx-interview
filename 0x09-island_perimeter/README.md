# Island Perimeter

## Description

The "Island Perimeter" project involves developing a function in Python to calculate the perimeter of an island represented in a 2D grid. The grid is a list of lists where `0` represents water and `1` represents land. The task is to apply knowledge of algorithms, data structures (specifically matrices or 2D lists), and conditional logic to solve this geometric problem within a grid context.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Code Explanation](#code-explanation)
- [References](#references)

## Requirements

- Python 3.4.3 or later
- Compatible with Ubuntu 20.04 LTS
- The code follows the PEP 8 style guide (version 1.7)
- No external modules or libraries are allowed
- All files must be executable

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/island_perimeter.git
    ```

2. **Navigate to the project directory:**

    ```sh
    cd island_perimeter
    ```

## Usage

1. **Ensure the Python file is executable:**

    ```sh
    chmod +x 0-island_perimeter.py
    ```

2. **Run the main script to test the function:**

    ```sh
    ./0-main.py
    ```

## Example

Given the following grid:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

### Code Explanation
island_perimeter(grid)
This function calculates the perimeter of an island represented in a 2D grid.

Arguments:
grid (list of list of int): A 2D grid where 0 represents water and 1 represents land.
Returns:
int: The perimeter of the island.
Description:
The function iterates over each cell in the grid.
For each land cell (1), it checks its four neighbors (top, bottom, left, right).
If a neighbor is water (0) or out of bounds, it contributes to the perimeter.
The perimeter is incremented based on the number of such conditions.

### Script Explanation
The 0-main.py script demonstrates the usage of the island_perimeter function by providing a sample grid and printing the calculated perimeter.

#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
