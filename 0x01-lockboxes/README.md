# Lockboxes

This Python project provides a solution to the "lockboxes" problem, where you have a set of locked boxes, each containing keys to other boxes, and the task is to determine if all boxes can be opened.

## Description

The `canUnlockAll` function in the `0-lockboxes.py` file implements an algorithm to determine if all boxes can be opened. It performs a depth-first search (DFS) starting from the first box and checks if all boxes are reachable. If all boxes are reachable, it returns `True`; otherwise, it returns `False`.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed on your machine.
3. Import the `canUnlockAll` function from the `0-lockboxes.py` file.
4. Pass a list of lists representing the boxes to the `canUnlockAll` function.
5. The function will return `True` if all boxes can be opened, and `False` otherwise.

Example usage:

```python
from 0-lockboxes import canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

