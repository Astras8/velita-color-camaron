### escena de la introduccion, previa al menu principal ###

import pygame as pg
from escenas.Escena import Escena
from animaciones.AnimacionFade import AnimacionFade as fade

class EscenaIntro(Escena):
    def __init__(self, anchoPantalla, altoPantalla, imagenLogo):
        super().__init__()

        ## atributos base ##
        # un logo
        self.logo = imagenLogo
        self.rectLogo = self.logo.get_rect(center = (anchoPantalla // 2, altoPantalla // 2))

        # transicion de la intro
        self.transicion = fade(anchoPantalla, altoPantalla, velocidadFade = 3)

        # se usan subestados para delimitar que fase de la animacion se esta reproduciendo actualmente
        self.subestado = "FADE_IN"
        self.transicion.iniciarFadeIn()

        # tiempos
        self.tiempoEspera = 2000
        self.tiempoInicio = 0

    def manejarEventos(self, eventos):
        for evento in eventos:
            if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                self.proximoEstado = "MENU" # saltarse la intro

    def actualizar(self, dt):
        self.transicion.actualizar()

        # los subestados de los que se hablaba:
        if self.subestado == "FADE_IN" and self.transicion.transicionCompleta:
            self.subestado = "MOSTRANDO_LOGO"
            self.tiempoInicio = pg.time.get_ticks()

        elif self.subestado == "MOSTRANDO_LOGO":
            if pg.time.get_ticks() - self.tiempoInicio >= self.tiempoEspera:
                self.subestado = "FADE_OUT"
                self.transicion.iniciarFadeOut()

        elif self.subestado == "FADE_OUT" and self.transicion.transicionCompleta:
            self.proximoEstado = "MENU"

    def dibujar(self, pantalla):
        pantalla.fill((0, 0, 0))
        pantalla.blit(self.logo, self.rectLogo)
        self.transicion.dibujar(pantalla)
    pass