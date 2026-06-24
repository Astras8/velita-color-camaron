import pygame as pg
from estados.EstadoJuego import EstadoJuego
from animaciones.AnimacionFade import AnimacionFade as fade
import Jugador as lupi
import Camara
import ObjetoMapa
import Colision

class EscenaJuego(EstadoJuego):
    def __init__(self, ancho, alto):
        super().__init__()

        self.camara = Camara.Camara(ancho, alto)

        self.ancho = ancho
        self.alto = alto

        # mapa
        self.diseñoMapa = [[0 for _ in range(30)] for _ in range(17)]

        self.tamañoTile = 64

        self.filas = len(self.diseñoMapa)
        self.columnas = len(self.diseñoMapa[0])

        self.anchoMapa = self.columnas * self.tamañoTile
        self.altoMapa = self.filas * self.tamañoTile

        self.lupi = lupi.Jugador(self.anchoMapa // 2, self.altoMapa // 2)
        
        self.colision = Colision.Colision()

        self.mapaSuperficie = pg.Surface((self.anchoMapa, self.altoMapa)).convert()

        texturaPasto = pg.image.load("assets/imagenes/texturaPasto.jpg").convert()
        texturaPasto = pg.transform.scale(texturaPasto, (self.tamañoTile, self.tamañoTile))
        self.mapaSuperficie.fill((40, 45, 40))

        # objetos
        self.listaObjetos = []

        self.posVela = (400, 120)
        self.radioInteraccion = 80.0
        self.cercaniaVela = False

        # fade
        self.transicion = fade(ancho, alto, velocidadFade = 4)
        self.transicion.iniciarFadeIn()

        self.cambiandoEscena = False

        for filaIdx, fila in enumerate(self.diseñoMapa):
            for columnaIdx, valor in enumerate(fila):
                x = columnaIdx * self.tamañoTile
                y = filaIdx * self.tamañoTile

                self.mapaSuperficie.blit(texturaPasto, (x, y))

                if valor == 1:
                    self.listaObjetos.append(ObjetoMapa.ObjetoMapa(x, y, self.tamañoTile, self.tamañoTile, (30, 30, 35)))

        objetoPrueba = ObjetoMapa.ObjetoMapa(100,100, 50, 50, (150, 150, 150))
        self.listaObjetos.append(objetoPrueba)

    def manejarEventos(self, eventos):
        if self.cambiandoEscena:
            return
        
        for evento in eventos:
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_ESCAPE:
                    self.proximoEstado = "MENU"

                if evento.key == pg.K_e and self.cercaniaVela:
                    self.transicion.iniciarFadeOut()
                    self.cambiandoEscena = True
    pass
    
    def actualizar(self, dt):
        self.transicion.actualizar()

        if self.cambiandoEscena and self.transicion.transicionCompleta:
            self.proximoEstado = "MINIJUEGO"
            return

        if not self.cambiandoEscena:
            self.lupi.actualizar(dt, self.anchoMapa, self.altoMapa)
            self.colision.resolver(self.lupi, self.listaObjetos)

            self.camara.actualizar(self.lupi, self.anchoMapa, self.altoMapa)

            distanciaX = self.lupi.rect.centerx - self.posVela[0]
            distanciaY = self.lupi.rect.centery - self.posVela[1]
            distancia = (distanciaX**2 + distanciaY**2)**0.5

            self.cercaniaVela = distancia <= self.radioInteraccion

    def dibujar(self, pantalla):
        # simula el jardin
        pantalla.fill((0, 0, 0))

        pantalla.blit(self.mapaSuperficie, (-self.camara.x, -self.camara.y))

        for objeto in self.listaObjetos:
            objeto.dibujar(pantalla, self.camara)

        velaPantallaX = self.posVela[0] - self.camara.x
        velaPantallaY = self.posVela[1] - self.camara.y
        pg.draw.circle(pantalla, (255, 200, 100), (int(velaPantallaX), int(velaPantallaY)), 15)

        self.lupi.dibujar(pantalla, self.camara)

        self.transicion.dibujar(pantalla)

    pass