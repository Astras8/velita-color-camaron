import pygame

# inicia el juego
pygame.init()

# fondos
fondo = ["fondoMenu.jpeg"]

# ventana
anchoVentana = 1280
altoVentana = 720
screen = pygame.display.set_mode((anchoVentana, altoVentana))

clock = pygame.time.Clock()
dt = 0

fondoMenuPrincipal = pygame.image.load(fondo[0]).convert_alpha()

rectFondoMenuPrincipal = fondoMenuPrincipal.get_rect()
rectFondoMenuPrincipal.center = (anchoVentana // 2, altoVentana // 2)

# loop del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill((51, 21, 57))
    screen.blit(fondoMenuPrincipal, rectFondoMenuPrincipal)

    pygame.display.flip()
