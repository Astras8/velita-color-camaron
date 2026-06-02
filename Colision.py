from abc import ABC, abstractmethod
import pygame

class colision(ABC):
    @abstractmethod
    def get_rect(self)->pygame.rect:
        pass
    