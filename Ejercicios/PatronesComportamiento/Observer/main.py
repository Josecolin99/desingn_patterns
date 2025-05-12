# Definición de la Interfaz Observador
class Observador:
    def actualizar(self, publicador):
        pass

# Definición de la clase Publicador
class Publicador():
    def __init__(self):
        self._observadores = []
        self._estado_publicador = None

    def aniadir(self, observador):
        self._observadores.append(observador)

    def quitar(self, observador):
        self._observadores.remove(observador)

    def notificar(self):
        for observador in self._observadores:
            observador.actualizar(self)

    def obtener_estado(self):
        return self._estado_publicador

    def establecer_estado(self, estado):
        self._estado_publicador = estado
        self.notificar()

# Definición de un observador concreto (A)
class ObservadorConcretoA(Observador):
    def actualizar(self, publicador):
        if publicador.obtener_estado() == 1:
            print("Observador Concreto A: Reacciona a evento")

# Definición de un observador concreto (B)
class ObservadorConcretoB(Observador):
    def actualizar(self, publicador):
        if publicador.obtener_estado() == 0:
            print("Observador Concreto B: Reacciona a evento")

publicador = Publicador()

observador_a = ObservadorConcretoA()
publicador.aniadir(observador_a)

observador_b = ObservadorConcretoB()
publicador.aniadir(observador_b)

publicador.establecer_estado(0)
publicador.establecer_estado(1)