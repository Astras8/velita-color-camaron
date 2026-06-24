### clase que define todos los aspectos del jugador ###

import pygame as pg

class Jugador(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        ## atributos base ##
        # imagen asociada al jugador, por ahora es una superficie con un solo color
        self.imagen = pg.Surface((80, 120))
        self.imagen.fill((100, 200, 255))

        # rectangulo del jugador
        self.rect = self.imagen.get_rect(center = (x, y))

        # coordenadas del jugador
        self.posX = float(self.rect.x)
        self.posY = float(self.rect.y)
        # velocidad base
        self.velocidad = 300.0

    def actualizar(self, dt, anchoMapa, altoMapa):
        teclas = pg.key.get_pressed()

        # direccion en x e y
        dirX = 0
        dirY = 0

        # cambios de direccion
        if teclas[pg.K_LSHIFT]:
            self.velocidad = 600 # simula el esprintar o correr
        else:
            self.velocidad = 300 # caminar, velocidad base

        if teclas[pg.K_a] or teclas[pg.K_LEFT]:
            dirX -= 1

        if teclas[pg.K_d] or teclas[pg.K_RIGHT]:
            dirX += 1
        
        if teclas[pg.K_w] or teclas[pg.K_UP]:
            dirY -= 1
        
        if teclas[pg.K_s] or teclas[pg.K_DOWN]:
            dirY += 1

        # normalizacion para evitar acumulacion de velocidad
        if dirX != 0 and dirY != 0:
            magnitud = (dirX ** 2 + dirY ** 2)**0.5
            dirX /= magnitud
            dirY /= magnitud

        self.posX += dirX * self.velocidad * dt
        self.posY += dirY * self.velocidad * dt

        # clamping
        self.posX = max(0.0, min(self.posX, float(anchoMapa - self.rect.width)))
        self.posY = max(0.0, min(self.posY, float(altoMapa - self.rect.height)))

        # coordenadas del rectangulo
        self.rect.x = int(self.posX)
        self.rect.y = int(self.posY)
    pass

    def dibujar(self, pantalla, camara):
        posPantallaX = self.rect.x - camara.x
        posPantallaY = self.rect.y - camara.y
        pantalla.blit(self.imagen, (posPantallaX, posPantallaY))
pass