import pygame as pg

class Boton:
    def __init__(self, x, y, ancho, alto, texto, callback, tamañoTexto = 30, colorBase = (50, 50, 50), colorHover = (100, 100, 100), colorTexto = (255, 255, 255)):
        ## atributos base ##
        # rectangulo, colores y funciones del boton
        self.rect = pg.Rect(x, y, ancho, alto)
        self.callback = callback
        
        self.colorBase = colorBase
        self.colorHover = colorHover
        self.colorActual = colorBase

        self.fuente = pg.font.Font(None, tamañoTexto)
        self.texto = self.fuente.render(texto, True, colorTexto)
        self.textoRect = self.texto.get_rect(center = self.rect.center)

        self.presionado = False

    def actualizar(self, posicionMouse, click, eventos):
        if self.rect.collidepoint(posicionMouse): # si el mouse esta sobre el boton
            self.colorActual = self.colorHover

            # si se hizo click, ejecuta la funcion
            if click[0]:
                if not self.presionado:
                    self.callback()
                    self.presionado = True
            
            # si no, no
            else:
                self.presionado = False

        else:
            # vuelve a estar normal
            self.colorActual = self.colorBase
            self.presionado = False

    def dibujar(self, superficie):
        pg.draw.rect(superficie, self.colorActual, self.rect, border_radius = 8)
        superficie.blit(self.texto, self.textoRect)