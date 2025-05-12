from abc import ABC, abstractmethod

class Interfaz(ABC):
    @abstractmethod
    def metodo(self):
        pass

class ImplementacionConcreta1(Interfaz):
    def metodo(self):
        print("Implementación concreta 1")

class ImplementacionConcreta2(Interfaz):
    def metodo(self):
        print("Implementación concreta 2")

class Abstraccion:
    def __init__(self, interfaz):
        self._interfaz = interfaz

    def funcionalidad1(self):
        self._interfaz.metodo()

abstraccion1 = Abstraccion(ImplementacionConcreta1())
abstraccion1.funcionalidad1()
abstraccion2 = Abstraccion(ImplementacionConcreta2())
abstraccion2.funcionalidad1()