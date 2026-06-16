import pygame as pg

class Enemigo:
    def __init__(self, direccion, tipo, ancho, alto):
        self.direccion = direccion
        self.tipo = tipo

        self.velocidad = 250.0 if tipo == "POLILLA" else 450.0

        cx = ancho // 2
        cy = alto // 2

        if self.direccion == "ARRIBA":
            self.rect = pg.Rect(cx - 15, 0, 30, 30) if tipo == "POLILLA" else pg.Rect(cx - 20, 0, 40, 15)
        elif self.direccion == "ABAJO":
            self.rect = pg.Rect(cx - 15, alto, 30, 30) if tipo == "POLILLA" else pg.Rect(cx - 20, alto, 40, 15)
        elif self.direccion == "IZQUIERDA":
            self.rect = pg.Rect(0, cy - 15, 30, 30) if tipo == "POLILLA" else pg.Rect(0, cy - 20, 15, 40)
        elif self.direccion == "DERECHA":
            self.rect = pg.Rect(ancho, cy - 15, 30, 30) if tipo == "POLILLA" else pg.Rect(ancho, cy - 20, 15, 40)

        self.posX = float(self.rect.x)
        self.posY = float(self.rect.y)
    
    def actualizar(self, dt):
        if self.direccion == "ARRIBA": self.posY += self.velocidad * dt
        if self.direccion == "ABAJO": self.posY -= self.velocidad * dt
        if self.direccion == "IZQUIERDA": self.posX += self.velocidad * dt
        if self.direccion == "DERECHA": self.posX -= self.velocidad * dt

        self.rect.x = int(self.posX)
        self.rect.y = int(self.posY)

    def dibujar(self, pantalla):
        color = (230, 120, 50) if self.tipo == "POLILLA" else (130, 200, 240)
        pg.draw.rect(pantalla, color, self.rect)