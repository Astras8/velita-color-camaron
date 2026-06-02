from abc import ABC, abstractmethod
import pygame

class EstadoJuego(ABC):  
    @abstractmethod
    def manejo_imput(self, event):
        pass
    
    @abstractmethod
    def actualizar(self):
        pass
    
    @abstractmethod
    def draw(self, fondo: pygame.surface):
        pass         
    pass