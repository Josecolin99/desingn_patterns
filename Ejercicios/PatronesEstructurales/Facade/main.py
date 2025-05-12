# Definición de la clase subsistema 1
class Subsistema1:
    def operacion1(self):
        print("Operación 1 del Subsistema 1")

# Definición de la clase subsistema 2
class Subsistema2:
    def operacion2(self):
        print("Operación 2 del Subsistema 2")

# Definición de la clase subsistema 3
class Subsistema3:
    def operacion3(self):
        print("Operación 3 del Subsistema 3")

# Definición de la Fachada
class Fachada:
    def __init__(self):
        self._sistema1 = Subsistema1()
        self._sistema2 = Subsistema2()
        self._sistema3 = Subsistema3()

    def operacion_compleja(self):
        print("Operación Compleja")
        self._sistema1.operacion1()
        self._sistema2.operacion2()
        self._sistema3.operacion3()

fachada = Fachada()
fachada.operacion_compleja()
