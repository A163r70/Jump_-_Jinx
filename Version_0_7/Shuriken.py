import pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class Shuriken(Sprite):
    def __init__(self, enemy):
        super().__init__()

        self._frames = []

        sheet_shuriken_path = Configurations.get_sheet_path_shuriken()
        shuriken_path = pygame.image.load(sheet_shuriken_path)

        sheet_frames_per_row = Configurations.get_shuriken_frames_per_row()
        sheet_width = shuriken_path.get_width()
        sheet_height = shuriken_path.get_height()
        shuriken_frame_width = sheet_width // sheet_frames_per_row
        shuriken_frame_height = sheet_height

        shuriken_frame_size = Configurations.get_shuriken_size()

        for i in range(sheet_frames_per_row):#
            x = i * shuriken_frame_width
            y = 0
            subsurface_rect = (x, y, shuriken_frame_width, shuriken_frame_height)
            frame = shuriken_path.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, shuriken_frame_size)

            self._frames.append(frame)

        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0

        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        self.rect = self.image.get_rect()

        enemy_rect = enemy.rect
        self.rect.right = enemy_rect.right - 130
        self.rect.centery = enemy_rect.centery - 10

        self._speed = Configurations.get_shuriken_speed()
        self._rect_x = float(self.rect.x)

    def shuriken_animation(self)->None:
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_shuriken_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            if self._frame_index >= len(self._frames):
                self._frame_index = 0

    def update_position(self):
        self._rect_x -= self._speed

        self.rect.x = int(self._rect_x)

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)