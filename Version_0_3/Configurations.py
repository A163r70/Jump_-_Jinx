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
    _personaje_size = (300, 300) #🤠🤠🤠agrugé un tamaño al personaje
    _game_title = "Jump & Jinx"
    _image_background = "../Media/image_b.jpg"
    _fps = 8
    _choice_pesonaje = "../Media/Elige a tu personaje.png" #🤠🤠🤠cargué la imagen de selección
    _diochan_reposo_image_path = ["../Media/Reposo 1.png", ##🤠🤠🤠 cargué mis sprites de reposo
                              "../Media/Reposo 2.png",
                              "../Media/Reposo 3.png",
                              "../Media/Reposo 4.png"]

    #Pantalla
    _velocidad_inicial = 2
    _aceleracion = 0.002

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para screen_size.
        """
        return cls._screen_size

    #🤠🤠🤠
    @classmethod
    def get_personaje_size(cls) -> tuple[int, int]:
        """
        Getter para screen_size.
        """
        return cls._personaje_size

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

    #🤠🤠🤠
    @classmethod
    def get_choice_pesonaje(cls) -> str:
        return cls._choice_pesonaje

    #🤠🤠🤠
    @classmethod
    def get_diochan_reposo_image_path(cls) -> list:
        return cls._diochan_reposo_image_path
