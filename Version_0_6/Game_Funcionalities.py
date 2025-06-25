"""
Nombre: Equipo los Bugs
Fecha: 10 de junio del 2025.

Descripción:

"""
import pygame
from Media import Background
from Configurations import Configurations

def game_events(personaje,elegido) -> tuple[bool, bool]:
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                personaje.elegir('A')
                elegido = True
            elif event.key == pygame.K_b:
                personaje.elegir('B')
                elegido = True
            elif event.key == pygame.K_c:
                personaje.elegir('C')
                elegido = True

    return game_over, elegido

def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background,personaje,bambus) -> None:
    """
    Función que administra los elementos visuales del juego.
    """
    background.update()  #Actualiza la posición del fondo
    background.blit(screen)

    for bambu in bambus.sprites():
        bambu.update_position()
        bambu.blit(screen)

    #Actualiza y dibuja al personaje y hace la caida y animacion
    personaje.update_position()
    personaje.animation()
    personaje.blit(screen)

    pygame.display.flip()
    clock.tick(Configurations.get_fps())



