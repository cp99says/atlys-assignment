from abc import ABC, abstractmethod

class ingest(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def validate():
        pass
    
    @abstractmethod
    def write():
        pass
        