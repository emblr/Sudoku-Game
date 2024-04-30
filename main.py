import pygame as pg
import sys
from SudokuGame import SudokuGrid, Button
import random

# Initialize pygame
pg.init()

icon = pg.image.load('icon.png')  # Load your icon image
pg.display.set_icon(icon)  # Set the icon for the window


# Load calm music
pg.mixer.music.load('calm.mp3')

# Set volume (optional)
pg.mixer.music.set_volume(0.5)  # Adjust volume between 0 and 1

# Play the music on loop (-1 indicates loop indefinitely)
pg.mixer.music.play(-1)


# Pygame setup
pg.init()
screen_width = 540
screen_height = 630  # Adjusted height to remove excess space at the bottom
screen = pg.display.set_mode((screen_width, screen_height))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)




# Define cell_size
cell_size = screen_width // 9

# Buttons
solve = Button(25, 560, 100, 50, RED, 'Solve')
check = Button(220, 560, 100, 50, RED, 'Check')
quitGame = Button(415, 560, 100, 50, RED, 'Quit')

# Define pre-made grids
grids = [[
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]],
    [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 6],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 5, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]],
    [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]],
    [
    [5, 0, 0, 0, 0, 7, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 7],
    [0, 0, 0, 6, 0, 9, 0, 0, 0],
    [0, 7, 0, 9, 8, 0, 6, 0, 0],
    [9, 0, 3, 0, 0, 4, 0, 6, 0],
    [8, 0, 7, 4, 0, 0, 0, 0, 0],
    [6, 2, 5, 0, 1, 0, 0, 0, 4],
    [4, 0, 0, 2, 0, 0, 3, 0, 0]],

    [
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 6, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 1, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3]
]

]



solved_grid = [
    [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]],
    [
    [3, 7, 6, 5, 1, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 6],
    [4, 8, 7, 6, 5, 2, 9, 3, 1],
    [6, 1, 3, 7, 4, 5, 5, 8, 9],
    [9, 6, 2, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 9, 2, 7, 6, 1, 3],
    [1, 3, 8, 9, 7, 4, 2, 5, 6],
    [7, 9, 4, 3, 8, 6, 5, 7, 4],
    [2, 4, 5, 2, 9, 1, 3, 6, 8]],
    [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 3, 9, 4],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 7, 4, 5, 3],
    [3, 5, 4, 6, 8, 2, 9, 1, 7],
    [9, 7, 1, 3, 4, 5, 2, 6, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 3, 6, 1, 3],
    [7, 6, 3, 4, 1, 8, 5, 2, 9]],
    [
    [5, 1, 9, 8, 6, 7, 4, 2, 3],
    [7, 8, 2, 3, 4, 1, 5, 9, 6],
    [3, 4, 6, 5, 9, 2, 8, 1, 7],
    [2, 3, 8, 6, 5, 9, 7, 4, 1],
    [1, 7, 4, 9, 8, 3, 6, 5, 2],
    [9, 5, 3, 1, 2, 4, 7, 6, 8],
    [8, 9, 7, 4, 3, 5, 2, 6, 1],
    [6, 2, 5, 7, 1, 8, 9, 3, 4],
    [4, 6, 1, 2, 7, 6, 3, 8, 5]],
    [
    [1, 8, 3, 6, 7, 5, 9, 4, 2],
    [2, 4, 7, 9, 1, 3, 6, 5, 8],
    [5, 6, 9, 4, 8, 2, 3, 7, 1],
    [6, 1, 7, 8, 4, 9, 5, 2, 3],
    [4, 9, 8, 3, 5, 7, 2, 1, 6],
    [7, 3, 2, 5, 6, 1, 1, 8, 9],
    [8, 2, 5, 1, 3, 9, 7, 6, 4],
    [3, 7, 6, 2, 9, 4, 8, 3, 5],
    [9, 5, 1, 7, 2, 8, 4, 9, 3]]
]

# Sudoku grid setup
grid = SudokuGrid()
grid_index = random.randint(0, 4)  # Select a random grid index


# Fill Sudoku grid with pre-made values
for row_index, row in enumerate(grids[grid_index]):
    for col_index, value in enumerate(row):
        if value != 0:
            grid.set_value(row_index, col_index, value, BLACK)  # Set pre-made values in red
        else:
            grid.set_value(row_index, col_index, '', RED)  # Set empty cells in black

# Main loop
running = True
selected_cell = None

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pg.mouse.get_pos()
                # Check if mouse click is within Sudoku grid
                if 0 <= mouse_pos[0] < 9 * cell_size and 0 <= mouse_pos[1] < 9 * cell_size:
                    row = mouse_pos[1] // cell_size
                    col = mouse_pos[0] // cell_size
                    selected_cell = (row, col)
                else:
                    selected_cell = None
                # Check button clicks
                if solve.is_over(mouse_pos):
                    grid.solve_grid(solved_grid[grid_index])  # Solve the grid
                elif quitGame.is_over(mouse_pos):
                    running = False  # Quit the game
                elif check.is_over(mouse_pos):
                    if grid.grid_matches(solved_grid[grid_index]):  # Check if grid matches solution
                        print('Congratulations! You solved the Sudoku puzzle!')
                    else:
                        print('Oops! Something went wrong. Keep trying!')
        elif event.type == pg.KEYDOWN:
            if selected_cell is not None:
                row, col = selected_cell
                if event.key == pg.K_BACKSPACE:  # Handle backspace key
                    if grids[grid_index][row][col] == 0:  # Check if cell is empty
                        grid.set_value(row, col, '', RED)  # Set value to empty
                elif pg.K_1 <= event.key <= pg.K_9:  # Handle numeric keys
                    input_number = int(pg.key.name(event.key))
                    if grids[grid_index][row][col] == 0:  # Check if cell is empty
                        grid.set_value(row, col, input_number, RED)  # Set input number

    # Fill screen with white
    screen.fill(WHITE)

    # Draw grid lines
    for i in range(10):
        thickness = 6 if i % 3 == 0 else 3
        pg.draw.line(screen, BLACK, (0, i * cell_size), (screen_width, i * cell_size), thickness)
        pg.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, screen_height - 92), thickness)

    # Display Sudoku grid
    grid.display(screen, cell_size)

    # Draw buttons
    quitGame.draw(screen)
    solve.draw(screen)
    check.draw(screen)

    # Update display
    pg.display.update()

# Quit Pygame
pg.quit()
sys.exit()
