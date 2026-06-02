from abc import ABC, abstractmethod

class ieventlistener(ABC):
    @abstractmethod
    def notificar(self, event: str):
        pass
    