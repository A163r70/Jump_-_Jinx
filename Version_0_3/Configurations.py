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
    _image_background = "../Media/fondo_oficial.png"
    _fps = 8
    _choice_pesonaje = "../Media/Elegir_personaje.png" #🤠🤠🤠cargué la imagen de selección

    _sprites_por_personaje = { #🤠🤠diccionario de sprites
        'A': {  #Diochan
            'reposo': [
                "../Media/D_Reposo1.png",
                "../Media/D_Reposo2.png",
                "../Media/D_Reposo3.png",
                "../Media/D_Reposo4.png"
            ]
        },
        'B': {  #Kagura
            'reposo': [
                "../Media/K_Reposo1.png",
                "../Media/K_Reposo2.png",
                "../Media/K_Reposo3.png",
                "../Media/K_Reposo4.png"
            ]
        },
        'C': {  #Alberto
            'reposo': [
                "../Media/A_Reposo1.png",
                "../Media/A_Reposo2.png",
                "../Media/A_Reposo3.png",
                "../Media/A_Reposo4.png"
            ]
        }
    }

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
    def get_sprites_por_personaje(cls) -> dict:
        return cls._sprites_por_personaje
