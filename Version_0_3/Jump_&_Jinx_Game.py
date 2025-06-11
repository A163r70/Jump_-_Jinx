import pygame
from Configurations import Configurations
from Game_Funcionalities import game_events, screen_refresh
from Media import Background
from Personajes import Personaje


def run_game() -> None:
    """
    Función principal del videojuego.
    """
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())

    personaje = Personaje()

    #🤠🤠🤠agregué otro while para revisar el personaje que eligen según la tecla
    elegido = False
    while not elegido:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

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

        #screen.fill((0, 0, 0))
        personaje.mostrar(screen)  #🤠🤠🤠muestro la imagen del personaje seleccionado
        pygame.display.flip()  #🤠🤠aquí atualizo la pantalla para mostrar los cambios
        clock.tick(30)  #🤠🤠🤠30 frames por segundo para la pantalla de selección

    background = Background()
    game_over = False
    while not game_over:
        game_over = game_events()

        screen_refresh(screen, clock, background)
        personaje.mostrar(screen)#🤠🤠🤠con esto dibujo el personaje elegido en pantalla
        pygame.display.flip()#🤠🤠🤠actualizo la pantalla
        clock.tick(Configurations.get_fps())#fps

    pygame.quit()


if __name__ == '__main__':
    run_game()
