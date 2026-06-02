class ControladorEstados:
    def __init__(self, estadoInicial, listaEstados):
        self.listaEstados = listaEstados
        self.nombreEstadoActual = estadoInicial
        self.estadoActual = self.listaEstados[self.nombreEstadoActual]
    
    def cambiarEstado(self):
        proximo = self.estadoActual.proximoEstado
        
        self.estadoActual.proximoEstado = None

        self.nombreEstadoActual = proximo
        self.estadoActual = self.listaEstados[self.nombreEstadoActual]

    def actualizar(self, dt):
        if self.estadoActual.proximoEstado is not None:
            self.cambiarEstado()
        self.estadoActual.actualizar(dt)

    def manejarEventos(self, eventos):
        self.estadoActual.manejarEventos(eventos)
    
    def dibujar(self, pantalla):
        self.estadoActual.dibujar(pantalla)

pass