# Definición de la clase Flyweight
class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        print(f"Flyweight con estado compartido '{self.shared_state}' y estado único '{unique_state}'.")

# Definición de la Factoría Flyweight
class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self.flyweights:
            self.flyweights[shared_state] = Flyweight(shared_state)
        return self.flyweights[shared_state]

factory = FlyweightFactory()

flyweight1 = factory.get_flyweight("estado compartido")
flyweight1.operation("estado único 1")

flyweight2 = factory.get_flyweight("estado compartido")
flyweight2.operation("estado único 2")

flyweight3 = factory.get_flyweight("estado compartido 2")
flyweight3.operation("estado único 3")