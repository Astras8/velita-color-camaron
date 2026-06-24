### clase que controla los metodos usados por las escenas para actualizarse ###

class ControladorEstados:
    def __init__(self, estadoInicial, listaEstados):
        ## atributos base ##
        # recibe una lista de estados desde main
        self.listaEstados = listaEstados
        # el estado inicial se denomina como actual
        self.nombreEstadoActual = estadoInicial
        self.estadoActual = self.listaEstados[self.nombreEstadoActual]
    
    def cambiarEstado(self):
        proximo = self.estadoActual.proximoEstado
        
        self.estadoActual.proximoEstado = None

        self.nombreEstadoActual = proximo
        self.estadoActual = self.listaEstados[self.nombreEstadoActual]

    def actualizar(self, dt):
        # si el proximo estado no es ninguno, se cambia, si no, sigue actualizando
        if self.estadoActual.proximoEstado is not None:
            self.cambiarEstado()
        self.estadoActual.actualizar(dt)

    def manejarEventos(self, eventos):
        # deja que cada escena maneje sus eventos
        self.estadoActual.manejarEventos(eventos)
    
    def dibujar(self, pantalla):
        # deja que cada escena dibuje sus cosas
        self.estadoActual.dibujar(pantalla)

pass