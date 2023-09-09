import pygame, sys
from grid import Grid
from blocks import *

pygame.init()
dark_blue = (44,44,127)

# Definimos el tamaño de la pantalla y el nombre
screen =pygame.display.set_mode((300,600))
pygame.display.set_caption("Python Tetris")

# Declaramos el tiempo de pygame
clock = pygame.time.Clock()

# Importamos la classe Grid y la guardamos en la variable (Son todas las casillas del juego)
game_grid = Grid()

block = TBlock()

while True:
    # Declaramos un for para cerrar el juego
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)


    pygame.display.update()
    clock.tick(60)