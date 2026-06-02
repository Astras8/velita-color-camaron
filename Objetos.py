from abc import ABC, abstractmethod
import pygame

class objetos(ABC):
    @abstractmethod
    def actualizar(self):
        pass
    
    @abstractmethod
    def draw(self, fondo: pygame):
        pass
    pass