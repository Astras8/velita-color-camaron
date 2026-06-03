import pygame as pg
from estados.EstadoJuego import EstadoJuego

class EscenaJuego(EstadoJuego):
    def __init__(self, ancho, alto):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        self.lupi = None
    
    #def actualizar(self, dt):

    def dibujar(self, pantalla):
        # simula el jardin
        pantalla.fill((6, 64, 43))
    pass