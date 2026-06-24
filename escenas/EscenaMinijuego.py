### escena que transcurre durante todo el minijuego tras interactuar con una vela ###

import pygame as pg, random
from escenas.Escena import Escena
from enemigos.Enemigo import Enemigo

class EscenaMinijuego(Escena):
    def __init__(self, ancho, alto):
        super().__init__()

        ## atributos base ##
        # ancho y alto de la pantalla
        self.ancho = ancho
        self.alto = alto

        # coordenadas del centro de la pantalla
        self.cx = ancho // 2
        self.cy = alto // 2

        # atributos de la vela
        self.vidaVela = 100.0
        self.rectVela = pg.Rect(self.cx - 20, self.cy - 20, 40, 40)

        # por defecto lupi mira hacia arriba
        self.direccionLupi = "ARRIBA"
        self.rectLupi = pg.Rect(0, 0, 45, 45)
        
        # atributos del minijuego
        self.distanciaBloqueo = 60
        self.listaEnemigos = []

        # tiempo y spawns
        self.tiempoSpawn = 1000
        self.ultimoSpawn = pg.time.get_ticks()

    def manejarEventos(self, eventos):
        for evento in eventos:
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_ESCAPE: # si se presiona escape
                    self.proximoEstado == "MENU" # simula un menu de pausa
                
                # mirar hacia:
                elif evento.key in [pg.K_w, pg.K_UP]: self.direccionLupi = "ARRIBA"
                elif evento.key in [pg.K_s, pg.K_DOWN]: self.direccionLupi = "ABAJO"
                elif evento.key in [pg.K_a, pg.K_LEFT]: self.direccionLupi = "IZQUIERDA"
                elif evento.key in [pg.K_d, pg.K_RIGHT]: self.direccionLupi = "DERECHA"
    
    def actualizar(self, dt):
        # actualiza la posicion de lupi
        if self.direccionLupi == "ARRIBA":
            self.rectLupi.center = (self.cx, self.cy - self.distanciaBloqueo)
        elif self.direccionLupi == "ABAJO":
            self.rectLupi.center = (self.cx, self.cy + self.distanciaBloqueo)
        elif self.direccionLupi == "IZQUIERDA":
            self.rectLupi.center = (self.cx - self.distanciaBloqueo, self.cy)
        elif self.direccionLupi == "DERECHA":
            self.rectLupi.center = (self.cx + self.distanciaBloqueo, self.cy)

        # spawn de enemigos
        tiempoActual = pg.time.get_ticks()
        if tiempoActual - self.ultimoSpawn >= self.tiempoSpawn:
            direccionRandom = random.choice(["ARRIBA", "ABAJO", "IZQUIERDA", "DERECHA"])
            tipoRandom = random.choice(["POLILLA", "VIENTO"]) # la polilla aun falta por ver si finalmente se incluira, no se ha consultado con psicologia aun
            self.listaEnemigos.append(Enemigo(direccionRandom, tipoRandom, self.ancho, self.alto))
            self.ultimoSpawn = tiempoActual

        for enemigo in self.listaEnemigos[:]:
            enemigo.actualizar(dt)

            # si lupi choca con el enemigo, se quita el enemigo
            if self.rectLupi.colliderect(enemigo.rect):
                self.listaEnemigos.remove(enemigo)
                continue
            
            # si un enemigo choca con la vela, se reduce la vida
            if self.rectVela.colliderect(enemigo.rect):
                self.vidaVela -= 25
                self.listaEnemigos.remove(enemigo)
        
        # si la vela se apaga, vuelve al menu
        if self.vidaVela <= 0:
            self.proximoEstado = "MENU"

    def dibujar(self, pantalla):
        pantalla.fill((25, 30, 35))

        pg.draw.line(pantalla, (40, 35, 55), (self.cx, 0), (self.cx, self.alto), 2) # lineas para el mapa
        pg.draw.line(pantalla, (40, 35, 55), (0, self.cy), (self.ancho, self.cy), 2)

        pg.draw.circle(pantalla, (255, 200, 80), (self.cx, self.cy), 20) # simula la vela en el centro de la pantalla

        for enemigo in self.listaEnemigos:
            enemigo.dibujar(pantalla) # dibuja los enemigos
        
        pg.draw.rect(pantalla, (100, 220, 255), self.rectLupi)

        pg.draw.rect(pantalla, (200, 50, 50), (self.ancho //2 - 100, 25, 200, 15)) # fondo de la barra
        pg.draw.rect(pantalla, (50, 200, 100), (self.ancho //2 - 100, 25, max(0, int(self.vidaVela * 2)), 15)) # vida
        pg.draw.rect(pantalla, (255, 255, 255), (self.ancho //2 - 100, 25, 200, 15), 2) # borde