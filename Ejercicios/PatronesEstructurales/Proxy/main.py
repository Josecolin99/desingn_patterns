# Definición del interfaz Servicio
class InterfazServicio:
    def realizar_accion(self):
        pass

class Servicio(InterfazServicio):
    def realizar_accion(self):
        print("Realizando acción")

class Proxy(InterfazServicio):
    def __init__(self):
        self.servicio = None

    def realizar_accion(self):
        if self.servicio is None:
            self.servicio = Servicio()
        self.servicio.realizar_accion()

# Ejemplo de uso
proxy = Proxy()
proxy.realizar_accion()