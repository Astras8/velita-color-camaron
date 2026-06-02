import sys, pygame as pg, Boton, ControladorEstados
from escenas.EscenaIntro import EscenaIntro as EscenaIntro
from escenas.EscenaMenuPrincipal import EscenaMenuPrincipal as EscenaMenuPrincipal

# funciones para los botones de prueba
def empezarJuego():
    print("Empezando el juego, yippeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

def salirJuego():
    pg.quit()
    sys.exit()

# inicia el juego
pg.init()

# fondos de prueba
fondo = ["assets/imagenes/fondoMenu.jpeg"]

# botones de prueba
botonComenzar = Boton.Boton(x = 300, y = 200, ancho = 200, alto = 60, texto = "Empezar", callback = empezarJuego, colorBase = (40, 160, 80), colorHover = (60, 200, 100))
botonSalir = Boton.Boton(x = 300, y = 300, ancho = 200, alto = 60, texto = "Salir", callback = salirJuego, colorBase = (180, 40, 40), colorHover = (220, 60, 60))

botones = [botonComenzar, botonSalir]

# ventana
anchoVentana = 1980
altoVentana = 1020
pantalla = pg.display.set_mode((anchoVentana, altoVentana), pg.FULLSCREEN | pg.SCALED)

reloj = pg.time.Clock()
dt = 0

# logo
logo = pg.image.load("assets/imagenes/prospera.png").convert_alpha()

rectLogo = logo.get_rect(center = (anchoVentana // 2,  altoVentana // 2))

# fondos
fondoMenuPrincipal = pg.image.load(fondo[0]).convert_alpha()

rectFondoMenuPrincipal = fondoMenuPrincipal.get_rect()
rectFondoMenuPrincipal.center = (anchoVentana // 2, altoVentana // 2)

# estados de juego de prueba
listaEstados = {
    "INTRO": EscenaIntro(anchoVentana, altoVentana, logo),
    "MENU": EscenaMenuPrincipal(anchoVentana, altoVentana)

}

# controlador
controlador = ControladorEstados.ControladorEstados(estadoInicial = "INTRO", listaEstados = listaEstados)

# loop del juego
while True:
    posicionMouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    dt = reloj.tick(60) / 1000.0

    eventos = pg.event.get()
    for evento in eventos:
        if evento.type == pg.QUIT:
            pg.quit()

        elif evento.type == pg.KEYDOWN:
            # cambiar a modo ventana
            if evento.key == pg.K_F11:
                pg.display.toggle_fullscreen()

    controlador.manejarEventos(eventos)
    controlador.actualizar(dt)
    controlador.dibujar(pantalla)

    pg.display.flip()
