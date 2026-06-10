import pygame as pg
from estados.EstadoJuego import EstadoJuego
import Jugador as lupi
import Camara
import ObjetoMapa

class EscenaJuego(EstadoJuego):
    def __init__(self, ancho, alto):
        super().__init__()

        self.camara = Camara.Camara(ancho, alto)
        self.ancho = ancho
        self.alto = alto

        self.lupi = lupi.Jugador(1000, 1000)

        # mapa
        self.anchoMapa = 3000
        self.altoMapa = 3000
        self.mapaSuperficie = pg.Surface((self.anchoMapa, self.altoMapa)).convert()
        self.mapaSuperficie.fill((40, 45, 40))

        for x in range(0, self.anchoMapa, 100):
            pg.draw.line(self.mapaSuperficie, (60, 65, 60), (x, 0), (x, self.altoMapa), 2)
            
        for y in range(0, self.altoMapa, 100):
            pg.draw.line(self.mapaSuperficie, (60, 65, 60), (0, y), (self.anchoMapa, y), 2)

        # objetos

        self.listaObjetos = []

        objetoPrueba = ObjetoMapa.ObjetoMapa(50, 50, 50, 50, (150, 150, 150))
        self.listaObjetos.append(objetoPrueba)

    def manejarEventos(self, eventos):
        for evento in eventos:
            if evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE:
                self.proximoEstado = "MENU"
    pass
    
    def actualizar(self, dt):
        self.lupi.actualizar(dt, self.anchoMapa, self.altoMapa)

        self.camara.actualizar(self.lupi, self.anchoMapa, self.altoMapa)

    def dibujar(self, pantalla):
        # simula el jardin
        pantalla.fill((0, 0, 0))

        pantalla.blit(self.mapaSuperficie, (-self.camara.x, -self.camara.y))

        for objeto in self.listaObjetos:
            objeto.dibujar(pantalla, self.camara)

        self.lupi.dibujar(pantalla, self.camara)
    pass