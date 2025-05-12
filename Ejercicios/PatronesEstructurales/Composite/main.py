from abc import ABC, abstractmethod

class Componente(ABC):
    @abstractmethod
    def operacion(self):
        pass

class Hoja(Componente):
    def operacion(self):
        print("Realizando operación en Hoja")

class Compuesto(Componente):
    def __init__(self):
        self._elementos = []

    def agregar_elemento(self, elemento):
        self._elementos.append(elemento)

    def quitar_elemento(self, elemento):
        self._elementos.remove(elemento)

    def operacion(self):
        print("Realizando operación en Composición")
        for elemento in self._elementos:
            elemento.operacion()

hoja1 = Hoja()
hoja2 = Hoja()

comp1 = Compuesto()
comp1.agregar_elemento(hoja1)
comp1.agregar_elemento(hoja2)

hoja3 = Hoja()

comp2 = Compuesto()
comp2.agregar_elemento(comp1)
comp2.agregar_elemento(hoja3)

comp2.operacion()