class Camara:
    def __init__(self, ancho, alto):
        ## atributos base ##
        # coordenadas base de la camara
        self.x = 0
        self.y = 0
        
        # alto y ancho de la pantalla
        self.ancho = ancho
        self.alto = alto
        # mitad del alto y ancho de la pantalla
        self.mitadAncho = ancho // 2
        self.mitadAlto = alto // 2

    def actualizar(self, objetivo, anchoMapa, altoMapa):
        # coordenadas en un mundo ideal donde el clamping no existe
        xIdeal = objetivo.rect.centerx - self.mitadAncho
        yIdeal = objetivo.rect.centery - self.mitadAlto

        # clamping, para el lamento de las coordenadas ideales
        self.x = max(0, min(xIdeal, anchoMapa - self.ancho))
        self.y = max(0, min(yIdeal, altoMapa - self.alto))