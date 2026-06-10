import pygame as pg

class ObjetoMapa:
    def __init__(self, x, y, ancho, alto, color):
        self.image = pg.Surface((ancho, alto))
        self.image.fill(color)

        self.rect = self.image.get_rect(topleft = (x, y))

    def dibujar(self, pantalla, camara):
        posPantallaX = self.rect.x - camara.x
        posPantallaY = self.rect.y - camara.y
        
        pantalla.blit(self.image, (posPantallaX, posPantallaY))