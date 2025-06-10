"""
Nombre: Equipo los Bugs
Fecha: 10 de junio del 2025.

Descripción:

"""

import pygame
from Configurations import Configurations
from Media import Background

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

def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background) -> None:
    """
    Función que administra los elementos visuales del juego.
    """
    background.blit(screen)

    pygame.display.flip()

    clock.tick(Configurations.get_fps())