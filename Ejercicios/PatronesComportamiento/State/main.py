# Definición de la clase Contexto
class Contexto:
    def __init__(self):
        self._estado = None

    def establecer_estado(self, estado):
        self._estado = estado

    def peticion(self):
        self._estado.manejar()

# Definición del interfaz Estado
class Estado:
    def manejar(self):
        pass

# Definición de una clase Estado Concreto (A)
class EstadoConcretoA(Estado):
    def manejar(self):
        print("Manejando la petición con estado A")

# Definición de una clase Estado Concreto (B)
class EstadoConcretoB(Estado):
    def manejar(self):
        print("Manejando la petición con estado B")

context = Contexto()
estadoA = EstadoConcretoA()
estadoB = EstadoConcretoB()
context.establecer_estado(estadoA)
context.peticion()
context.establecer_estado(estadoB)
context.peticion()