import pygame as pg

class Colision:
    def resolver(self, jugador, objetos):
        for objeto in objetos:
            if not jugador.rect.colliderect(objeto.rect):
                continue
            
            solx = self._solapamientox(jugador.rect, objeto.rect)
            soly = self._solapamientoy(jugador.rect, objeto.rect)
            
            if solx < soly:
                if jugador.rect.centerx < objeto.rect.centerx:
                    jugador.posX -= solx
                else:
                    jugador.posX += solx
            else:
                if jugador.rect.centery < objeto.rect.centery:
                    jugador.posY -= soly
                else:
                    jugador.posY += soly
            
            jugador.rect.x = int(jugador.posX)
            jugador.rect.y = int(jugador.posY)
            
    def _solapamientox(self, rect1, rect2):
        return min(rect1.right, rect2.right) - max(rect1.left, rect2.left)
    
    def _solapamientoy(self, rect1, rect2):
        return min(rect1.bottom, rect2.bottom) - max(rect1.top, rect2.top)
    