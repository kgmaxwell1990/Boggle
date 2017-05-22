from string import ascii_uppercase
from random import choice

def make_grid(height, width):
    return {(row, col): choice(ascii_uppercase)
                     for row in range(height)
                     for col in range(width)}

def neighbours_of_position(row,col):
    return [ (row - 1, col - 1), (row -1, col), (row - 1, col + 1), 
              (row, col - 1),                       (row, col + 1),
              (row + 1, col -1), (row + 1, col), (row + 1, col + 1)]

def all_grid_neighbours(grid):
    neighbours = {}
    for position in grid:
        row, col = position
        position_neighbours = neighbours_of_position(row, col)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours

def path_to_word(grid, path):
    return ''.join([grid[p] for p in path])
