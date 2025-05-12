class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        # Función que permite acceder a la instancia única de la clase
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        # El constructor es privado para asegurarnos de que sólo se puede crear una instancia
        if Singleton.__instance != None:
            raise Exception("Esta clase es un singleton, no se pueden crear más de una instancia.")
        else:
            Singleton.__instance = self

# Creamos dos instancias de la clase Singleton
singleton1 = Singleton.getInstance()
singleton2 = Singleton.getInstance()

# Comprobamos si ambas instancias son la misma
print(singleton1 is singleton2)