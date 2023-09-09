import pygame
from colors import Colors

# Creamos una clase para las casillas del juego
class Grid:
    # Definimos la cantidad de alto y ancho
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        # Las recorremos y le damos el valor 0 (que proximamente seran el valor de los colores).
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        # Harcodeamos las variables de los colores
        self.colors = Colors.get_cells_colors()

    # Funcion que imprime el valor (numero) de la grilla en la consola
    def print_grid(self):
        for row in range(self.num_cols):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def get_cell_colors(self):

        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (223, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]

    # Funcion para pintar la grilla en el juego
    def draw(self, screen):
        # Recorre todas las filas y columnas
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                # Guarda el valor en una variable
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)

                # Pinta dependiendo el valor de la variable
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)