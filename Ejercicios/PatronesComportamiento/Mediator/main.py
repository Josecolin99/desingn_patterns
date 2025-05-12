# Definición del interfaz Mediador
class Mediador:
    def enviar_mensaje(self, componente, mensaje):
        pass

# Definición de la clase Mediador Concreto
class MediadorConcreto(Mediador):
    def __init__(self, componenteA, componenteB):
        self._componenteA = componenteA
        self._componenteB = componenteB

    def enviar_mensaje(self, componente, mensaje):
        if isinstance(componente, ComponenteA):
            self._componenteB.recibir_mensaje(mensaje)
        else:
            self._componenteA.recibir_mensaje(mensaje)

# Definición del interfaz Componente
class Componente:
    def __init__(self, mediador):
        self._mediador = mediador

    def enviar_mensaje(self, mensaje):
        self._mediador.enviar_mensaje(self, mensaje)

    def recibir_mensaje(self, mensaje):
        pass

# Definición de la clase del Componente A
class ComponenteA(Componente):
    def recibir_mensaje(self, mensaje):
        print("Componente A mensaje recibido: {}".format(mensaje))

# Definición de la clase del Componente B
class ComponenteB(Componente):
    def recibir_mensaje(self, mensaje):
        print("Componente B mensaje recibido: {}".format(mensaje))

# Crear los objetos necesarios
mediador = MediadorConcreto(ComponenteA(Mediador), ComponenteB(Mediador))
componentea = ComponenteA(mediador)
componenteb = ComponenteB(mediador)

# Enviar un mensaje desde Colleague1 a Colleague2 a través del Mediator
componentea.enviar_mensaje("Hola desde el componente A!")
componenteb.enviar_mensaje("Hola desde el componente B!")