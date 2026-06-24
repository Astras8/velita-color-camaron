### superclase para todas las escenas del juego ###

class Escena:
    def __init__(self):
        ## atributos base ##
        # cual es el proximo estado despues del actual
        self.proximoEstado = None

        # traslada los datos del estado actual al proximo
        self.persistir = {}

    def manejarEventos(self, eventos):
        pass
    
    def actualizar(self, dt):
        pass

    def dibujar(self, pantalla):
        pass

    pass