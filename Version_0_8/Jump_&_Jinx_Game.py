import pygame
from Configurations import Configurations
from Game_Funcionalities import game_events, screen_refresh,check_collision
from Media import Background, Background_selection
from Personajes import Personaje
from Bambu import Bambu
from pygame.sprite import Group
import time
from Enemigo import Enemigo
from Shuriken import Shuriken


def run_game() -> None:
    """
    Función principal del videojuego
    """
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())

    personaje = Personaje(screen)

    #🤠🤠🤠agregué otro while para revisar el personaje que eligen según la tecla
    elegido = False
    game_over = False
    selection = Background_selection()

    # 🎯Inicializar el score y fuente
    score = 0
    font = pygame.font.SysFont("Segoe UI", 36, bold=True)
    original_score_image = pygame.image.load(Configurations.get_score_image())
    score_image = pygame.transform.scale(original_score_image, (Configurations.get_score_size()))

    while not elegido and not game_over:
        game_over,elegido = game_events(personaje,elegido)  #🤠🤠🤠muestro la imagen del personaje seleccionado
        pygame.display.flip()  #🤠🤠aquí atualizo la pantalla para mostrar los cambios
        selection.blit(screen)
        clock.tick(Configurations.get_frames_seleccion())  #🤠🤠🤠30 frames por segundo para la pantalla de selección

    background = Background()

    tiempo_ultimo_bambu = time.time()
    intervalo_bambu = Configurations.get_segundos_aparicion_bambu()  # segundos entre cada bambú
    bambus = Group()

    enemy = Enemigo(screen)
    enemy_group = Group()


    shuriken_group = Group()
    ultimo_tiempo_shuriken = time.time()
    intervalo_shurikens = Configurations.get_tiempo_aparicion()

    bandera = False

    while not game_over and elegido:
        tiempo_actual = time.time()
        if (tiempo_actual - ultimo_tiempo_shuriken) > intervalo_shurikens and bandera:
            new_shuriken = Shuriken(enemy)
            shuriken_group.add(new_shuriken)
            ultimo_tiempo_shuriken = tiempo_actual

        game_over, elegido = game_events(personaje, elegido)
        # Generar nuevo bambú si ha pasado suficiente tiempo


        # generamos un shuriken nuevo cada 2 segundos


        if tiempo_actual - tiempo_ultimo_bambu > intervalo_bambu:
            bambu = Bambu(screen)
            bambus.add(bambu)
            tiempo_ultimo_bambu = tiempo_actual

        game_over = check_collision(screen, personaje, bambus,shuriken_group)

        # 🎯Revisar para sumar al score
        for bambu in list(bambus):
            if not hasattr(bambu, "pasado"):  # Mi variable dinámica
                bambu.pasado = False

            if not bambu.pasado and bambu.rect_abajo.right < personaje.rect.left:
                score += 1
                bambu.pasado = True

        if score == 15:
            enemy_group.add(enemy)
            bandera = True


        # Eliminar bambús que ya salieron de la pantalla.
        for bambu in list(bambus):
            if bambu.rect_abajo.right < 0:
                bambus.remove(bambu)

        screen_refresh(screen, clock, background, personaje, bambus, enemy_group, shuriken_group, score, font, score_image)


    pygame.quit()


if __name__ == '__main__':
    run_game()