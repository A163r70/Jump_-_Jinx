import pygame
from Configurations import Configurations

class Personaje:
    def __init__(self):
        self.seleccionado = None

        sprites = Configurations.get_sprites_por_personaje()
        tamano = Configurations.get_personaje_size()

        self.imagenes = {
            'A': pygame.transform.scale(pygame.image.load(sprites['A']['reposo'][0]), tamano),
            'B': pygame.transform.scale(pygame.image.load(sprites['B']['reposo'][0]), tamano),
            'C': pygame.transform.scale(pygame.image.load(sprites['C']['reposo'][0]), tamano)
        }

        #🤠🤠🤠cargé y escalé la imagen de fondo para elegir personaje con el tamaño de toda la pantalla
        self.imagen_elegir = pygame.transform.scale(
            pygame.image.load(Configurations.get_choice_pesonaje()),
            Configurations.get_screen_size()
        )

    def elegir(self, tecla: str): #🤠🤠guardé la imagen seleccionada según la tecla presionada
        if tecla in self.imagenes:
            self.seleccionado = self.imagenes[tecla]

    def mostrar(self, screen: pygame.Surface):#🤠🤠🤠con esto se dibuj la imagen seleccionada en pantalla o la imagen de selección si no se ha elegido
        if self.seleccionado:
            screen.blit(self.seleccionado, (20, 20))  #🤠dibuja el personaje seleccionado en la esquina superior izq
        else:
            screen.blit(self.imagen_elegir, (0, 0))  #🤠🤠dib la imagen de fondo para elegir personaje cubriendo toda la pantalla
