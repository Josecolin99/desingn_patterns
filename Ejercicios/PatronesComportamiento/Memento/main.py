# Definición de la clase Memento
class Memento:
    def __init__(self, estado):
        self._estado = estado

    def obtener_estado(self):
        return self._estado

# Definición de la clase Originador
class Originador:
    def __init__(self, estado):
        self._estado = estado

    def establecer_estado(self, estado):
        print("Originador: estableciendo estado a:", estado)
        self._estado = estado

    def crear_memento(self):
        print("Originador: Creando Memento.")
        return Memento(self._estado)

    def establecer_memento(self, memento):
        estado = memento.obtener_estado()
        print("Originador: estado después de restaurar Memento:", estado)
        self._estado = estado

# Definición de la clase Cuidadora
class Cuidadora:
    def __init__(self, Originador):
        self._mementos = []
        self._Originador = Originador

    def backup(self):
        print("\nCuidadora: Guardando estado memento...")
        self._mementos.append(self._Originador.crear_memento())

    def deshacer(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print("Cuidadora: Restaurando estado a:", memento.obtener_estado())
        try:
            self._Originador.establecer_memento(memento)
        except Exception as e:
            self.deshacer()

originador = Originador("1-2-3-4-5.")
cuidadora = Cuidadora(originador)
cuidadora.backup()
originador.establecer_estado("1-2-3-4.")
cuidadora.backup()
originador.establecer_estado("1-2-3.")
cuidadora.backup()
originador.establecer_estado("1-2.")
print("\n Estado actual: ", originador._estado, "\n")
cuidadora.deshacer()
cuidadora.deshacer()
cuidadora.deshacer()