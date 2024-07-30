"""
variables.py

This module defines constants used in the Conway's Game of Life simulation
using Pygame. These constants include color definitions, screen dimensions,
grid settings, and frame rate.

Constants:
- `GRID_LINE` (tuple): The color of the grid lines in RGB format.
- `BACKGROUND` (tuple): The background color of the grid in RGB format.
- `CELL_ALIVE` (tuple): The color of the alive cells in RGB format.

Screen Dimensions:
- `WIDTH` (int): The width of the Pygame window.
- `HEIGHT` (int): The height of the Pygame window.

Grid Settings:
- `TILE_SIZE` (int): The size of each cell in the grid (in pixels).
- `GRID_WIDTH` (int): The number of columns in the grid, calculated as `WIDTH // TILE_SIZE`.
- `GRID_HEIGHT` (int): The number of rows in the grid, calculated as `HEIGHT // TILE_SIZE`.

Frame Rate:
- `FPS` (int): The frame rate for the Pygame window, controlling the simulation speed.
"""

GRID_LINE = (0, 0, 0)
BACKGROUND = (128, 128, 128)
CELL_ALIVE = (255, 255, 0)

WIDTH, HEIGHT = 1200, 1000
TILE_SIZE = 10
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
GENERATED_CELLS = GRID_WIDTH * GRID_HEIGHT // 20
FPS = 60
