from abc import ABC, abstractmethod

# Definición del interfaz Clase que implementarán las clases concretas
class Clase(ABC):

    def plantilla(self):
        self.operacion1()
        self.operacion2()

    @abstractmethod
    def operacion1(self):
        pass

    @abstractmethod
    def operacion2(self):
        pass

# Definición de una Clase Concreta (A)
class ClaseConcretaA(Clase):

    def operacion1(self):
        print("Operación 1 para ClaseConcretaA")

    def operacion2(self):
        print("Operación 2 para ClaseConcretaA")


# Definición de una Clase Concreta (B)
class ClaseConcretaB(Clase):

    def operacion1(self):
        print("Operación 1 para ClaseConcretaB")

    def operacion2(self):
        print("Operación 2 para ClaseConcretaB")


clase_a = ClaseConcretaA()
clase_a.plantilla()
clase_b = ClaseConcretaB()
clase_b.plantilla()