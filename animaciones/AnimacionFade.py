import pygame as pg

class AnimacionFade:
    def __init__(self, pantallaAncho, pantallaAlto, velocidadFade = 3):
        self.capaNegra = pg.Surface((pantallaAncho, pantallaAlto)).convert_alpha()
        self.capaNegra.fill((0, 0, 0))

        self.alfaActual = 0
        self.modo = None # tiene dos modos, el "Fade In" y el "Fade Out"

        self.velocidad = velocidadFade
        self.transicionCompleta = False

    def iniciarFadeIn(self):
        self.modo = "fadeIn"
        self.alfaActual = 255
        self.transicionCompleta = False
        self.capaNegra.set_alpha(self.alfaActual)

    def iniciarFadeOut(self):
        self.modo = "fadeOut"
        self.alfaActual = 0
        self.transicionCompleta = False
        self.capaNegra.set_alpha(self.alfaActual)

    def actualizar(self):
        if self.transicionCompleta or self.modo is None:
            return

        if self.modo == "fadeIn":
            self.alfaActual -= self.velocidad
            if self.alfaActual <= 0:
                self.alfaActual = 0
                self.transicionCompleta = True

        elif self.modo == "fadeOut":
            self.alfaActual += self.velocidad
            if self.alfaActual >= 255:
                self.alfaActual = 255
                self.transicionCompleta = True

        self.capaNegra.set_alpha(self.alfaActual)
    
    def dibujar(self, pantalla):
        if self.alfaActual > 0:
            pantalla.blit(self.capaNegra, (0, 0))