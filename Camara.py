class Camara:
    def __init__(self, ancho, alto):
        self.x = 0
        self.y = 0
        
        self.ancho = ancho
        self.alto = alto
        self.mitadAncho = ancho // 2
        self.mitadAlto = alto // 2

    def actualizar(self, objetivo, anchoMapa, altoMapa):
        xIdeal = objetivo.rect.centerx - self.mitadAncho
        yIdeal = objetivo.rect.centery - self.mitadAlto

        # clamping
        self.x = max(0, min(xIdeal, anchoMapa - self.ancho))
        self.y = max(0, min(yIdeal, altoMapa - self.alto))