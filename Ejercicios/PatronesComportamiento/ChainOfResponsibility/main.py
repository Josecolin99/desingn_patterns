# Definición de la clase Manejador Base
class Manejador:
    def __init__(self, sucesor=None):
        self._sucesor = sucesor

    def manejar_peticion(self, peticion):
        manejada = self._manejar(peticion)
        if not manejada:
            self._sucesor.manejar_peticion(peticion)

    def _manejar(self, peticion):
        raise NotImplementedError('La implementación debe hacerse en una subclase')

# Definición de la clase Manejador Concreto A
class ManejadorConcretoA(Manejador):
    def _manejar(self, peticion):
        if 0 < peticion <= 10:
            print(f"Peticion {peticion} gestionada por ManejadorConcretoA")
            return True
        else:
            return False

# Definición de la clase Manejador Concreto B
class ManejadorConcretoB(Manejador):
    def _manejar(self, peticion):
        if 10 < peticion <= 20:
            print(f"Peticion {peticion} gestionada por ManejadorConcretoB")
            return True
        else:
            return False

# Definición de la clase Manejador Concreo C
class ManejadorConcretoC(Manejador):
    def _manejar(self, peticion):
        if 20 < peticion <= 30:
            print(f"Petición {peticion} gestionada por ManejadorConcretoC")
            return True
        else:
            return False

# Definición de la clase Manejador por defecto
class ManejadorPorDefecto(Manejador):
    def _manejar(self, peticion):
        print(f"No hay manejador definido para la petición {peticion}")
        return True

# Configuramos la cadena de responsabilidad
manejador_a = ManejadorConcretoA()
manejador_b = ManejadorConcretoB()
manejador_c = ManejadorConcretoC()
manejador_defecto = ManejadorPorDefecto()

manejador_a._sucesor = manejador_b
manejador_b._sucesor = manejador_c
manejador_c._sucesor = manejador_defecto

for peticion in [5, 15, 25, 35]:
    manejador_a.manejar_peticion(peticion)