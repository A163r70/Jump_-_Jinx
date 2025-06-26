import pygame
from Configurations import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla.
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

class Audio:
    """
    Clase que contiene el audio del videojuego, incluyendo la música y los efectos de sonido.
    Sus atributos son: la música y los sonidos.
    Sus métodos son: para reproducir y controlar la música, así como los que reproducen los sonidos.
    """

    def __init__(self):
        # Se carga la música del videojuego.
        pygame.mixer.music.load(Configurations.get_music_path())

        # Se carga el sonido de selección.
        self._selection_sound = pygame.mixer.Sound(Configurations.get_selection_sound())

        # Se carga el sonido de brinco.
        self._jump_sound = pygame.mixer.Sound(Configurations.get_jump_sound_path())

        # Se carga el sonido de la llegada del enemigo.
        self._enemy_sound = pygame.mixer.Sound(Configurations.get_enemy_sound_path())

        # Se carga el sonido cuando el jugador ha perdido.
        self._game_over_sound = pygame.mixer.Sound(Configurations.get_game_over_sound_path())

    @classmethod
    def play_music(cls, volume) -> None:
        """
        Se utiliza para reproducir la música en bucle.
        """
        pygame.mixer.music.play(loops=-1)  # Un -1 indica que la música se reproduce en bucle.
        pygame.mixer.music.set_volume(volume)

    def play_selection_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido de inicio del juego.
        """
        self._selection_sound.play()

    @classmethod
    def music_fadeout(cls, time) -> None:
        """
        Se utiliza para realizar un desvanecimiento de la música del juego hasta parar.
        :param time: Tiempo de desvanecimiento de la música (en ms).
        """
        pygame.mixer.music.fadeout(time)

    def play_jump_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando la serpiente come la manzana.
        """
        self._jump_sound.play()

    def play_enemy_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando la serpiente come la manzana.
        """
        self._enemy_sound.play()

    def play_game_over_sound(self) -> None:
        """
        Se utiliza para reproducir el sonido cuando el jugador ha perdido.
        """
        self._game_over_sound.play()

class GameOverImage:
    def __init__(self):
        self.image = pygame.image.load("../media/game_over_image.png")
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.image, self.rect)