def pascal_triangle(n):
    """
    This function generates Pascal's triangle up to a given number of rows (n).

    Args:
        n: An integer representing the number of rows in the Pascal's triangle.
    Returns:
        A list of lists containing the elements of the Pascal's triangle.
            An empty list is returned if n <= 0.
    """


if n <= 0:
    return []

# Initialize with the first row (1)
triangle = [[1]]

for i in range(1, n):
    # Build the next row by summing adjacent elements from the previous row
    next_row = [1]
    for j in range(1, i):
        next_row.append(triangle[i-1][j-1] + triangle[i-1][j])
    # End with 1 for each row
    next_row.append(1)
    triangle.append(next_row)

return triangle
