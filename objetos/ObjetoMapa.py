## clase para los objetos presentes en el mapa ##

import pygame as pg

class ObjetoMapa:
    def __init__(self, x, y, ancho, alto, color):
        ## atributos base ##
        # imagen asociada al objeto
        self.imagen = pg.Surface((ancho, alto))
        self.imagen.fill(color)
        
        # rectangulo del objeto, funcion especifica de pygame
        self.rect = self.imagen.get_rect(topleft = (x, y))

    def dibujar(self, pantalla, camara):
        posPantallaX = self.rect.x - camara.x
        posPantallaY = self.rect.y - camara.y
        
        pantalla.blit(self.imagen, (posPantallaX, posPantallaY))