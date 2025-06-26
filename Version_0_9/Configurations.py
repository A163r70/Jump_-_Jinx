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
    _personaje_size = (70, 100 ) #🤠🤠🤠agrugé un tamaño al personaje
    _game_title = "Jump & Jinx"
    _image_background = "../Media/fondo_oficial.png"
    _fps = 8
    _choice_pesonaje = "../Media/Elegir_personaje.png" #🤠🤠🤠cargué la imagen de selección.

    _sprites_por_personaje = { #🤠🤠diccionario de sprites
        'A': {  #Diochan
            'reposo': [
                "../Media/D_S_1.png",
                "../Media/D_S_2.png",
                "../Media/D_S_3.png",
                "../Media/D_S_4.png"
            ]
        },
        'B': {  #Kagura
            'reposo': [
                "../Media/K_S_1.png",
                "../Media/K_S_2.png",
                "../Media/K_S_3.png",
                "../Media/K_S_4.png"
            ]
        },
        'C': {  #Alberto
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
    _espacio = 270
    _altura_maxima = 100

    #pantallaseleccion
    _frames_seleccion = 30
    _segundos_aparicion_bambu = 2
    _posicion_eleccion = (0,0)

    #personaje
    _milisegundos_aparicion = 150
    _posicion_inicial = (0, 250)
    _sped_personaje = 20.5

    # enemigo
    _sheet_path_enemy = ["../Media/pixil-layer-Background.png",
                         "../Media/pixil-layer-Background (1).png",
                         "../Media/pixil-layer-Background (2).png",
                         "../Media/pixil-layer-Background (3).png",
                         "../Media/pixil-layer-Background (4).png",
                         "../Media/pixil-layer-Background (5).png"]

    _enemy_size = (200, 300)
    _speed_enemy = 10
    _time_to_refresh = 70
    _speed_move_enemy = 19.5

    # shuriken
    _sheet_path_shuriken = "../Media/shuriken.png"
    _shuriken_frames_per_row = 4
    _shuriken_size = (40, 40)
    _shuriken_speed = 20.5
    _shuriken_frame_delay = 100
    _tiempo_aparicion = 3


    _score_image = "../Media/score_image.png"
    _score_size = (120, 90)

    _game_over_screen_time = 4
    # Configuraciones de la música del juego.
    _music_volume = 0.25  # Volumen de la música de fondo (valor entre 0 y 1).
    _music_fadeout_time = _game_over_screen_time * 1000  # Duración del desvanecimiento de la música (en ms).


    # Rutas de los audios utilizados en la clase Audio.
    _music_path = "../Media/jugando_song.mp3"
    _selection_sound = "../Media/inicio_song.mp3"
    _jump_sound_path = "../Media/jump.mp3"
    _enemy_sound_path = "../Media/sonido_villano.mp3"
    _game_over_sound_path = "../Media/game_over.mp3"

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

    @classmethod
    def get_sheet_path_enemy(cls) -> list:
        return cls._sheet_path_enemy

    @classmethod
    def get_enemy_size(cls) -> tuple[int, int]:
        return cls._enemy_size

    @classmethod
    def get_speed_enemy(cls) -> int:
        return cls._speed_enemy

    @classmethod
    def get_time_to_refresh(cls) -> int:
        return cls._time_to_refresh

    @classmethod
    def get_speed_move_enemy(cls) -> float:
        return cls._speed_move_enemy

    @classmethod
    def get_sheet_path_shuriken(cls) -> str:
        return cls._sheet_path_shuriken

    @classmethod
    def get_shuriken_frames_per_row(cls) -> int:
        return cls._shuriken_frames_per_row

    @classmethod
    def get_shuriken_size(cls) -> tuple[int, int]:
        return cls._shuriken_size

    @classmethod
    def get_shuriken_speed(cls) -> float:
        return cls._shuriken_speed

    @classmethod
    def get_shuriken_frame_delay(cls)->int:
        return cls._shuriken_frame_delay

    @classmethod
    def get_tiempo_aparicion(cls)->int:
        return cls._tiempo_aparicion

    @classmethod
    def get_score_image(cls) -> str:
        return cls._score_image

    @classmethod
    def get_score_size(cls) -> tuple[int, int]:
        return cls._score_size

    @classmethod
    def get_music_volume(cls) -> float:
        """
        Getter para _music_volume.
        """
        return cls._music_volume

    @classmethod
    def get_music_fadeout_time(cls) -> int:
        """
        Getter para _music_fadeout_time.
        """
        return cls._music_fadeout_time

    @classmethod
    def get_music_path(cls) -> str:
        """
        Getter para _music_path.
        """
        return cls._music_path

    @classmethod
    def get_selection_sound(cls) -> str:
        """
        Getter para _start_sound_path.
        """
        return cls._selection_sound

    @classmethod
    def get_jump_sound_path(cls) -> str:
        """
        Getter para _eats_apple_sound_path.
        """
        return cls._jump_sound_path

    @classmethod
    def get_enemy_sound_path(cls) -> str:
        """
        Getter para _eats_apple_sound_path.
        """
        return cls._enemy_sound_path

    @classmethod
    def get_game_over_sound_path(cls) -> str:
        """
        Getter para _game_over_sound_path.
        """
        return cls._game_over_sound_path

    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para _apple_color
        """
        return cls._game_over_screen_time

    @classmethod
    def get_espacio(cls) -> int:
        """
        Getter para espacio
        """
        return cls._espacio

    @classmethod
    def get_altura_maxima(cls) -> int:
        """
        Getter para _altura_maxima del bambu
        """
        return cls._altura_maxima