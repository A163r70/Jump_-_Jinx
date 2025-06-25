import pygame
from pygame.sprite import Sprite
from Configurations import Configurations


class Personaje(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.seleccionado = None
        self.sprite_index = 0
        sprites = Configurations.get_sprites_por_personaje()
        size = Configurations.get_personaje_size()
        self.velocidad_caida = Configurations.get_sped_personaje()

        self.imagenes = {
            'A': [pygame.transform.scale(pygame.image.load(img), size) for img in sprites['A']['reposo']],
            'B': [pygame.transform.scale(pygame.image.load(img), size) for img in sprites['B']['reposo']],
            'C': [pygame.transform.scale(pygame.image.load(img), size) for img in sprites['C']['reposo']]
        }

        self.image = pygame.transform.scale(
            pygame.image.load(Configurations.get_choice_pesonaje()),
            Configurations.get_screen_size()
        )
        self.last_update = pygame.time.get_ticks()
        self.velocidad_animacion = Configurations.get_milisegundos_aparicion()  # Milisegundos entre frames

        self.rect = self.image.get_rect()
        screen_rect = screen.get_rect()
        self.rect.x = Configurations.get_posicion_inicial()[0]
        self.rect.y = Configurations.get_posicion_inicial()[1]
        self.rect.centery = screen_rect.centery
        self.rect.right = screen_rect.right

        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.centery = screen_rect.centery

    def elegir(self, tecla: str):
        if tecla in self.imagenes and not self.seleccionado:
            self.seleccionado = self.imagenes[tecla]
            self.sprite_index = 0
            self.last_update = pygame.time.get_ticks()


    def animation(self):

        if self.seleccionado:
            time = pygame.time.get_ticks()
            if time - self.last_update > self.velocidad_animacion:
                self.sprite_index = (self.sprite_index + 1) % len(self.seleccionado)
                self.last_update = time

    def update_position(self):
        self.rect.y += self.velocidad_caida
        self.rect.x += self.velocidad_caida



    def blit(self, screen: pygame.Surface):
        if self.seleccionado:
            screen.blit(self.seleccionado[self.sprite_index], self.rect)
