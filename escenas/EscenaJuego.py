### escena en donde transcurre todo el juego, excluyendo los minijuegos ###

import pygame as pg, jugador.Jugador as lupi, interfaz.Camara as Camara, objetos.ObjetoMapa as ObjetoMapa
from escenas.Escena import Escena
from animaciones.AnimacionFade import AnimacionFade as fade

class EscenaJuego(Escena):
    def __init__(self, ancho, alto):
        super().__init__()

        ## atributos base ##
        # ancho y alto de la pantalla
        self.ancho = ancho
        self.alto = alto

        # crea una camara en base al alto y ancho de la pantalla
        self.camara = Camara.Camara(ancho, alto)

        ## mapa ##
        # se crea una matriz donde 0 indica vacio y 1 indica un objeto
        self.diseñoMapa = [[0 for _ in range(30)] for _ in range(17)]
        self.tamañoTile = 64

        # filas y columnas del mapa
        self.filas = len(self.diseñoMapa)
        self.columnas = len(self.diseñoMapa[0])

        # el ancho y el alto se obtienen por multiplicarse con el tamaño de las tiles
        # las tiles sirven para delimitar el tamaño de un "bloque" del mapa
        self.anchoMapa = self.columnas * self.tamañoTile
        self.altoMapa = self.filas * self.tamañoTile

        # el jugador, aparece en el centro del mapa
        self.lupi = lupi.Jugador(self.anchoMapa // 2, self.altoMapa // 2)

        # se inicializa el mapa como superficie
        self.mapaSuperficie = pg.Surface((self.anchoMapa, self.altoMapa)).convert()

        # se inicializa y escala la textura del pasto para usarse en el mapa
        texturaPasto = pg.image.load("assets/imagenes/texturaPasto.jpg").convert()
        texturaPasto = pg.transform.scale(texturaPasto, (self.tamañoTile, self.tamañoTile))
        self.mapaSuperficie.fill((40, 45, 40))

        ## objetos ##
        # se usa un arreglo para almacenar los tipos de objetos
        self.listaObjetos = []

        # atributos sobre la posicion y radio de interaccion de la vela
        self.posVela = (400, 120)
        self.fuenteInteraccion = pg.font.Font(None, 32)
        self.radioInteraccion = 80.0
        self.cercaniaVela = False

        ## fade ##
        self.transicion = fade(ancho, alto, velocidadFade = 4)
        self.transicion.iniciarFadeIn()

        # booleano para iniciar la transicion
        self.cambiandoEscena = False

        # matriz que crea el mapa en "bloques" cubiertos con la textura del pasto para todas las filas y columnas, si el valor es de la matriz es 1, se crea un objeto en esa posicion
        for filaIdx, fila in enumerate(self.diseñoMapa):
            for columnaIdx, valor in enumerate(fila):
                x = columnaIdx * self.tamañoTile
                y = filaIdx * self.tamañoTile

                self.mapaSuperficie.blit(texturaPasto, (x, y))

                if valor == 1:
                    self.listaObjetos.append(ObjetoMapa.ObjetoMapa(x, y, self.tamañoTile, self.tamañoTile, (30, 30, 35)))

        objetoPrueba = ObjetoMapa.ObjetoMapa(50, 50, 50, 50, (150, 150, 150))
        self.listaObjetos.append(objetoPrueba)

    def manejarEventos(self, eventos):
        if self.cambiandoEscena: # si esta cambiando de escena, no hace nada
            return
        
        for evento in eventos:
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_ESCAPE:
                    self.proximoEstado = "MENU" # si se presiona escape, vuelve al menu, simula un menu de pausa

                if evento.key == pg.K_e and self.cercaniaVela:
                    self.transicion.iniciarFadeOut()
                    self.cambiandoEscena = True # si se interactua con la vela, inicia una transicion al minijuego
    pass
    
    def actualizar(self, dt):
        self.transicion.actualizar()

        if self.cambiandoEscena and self.transicion.transicionCompleta:
            self.proximoEstado = "MINIJUEGO"
            return

        if not self.cambiandoEscena:
            self.lupi.actualizar(dt, self.anchoMapa, self.altoMapa)

            self.camara.actualizar(self.lupi, self.anchoMapa, self.altoMapa)

            distanciaX = self.lupi.rect.centerx - self.posVela[0] # la posicion 0 es la coordenada en x
            distanciaY = self.lupi.rect.centery - self.posVela[1] # la posicion 1 es la coordenada en y
            distancia = (distanciaX**2 + distanciaY**2)**0.5 # normalizacion, vivan los vectores

            self.cercaniaVela = distancia <= self.radioInteraccion

    def dibujar(self, pantalla):
        # simula el jardin
        pantalla.fill((0, 0, 0))

        pantalla.blit(self.mapaSuperficie, (-self.camara.x, -self.camara.y))

        for objeto in self.listaObjetos:
            objeto.dibujar(pantalla, self.camara)

        # dibuja a la vela
        velaPantallaX = self.posVela[0] - self.camara.x
        velaPantallaY = self.posVela[1] - self.camara.y
        pg.draw.circle(pantalla, (255, 200, 100), (int(velaPantallaX), int(velaPantallaY)), 15)

        # dibuja al personaje
        self.lupi.dibujar(pantalla, self.camara)

        # interaccion con la vela
        if self.cercaniaVela and not self.cambiandoEscena:
            textoSuperficie = self.fuenteInteraccion.render("Pulsa E para interactuar con la vela", True, (255, 255, 255))

            rectTexto = textoSuperficie.get_rect(center=(int(velaPantallaX), int(velaPantallaY) - 40))

            fondoTexto = pg.Surface((rectTexto.width + 10, rectTexto.height + 6), pg.SRCALPHA)
            fondoTexto.fill((0, 0, 0, 180))

            pantalla.blit(fondoTexto, (rectTexto.x - 5, rectTexto.y - 3))
            pantalla.blit(textoSuperficie, rectTexto)

        self.transicion.dibujar(pantalla)
    pass