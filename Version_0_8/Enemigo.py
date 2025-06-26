import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class Enemigo(Sprite):
    def __init__(self, screen):
        super().__init__()
        screen_rect = screen.get_rect()
        self._enemy_frames = []

        for i in range(len(Configurations.get_sheet_path_enemy())):
            self.image = pygame.image.load(Configurations.get_sheet_path_enemy()[i])
            self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale(self.image, Configurations.get_enemy_size())
            self._enemy_frames.append(self.image)
        self._last_update_time = pygame.time.get_ticks()

        self._frame_index = 0
        self.image = self._enemy_frames[self._frame_index]

        self.rect = self.image.get_rect()

        self.rect.centery = screen_rect.centery
        self.rect.right = screen_rect.right
        self.rect_y = float(self.rect.y)

        self._moving_down = True

    def animation(self)->None:
        current_time = pygame.time.get_ticks()
        time_to_refresh = Configurations.get_time_to_refresh()
        need_refres = (current_time - self._last_update_time) >= time_to_refresh

        if need_refres:
            self.image = self._enemy_frames[self._frame_index]

            self._last_update_time = current_time
            self._frame_index += 1

            if self._frame_index >= len(self._enemy_frames):
                self._frame_index = 0

    def update_position(self, screen)->None:
        screen_rect = screen.get_rect()
        speed = Configurations.get_speed_move_enemy()
        if self._moving_down:
            self.rect_y += speed
            if self.rect.bottom >= screen_rect.bottom:
                self._moving_down = False
        else:
            self.rect_y -= speed
            if self.rect.top <= screen_rect.top:
                self._moving_down = True

        self.rect.y = int(self.rect_y)


    def blit(self, screen: pygame.surface.Surface)->None:
        screen.blit(self.image, self.rect)