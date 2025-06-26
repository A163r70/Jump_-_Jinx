from pygame.sprite import Sprite
from Configurations import Configurations
import pygame
import random

class Bambu(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        #Tamaño de pantalla y bambú
        screen_rect = screen.get_rect()
        bambu_image_path = Configurations.get__image_bambu()
        bambu_width, bambu_height = Configurations.get_bambu_size()

        # Parámetros del hueco entre bambús
        self.espacio = 150  # Austar el hueco entre los bambus
        altura_maxima = screen_rect.height - self.espacio - 100
        altura_hueco = random.randint(100, altura_maxima)

        # Imagen y escalado para ambos bambús
        original_image = pygame.image.load(bambu_image_path)

        # Bambú de arriba (invertido verticalmente)
        self.image_arriba = pygame.transform.scale(pygame.transform.flip(original_image, False, True), (bambu_width, altura_hueco))
        self.rect_arriba = self.image_arriba.get_rect()
        self.rect_arriba.bottom = altura_hueco
        self.rect_arriba.left = screen_rect.width

        # Bambú de abajo
        altura_abajo = screen_rect.height - altura_hueco - self.espacio
        self.image_abajo = pygame.transform.scale(original_image, (bambu_width, altura_abajo))
        self.rect_abajo = self.image_abajo.get_rect()
        self.rect_abajo.top = altura_hueco + self.espacio
        self.rect_abajo.left = screen_rect.width

        self._speed = Configurations.get_bambu_speed()
        self._rect_x = float(self.rect_abajo.x)

    def update_position(self):
        # Movimiento horizontal
        self._rect_x -= self._speed
        self.rect_arriba.x = int(self._rect_x)
        self.rect_abajo.x = int(self._rect_x)

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image_arriba, self.rect_arriba)
        screen.blit(self.image_abajo, self.rect_abajo)
