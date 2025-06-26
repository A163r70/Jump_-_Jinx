"""
Nombre: Equipo los Bugs
Fecha: 10 de junio del 2025.

Descripción:

"""
import pygame
from Media import Background
from Configurations import Configurations
from Personajes import Personaje

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

            if event.key == pygame.K_SPACE:
                personaje._is_moving_up = True
            if event.key == pygame.K_SPACE:
                personaje._is_moving_down = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                personaje.is_moving_up = False
            if event.key == pygame.K_SPACE:
                personaje.is_moving_down = True

    return game_over, elegido

def check_collision(screen: pygame.surface.Surface, personaje: Personaje, bambus, shurikens):
    game_over = False


    screen_rect = screen.get_rect()

    if personaje.rect.top < screen_rect.top:
        game_over = True
    elif personaje.rect.top > screen_rect.bottom:
        game_over = True

    for bambu in bambus:
        if personaje.rect.colliderect(bambu.rect_arriba) or personaje.rect.colliderect(bambu.rect_abajo):
            return True

    for shuriken in shurikens:
        if personaje.rect.colliderect(shuriken.rect):
            return True

    return game_over

def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background,personaje,bambus,group_enemy: pygame.sprite.Group,
                   shuriken_group: pygame.sprite.Group) -> None:
    """
    Función que administra los elementos visuales del juego
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

    for enemy in group_enemy.sprites():
        enemy.blit(screen)
        enemy.animation()
        enemy.update_position(screen)

    for shuriken in shuriken_group.sprites():
        shuriken.shuriken_animation()
        shuriken.update_position()
        shuriken.blit(screen)



    pygame.display.flip()
    clock.tick(Configurations.get_fps())








