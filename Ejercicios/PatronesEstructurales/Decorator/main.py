from abc import ABC, abstractmethod

# Definición de la clase base
class Componente(ABC):
    def operacion(self):
        pass

# Definición de la clase concreta que implementa la clase base
class ComponenteConcreto(Componente):
    def operacion(self):
        print("Realizando operación en Componente Concreto")

# Definición de la clase decoradora base que también implementa la clase base
class Decorador(Componente):
    def __init__(self, componente):
        self._componente = componente

    def operacion(self):
        self._componente.operacion()

# Definición de la clase concreta decoradora que agrega funcionalidad al componente base
class DecoradorConcreto(Decorador):
    def __init__(self, componente):
        super().__init__(componente)

    def operacion(self):
        super().operacion()
        self.agregar_funcionalidad()

    def agregar_funcionalidad(self):
        print("Agregando funcionalidad al Componente")

componente = ComponenteConcreto()
decorador = DecoradorConcreto(componente)
decorador.operacion()