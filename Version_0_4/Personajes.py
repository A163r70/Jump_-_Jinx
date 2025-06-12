import pygame
from Configurations import Configurations

class Personaje:
    def __init__(self):
        self.seleccionado = None  # Lista de imágenes animadas del personaje
        self.sprite_index = 0
        self.last_update = pygame.time.get_ticks()
        self.velocidad_animacion = Configurations.get_milisegundos_aparicion()  # Milisegundos entre frames

        sprites = Configurations.get_sprites_por_personaje()
        size = Configurations.get_personaje_size()

        self.imagenes = {
            'A': [pygame.transform.scale(pygame.image.load(img), size) for img in sprites['A']['reposo']],
            'B': [pygame.transform.scale(pygame.image.load(img), size) for img in sprites['B']['reposo']],
            'C': [pygame.transform.scale(pygame.image.load(img), size) for img in sprites['C']['reposo']]
        }

        self.imagen_elegir = pygame.transform.scale(
            pygame.image.load(Configurations.get_choice_pesonaje()),
            Configurations.get_screen_size()
        )

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

    def blit(self, screen: pygame.Surface):
        if self.seleccionado:
            screen.blit(self.seleccionado[self.sprite_index], (Configurations.get_posicion_inicial()))
        else:
            screen.blit(self.imagen_elegir, (Configurations.get_posicion_eleccion()))
