from abc import ABC, abstractmethod
import pygame

class nivel(ABC):
    @abstractmethod
    def cargar_info(self):
        pass
    
    @abstractmethod
    def actualizar(self):
        pass
    
    @abstractmethod
    def draw(self, fondo: pygame.surface):
        pass
    
    @abstractmethod
    def completado(self)->bool:
        pass
    pass
