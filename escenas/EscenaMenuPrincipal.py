import pygame as pg
from estados.EstadoJuego import EstadoJuego

class EscenaMenuPrincipal(EstadoJuego):
    def __init__(self, ancho, alto):
        super().__init__()

        # imagen provisional
        fondo = pg.image.load("assets/imagenes/fondoMenu.jpeg").convert()
        self.fondo = pg.transform.scale(fondo, (ancho, alto))

        # iluminacion, seria mejor cambiarla a una elipse, se veria mas natural
        # falta agregar movimiento y parpadeos a la llama de la vela 
        self.posVela = (ancho // 2, (alto // 2) + 150)

        self.radioActual = 0
        self.radioMaximo = 600
        self.velocidadEncendido = 200

        self.mascaraLuz = pg.Surface((ancho, alto)).convert()

        diametroMax = int(self.radioMaximo * 2)
        self.texturaLuz = pg.Surface((diametroMax, diametroMax)).convert()
        self.texturaLuz.fill((0, 0, 0))

        # botones provisionales
        self.fuente = pg.font.Font(None, 50)
        
        self.COLOR_NORMAL = (200, 200, 200)
        self.COLOR_HOVER = (255, 100, 100)
        
        self.hoverJugar = False
        self.hoverSalir = False

        self.centroX = ancho // 2
        self.yJugar = alto - 150
        self.ySalir = alto - 90

        self.rectJugar = self.fuente.render("JUGAR", True, self.COLOR_NORMAL).get_rect(center = (self.centroX, self.yJugar))
        self.rectSalir = self.fuente.render("SALIR", True, self.COLOR_NORMAL).get_rect(center = (self.centroX, self.ySalir))

        for r in range(int(self.radioMaximo), 0, -2):
            intensidad = int(255 * (1 - (r / self.radioMaximo)))
            color = (intensidad, intensidad, intensidad)
            pg.draw.circle(self.texturaLuz, color, (int(self.radioMaximo), int(self.radioMaximo)), r)

    def manejarEventos(self, eventos):
        for evento in eventos:
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                if self.rectJugar.collidepoint(evento.pos):
                    self.proximoEstado = "JUEGO"
                
                elif self.rectSalir.collidepoint(evento.pos):
                    pg.quit()
        pass

    def actualizar(self, dt):
        if self.radioActual < self.radioMaximo:
            self.radioActual += self.velocidadEncendido * dt
            if self.radioActual > self.radioMaximo:
                self.radioActual = self.radioMaximo
        
        mousePos = pg.mouse.get_pos()

        self.hoverJugar = self.rectJugar.collidepoint(mousePos)
        self.hoverSalir = self.rectSalir.collidepoint(mousePos)

    def dibujar(self, pantalla):
        pantalla.blit(self.fondo, (0, 0))

        self.mascaraLuz.fill((0, 0, 0))

        if self.radioActual > 0:
            diametroActual = int(self.radioActual * 2)

            luzEscalada = pg.transform.scale(self.texturaLuz, (diametroActual, diametroActual))

            x = int(self.posVela[0] - self.radioActual)
            y = int(self.posVela[1] - self.radioActual)

            self.mascaraLuz.blit(luzEscalada, (x, y))

        pantalla.blit(self.mascaraLuz, (0, 0), special_flags = pg.BLEND_RGB_MULT)

        # botones
        colorActualJugar = self.COLOR_HOVER if self.hoverJugar else self.COLOR_NORMAL
        textoJugar = self.fuente.render("JUGAR", True, colorActualJugar)
        pantalla.blit(textoJugar, self.rectJugar)

        colorActualSalir = self.COLOR_HOVER if self.hoverSalir else self.COLOR_NORMAL
        textoSalir = self.fuente.render("SALIR", True, colorActualSalir)
        pantalla.blit(textoSalir, self.rectSalir)

    pass