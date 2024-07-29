"""
functions.py

This module contains helper functions for the Conway's Game of Life simulation
using Pygame. The functions included are:

- `generate_cells(num)`: Generate a set of random cell positions.
- `get_neighbors(pos)`: Get the neighboring positions of a given cell position.
- `adjust_grid(positions)`: Adjust the grid according to Conway's Game of Life rules.
- `draw_grid(positions, screen)`: Draw the grid and the living cells on the screen.
"""

import random
import pygame
from variables import (
    GRID_LINE,
    CELL_ALIVE,
    WIDTH,
    HEIGHT,
    TILE_SIZE,
    GRID_WIDTH,
    GRID_HEIGHT,
)


def generate_cells(num):
    """
    Generate a set of random cell positions.

    Args:
        num (int): The number of cells to generate.

    Returns:
        set: A set of tuples representing the positions of the generated cells.
    """

    return set(
        [
            (random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT))
            for _ in range(num)
        ]
    )


def get_neighbors(pos):
    """
    Get the neighboring positions of a given cell position.

    Args:
        pos (tuple): A tuple representing the (x, y) position of the cell.

    Returns:
        list: A list of tuples representing the positions of neighboring cells.
    """
    x, y = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue

        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue

            neighbors.append((x + dx, y + dy))

    return neighbors


def adjust_grid(positions):
    """
    Adjust the grid based on the current state according to Conway's Game of Life rules.

    Args:
        positions (set): A set of tuples representing the current positions of living cells.

    Returns:
        set: A set of tuples representing the new positions of living cells after the adjustment.
    """
    all_neighbors = set()
    new_positions = set()

    # Checking if living cell is kept alive after iteration
    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)

        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) in [2, 3]:
            new_positions.add(position)

    # Checking if dead cell becomes alive after iteration
    for position in all_neighbors:
        neighbors = get_neighbors(position)
        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions


def draw_grid(positions, screen):
    """
    Draw the grid and the living cells on the screen.

    Args:
        positions (set): A set of tuples representing the positions of living cells.
        screen (pygame.Surface): The pygame surface on which to draw.
    """
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, CELL_ALIVE, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(
            screen, GRID_LINE, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE)
        )
    for col in range(GRID_WIDTH):
        pygame.draw.line(
            screen, GRID_LINE, (col * TILE_SIZE - 1, 0), (col * TILE_SIZE - 1, HEIGHT)
        )
