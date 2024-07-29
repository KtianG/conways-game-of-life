"""
    Simple Conway's game of life simulation using pygame.
"""

import random
import pygame
from variables import (
    BACKGROUND,
    WIDTH,
    HEIGHT,
    TILE_SIZE,
    GRID_WIDTH,
    FPS,
)
from functions import generate_cells, adjust_grid, draw_grid

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
    """
    Main loop for the Conway's Game of Life simulation.

    This function initializes the game state and enters the main event loop,
    handling user inputs and updating the display based on the game rules.
    """
    running = True
    playing = False
    count = 0
    update_frequency = 30

    positions = set()

    while running:
        clock.tick(FPS)

        if playing:
            count += 1
            if count >= update_frequency:
                count = 0
                positions = adjust_grid(positions)

        pygame.display.set_caption("Playing" if playing else "Paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                    count = 0
                if event.key == pygame.K_c:
                    positions = set()
                    count = 0
                    playing = False
                if event.key == pygame.K_g:
                    count = 0
                    positions = generate_cells(random.randrange(5, 10) * GRID_WIDTH)

        screen.fill(BACKGROUND)
        draw_grid(positions, screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
