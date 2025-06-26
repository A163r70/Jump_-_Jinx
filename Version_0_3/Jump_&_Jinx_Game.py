import pygame
from Configurations import Configurations
from Game_Funcionalities import game_events, screen_refresh
from Media import Background
from Personajes import Personaje


def run_game() -> None:
    """
    Función principal del videojuego
    """
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())

    personaje = Personaje()

    #🤠🤠🤠agregué otro while para revisar el personaje que eligen según la tecla
    elegido = False
    game_over = False

    while not elegido and not game_over:
        game_over,elegido = game_events(personaje,elegido)  #🤠🤠🤠muestro la imagen del personaje seleccionado
        pygame.display.flip()  #🤠🤠aquí atualizo la pantalla para mostrar los cambios
        personaje.blit(screen)
        clock.tick(30)  #🤠🤠🤠30 frames por segundo para la pantalla de selección

    background = Background()

    while not game_over and elegido:
        game_over,elegido = game_events(personaje,elegido)
        screen_refresh(screen, clock, background,personaje)

    pygame.quit()


if __name__ == '__main__':
    run_game()
