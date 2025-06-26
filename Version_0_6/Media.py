import pygame
from Configurations import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla
    """

    def __init__(self):
        background_image_path = Configurations.get_image_background()
        self.image = pygame.image.load(background_image_path)
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.width = screen_size[0]
        self.height = screen_size[1]

        self.x1 = 0
        self.x2 = self.width
        self.y = 0

        self.speed = Configurations.get_velocidad_inicial()
        self.increment = Configurations.get_aceleracion()

    def update(self):

        self.speed += self.increment

        self.x1 -= self.speed
        self.x2 -= self.speed

        if self.x1 <= -self.width:
            self.x1 = self.x2 + self.width
        if self.x2 <= -self.width:
            self.x2 = self.x1 + self.width

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, (self.x1, self.y))
        screen.blit(self.image, (self.x2, self.y))

class Background_selection:
    def __init__(self):
        background_image_path = Configurations.get_choice_pesonaje()
        self.image = pygame.image.load(background_image_path)
        # Escalamos la imagen para que coincida con el tamaño de la pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)