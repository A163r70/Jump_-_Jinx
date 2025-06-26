from pygame.sprite import Sprite
from Configurations import Configurations
import pygame
import random

class Bambu(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        screen_rect = screen.get_rect()
        bambu_image_path = Configurations.get__image_bambu()
        bambu_width, bambu_height = Configurations.get_bambu_size()

        self.espacio = Configurations.get_espacio()
        altura_maxima = screen_rect.height - self.espacio - Configurations.get_altura_maxima()
        altura_hueco = random.randint(Configurations.get_altura_maxima(), altura_maxima)

        original_image = pygame.image.load(bambu_image_path)

        self.image_arriba = pygame.transform.scale(
            pygame.transform.flip(original_image, False, True),
            (bambu_width, altura_hueco)
        )
        self.rect_arriba = self.image_arriba.get_rect(bottom=altura_hueco, left=screen_rect.width)#

        altura_abajo = screen_rect.height - altura_hueco - self.espacio
        self.image_abajo = pygame.transform.scale(
            original_image,
            (bambu_width, altura_abajo)
        )
        self.rect_abajo = self.image_abajo.get_rect(top=altura_hueco + self.espacio, left=screen_rect.width)

        self._speed = Configurations.get_bambu_speed()
        self._rect_x = float(self.rect_abajo.x)

    def update_position(self):
        self._rect_x -= self._speed
        self.rect_arriba.x = int(self._rect_x)
        self.rect_abajo.x = int(self._rect_x)

    def blit(self, screen):
        screen.blit(self.image_arriba, self.rect_arriba)
        screen.blit(self.image_abajo, self.rect_abajo)
