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
    _personaje_size = (125, 150) #🤠🤠🤠agrugé un tamaño al personaje
    _game_title = "Jump & Jinx"
    _image_background = "../Media/fondo_oficial.png"
    _fps = 8
    _choice_pesonaje = "../Media/Elegir_personaje.png" #🤠🤠🤠cargué la imagen de selección

    _sprites_por_personaje = {  # 🤠🤠diccionario de sprites
        'A': {  # Diochan
            'reposo': [
                "../Media/D_S_1.png",
                "../Media/D_S_2.png",
                "../Media/D_S_3.png",
                "../Media/D_S_4.png"
            ]
        },
        'B': {  # Kagura
            'reposo': [
                "../Media/K_S_1.png",
                "../Media/K_S_2.png",
                "../Media/K_S_3.png",
                "../Media/K_S_4.png"
            ]
        },
        'C': {  # Alberto
            'reposo': [
                "../Media/A_S_1.png",
                "../Media/A_S_2.png",
                "../Media/A_S_3.png",
                "../Media/A_S_4.png",
                "../Media/A_S_5.png"
            ]
        }
    }

    #Pantalla
    _velocidad_inicial = 2
    _aceleracion = 0.002

    _image_bambu = "../Media/bambu.png"
    _bambu_size = (100, 144)
    _bambu_speed= 20

    #pantallaseleccion
    _frames_seleccion = 30
    _segundos_aparicion_bambu = 2
    _posicion_eleccion = (0,0)

    #personaje
    _milisegundos_aparicion = 150
    _posicion_inicial = (0, 250)
    _sped_personaje = 20.5

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

    @classmethod
    def get__image_bambu(cls) -> str:
        return cls._image_bambu

    @classmethod
    def get_bambu_size(cls) -> tuple[int, int]:
        return cls._bambu_size

    @classmethod
    def get_bambu_speed(cls) -> float:
        return cls._bambu_speed

    @classmethod
    def get_frames_seleccion(cls)->int:
        return cls._frames_seleccion

    @classmethod
    def get_segundos_aparicion_bambu(cls)->int:
        return cls._segundos_aparicion_bambu

    @classmethod
    def get_milisegundos_aparicion(cls)->int:
        return cls._milisegundos_aparicion

    @classmethod
    def get_posicion_inicial(cls)->tuple[int,int]:
        return cls._posicion_inicial

    @classmethod
    def get_posicion_eleccion(cls)->tuple[int,int]:
        return cls._posicion_eleccion

    @classmethod
    def get_sped_personaje(cls)->float:
        return cls._sped_personaje