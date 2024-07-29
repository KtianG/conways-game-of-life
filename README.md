# Conway's Game of Life Simulation

This project is a simple implementation of Conway's Game of Life using Pygame. Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

## Features

- Simulation of Conway's Game of Life using Pygame
- Interactive grid where you can toggle cells by clicking
- Start, pause, and clear the grid using keyboard controls
- Randomly generate initial cell configurations

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/conways-game-of-life.git
    cd conways-game-of-life
    ```

2. Create a virtual environment and activate it (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the simulation:
    ```sh
    python main.py
    ```

2. Use the following controls to interact with the simulation:
    - **Mouse Click**: Toggle cell state (alive/dead)
    - **Spacebar**: Start/pause the simulation
    - **C key**: Clear the grid
    - **G key**: Generate a random initial configuration of cells

## Code Structure

- `main.py`: Contains the main loop and event handling for the simulation.
- `functions.py`: Contains helper functions for generating cells, getting neighbors, adjusting the grid, and drawing the grid.
- `variables.py`: Contains constant values used throughout the project.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Acknowledgements
- `Pygame`: - The library used for creating the graphical interface.
- `Conway's Game of Life`: - The inspiration for this project.
