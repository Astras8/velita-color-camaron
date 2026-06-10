import pygame as pg

class Jugador(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.Surface((80, 120))
        self.image.fill((100, 200, 255))

        self.rect = self.image.get_rect(center = (x, y))

        self.posX = float(self.rect.x)
        self.posY = float(self.rect.y)
        self.velocidad = 300.0

    def actualizar(self, dt, anchoMapa, altoMapa):
        teclas = pg.key.get_pressed()

        dirX = 0
        dirY = 0

        if teclas[pg.K_LSHIFT]:
            self.velocidad = 600
        else:
            self.velocidad = 300

        if teclas[pg.K_a] or teclas[pg.K_LEFT]:
            dirX -= 1

        if teclas[pg.K_d] or teclas[pg.K_RIGHT]:
            dirX += 1
        
        if teclas[pg.K_w] or teclas[pg.K_UP]:
            dirY -= 1
        
        if teclas[pg.K_s] or teclas[pg.K_DOWN]:
            dirY += 1

        if dirX != 0 and dirY != 0:
            magnitud = (dirX ** 2 + dirY ** 2)**0.5
            dirX /= magnitud
            dirY /= magnitud

        self.posX += dirX * self.velocidad * dt
        self.posY += dirY * self.velocidad * dt

        # clamping
        self.posX = max(0.0, min(self.posX, float(anchoMapa - self.rect.width)))
        self.posY = max(0.0, min(self.posY, float(altoMapa - self.rect.height)))

        self.rect.x = int(self.posX)
        self.rect.y = int(self.posY)
    pass

    def dibujar(self, pantalla, camara):
        posPantallaX = self.rect.x - camara.x
        posPantallaY = self.rect.y - camara.y
        pantalla.blit(self.image, (posPantallaX, posPantallaY))
pass