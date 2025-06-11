import pygame
from Configurations import Configurations

class Personaje:
    def __init__(self):
        self.seleccionado = None

        ruta_diochan = Configurations.get_diochan_reposo_image_path()
        ruta_kagura = Configurations.get_diochan_reposo_image_path()
        ruta_alberto = Configurations.get_diochan_reposo_image_path()
        self.imagenes = { #🤠escalo la imagen cuando la cargo
            'A': pygame.transform.scale(pygame.image.load(ruta_diochan[0]), Configurations.get_personaje_size()),
            'B': pygame.transform.scale(pygame.image.load(ruta_kagura[0]), Configurations.get_personaje_size()),
            'C': pygame.transform.scale(pygame.image.load(ruta_alberto[0]), Configurations.get_personaje_size())
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
