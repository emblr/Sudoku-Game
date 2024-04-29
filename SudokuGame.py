import pygame as pg

BLACK = (0, 0, 0)
RED = (255, 0, 0)

class SudokuGrid:
    def __init__(self):
        # Initialize an empty grid with colors
        self.grid = [[(0, None) for _ in range(9)] for _ in range(9)]

    def set_value(self, row, col, value, color):
        # Set the value and color at the specified row and column
        self.grid[row][col] = (value, color)

    def solve_grid(self, solution):
        # Set the grid values to the solution
        for row_index, row in enumerate(solution):
            for col_index, value in enumerate(row):
                if value != 0:
                    self.grid[row_index][col_index] = (value, RED)

    def get_value(self, row, col):
        # Get the value and color at the specified row and column
        return self.grid[row][col]

    def display(self, screen, cell_size):
        # Display the grid
        for row_index, row in enumerate(self.grid):
            for col_index, (value, color) in enumerate(row):
                # Render the value at the specified row and column with color
                font = pg.font.Font(None, 36)
                text = font.render(str(value), True, color)
                # Center the text within the cell
                text_rect = text.get_rect(center=(col_index * cell_size + cell_size // 2, row_index * cell_size + cell_size // 2))
                # Draw the text on the screen
                screen.blit(text, text_rect)

    def grid_matches(self, solved_grid):
        # Check if the current grid matches the solved grid
        for i in range(9):
            for j in range(9):
                if self.grid[i][j][0] != solved_grid[i][j]:
                    return False
        return True

class Button:
    def __init__(self, x, y, width, height, color, text=''):
        # Initialize button attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text

    def draw(self, screen, outline=None):
        # Draw the button on the screen
        if outline:
            # Draw button outline
            pg.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        # Draw button rectangle
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            # Render text on the button
            font = pg.font.Font(None, 24)
            text = font.render(self.text, 1, (0, 0, 0))
            # Center the text within the button
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        # Check if the specified position is over the button
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
