#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (list of lists): A list where each element is a list
    of integers representing the keys in each box.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited.add(current_box)
        for key in boxes[current_box]:
            if key < n and key not in visited:
                stack.append(key)

    return len(visited) == n
