import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.value}"

# Creamos una instancia del prototipo concreto
prototype = ConcretePrototype("Prototipo 1", 1)

# Clonamos el prototipo
clone = prototype.clone()

# Cambiamos el valor del clone
clone.value = 2

# Mostramos los valores de ambos prototipos
print(prototype)
print(clone)