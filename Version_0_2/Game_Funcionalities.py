"""
Nombre: Equipo los Bugs
Fecha: 09 del 2025.

"""

import pygame
from Configurations import Configurations

def game_events() -> bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin del juego.
    """
    game_over = False

    #Revisamos todos los eventos generados por el usuario.
    for event in pygame.event.get():
        #Si el usuario cierra la ventana, indicamos que se debe terminar el juego.
        if event.type == pygame.QUIT:
            game_over = True

    return game_over

def screen_refresh(screen: pygame.surface.Surface) -> None:
    """
    Función que administra los elementos visuales del juego.
    """
    #Rellenamos la pantalla con el color de fondo configurado.
    screen.fill(Configurations.get_background())

    pygame.display.flip()