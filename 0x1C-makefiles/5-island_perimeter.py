#!/usr/bin/python3
""" 5-island_perimeter.py
This module is used to return the perimeter of an
island described in grid:
- grid is a list of integers where:
    - 0 represents a water zone
    - 1 represents a land zone
    - One cell is a square with side length 1
    - Grid cells are connected horizontally/vertically
      (not diagonally)

- Grid is rectangular, width and height don't exceed 100

- The island doesn't have "lakes"
  (water that isn't connected to the water around the island)
"""


def island_perimeter(grid):
    """ island_perimeter function """
    perimeter = 0

    nrow = len(grid)

    if grid != []:
        ncolumn = len(grid[0])

    for a in range(nrow):
        for b in range(ncolumn):
            if grid[a][b] == 1:
                if (a - 1) == -1 or grid[a - 1][b] == 0:
                    perimeter += 1
                if (a + 1) == nrow or grid[a + 1][b] == 0:
                    perimeter += 1
                if (b - 1) == -1 or grid[a][b - 1] == 0:
                    perimeter += 1
                if (b + 1) == ncolumn or grid[a][b + 1] == 0:
                    perimeter += 1

    return perimeter
