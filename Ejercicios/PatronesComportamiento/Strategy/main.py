from abc import ABC, abstractmethod

# Definición de la clase abstracta Estrategia
class Estrategia(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

# Definición de una clase Estrategia Concreta (A)
class EstrategiaConcretaA(Estrategia):
    def ejecutar(self):
        print("Ejecutando la estrategia A")

# Definición de una clase Estrategia Concreta (B)
class EstrategiaConcretaB(Estrategia):
    def ejecutar(self):
        print("Ejecutando la estrategia B")

# Definición de la clase Contexto
class Contexto:
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def establecer_estrategia(self, estrategia):
        self._estrategia = estrategia

    def ejecutar_estrategia(self):
        self._estrategia.ejecutar()

contexto = Contexto(EstrategiaConcretaA())
contexto.ejecutar_estrategia()
contexto.establecer_estrategia(EstrategiaConcretaB())
contexto.ejecutar_estrategia()
contexto.establecer_estrategia(EstrategiaConcretaA())
contexto.ejecutar_estrategia()