"""
Nombre: Equipo los Bugs
Fecha:
"""

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    #Definimos el tamaño de la pantalla, título y color de fondo RGB.
    _screen_size = (1280, 720)
    _game_title = "Jump & Jinx"
    _image_background = "../Media/image_b.jpg"
    _fps = 8

    #Pantalla
    _velocidad_inicial = 2
    _aceleracion = 0.002

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para get_game_title.
        """
        return cls._game_title

    @classmethod
    def get_image_background(cls)->str:
        return cls._image_background

    @classmethod
    def get_fps(cls)->int:
        return cls._fps

    @classmethod
    def get_velocidad_inicial(cls) -> int:
        return cls._velocidad_inicial

    @classmethod
    def get_aceleracion(cls) -> float:
        return cls._aceleracion