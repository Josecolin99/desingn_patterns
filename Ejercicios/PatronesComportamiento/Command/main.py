# Definición de la clase Receptor que va a recibir y ejecutar las acciones
class Receptor:
    def ejecutar(self):
        print("Ejecutando acción en el receptor.")

# Definición de la clase Comando que es la interfaz común para todos los comandos
class Comando:
    def ejecutar(self):
        pass

# Definición de una clase ComandoConcreto para cada acción que pueda realizar el receptor
class ConcreteCommand(Comando):
    def __init__(self, receptor):
        self.receptor = receptor

    def ejecutar(self):
        self.receptor.ejecutar()

# Definición de la clase Invocador que se encarga de manejar los comandos
class Invocador:
    def establecer_comando(self, comando):
        self.comando = comando

    def ejecutar_comando(self):
        self.comando.ejecutar()

# Creamos instancias de las clases
receptor = Receptor()
comando_concreto = ConcreteCommand(receptor)
invocador = Invocador()

# Asignamos el ComandoConcreto al Invocador
invocador.establecer_comando(comando_concreto)

# Ejecutamos la acción a través del Invocador
invocador.ejecutar_comando()
