# Definición del interfaz Elemento
class Elemento:
    def aceptar(self, visitor):
        pass

# Definición de una clase concreta (A) del tipo Elemento
class ElementoConcretoA(Elemento):
    def aceptar(self, visitor):
        visitor.visitar_elemento_a(self)


# Definición de una clase concreta (B) del tipo Elemento
class ElementoConcretoB(Elemento):
    def aceptar(self, visitor):
        visitor.visitar_elemento_b(self)

# Definición del interfaz Visitor
class Visitor:
    def visitar_elemento_a(self, elemento):
        pass
    def visitar_elemento_b(self, elemento):
        pass

# Definición de una clase concreta (1) del tipo visitor
class VisitorConcreto1(Visitor):
    def visitar_elemento_a(self, elemento):
        print("Visitor 1: Elemento A")
    def visitar_elemento_b(self, elemento):
        print("Visitor 1: Elemento B")

# Definición de una clase concreta (2) del tipo visitor
class VisitorConcreto2(Visitor):
    def visitar_elemento_a(self, elemento):
        print("Visitor 2: Elemento A")
    def visitar_elemento_b(self, elemento):
        print("Visitor 2: Elemento B")

elementos = [ElementoConcretoA(), ElementoConcretoB(), ElementoConcretoA()]
visitor1 = VisitorConcreto1()
visitor2 = VisitorConcreto2()

for elemento in elementos:
    elemento.aceptar(visitor1)
for elemento in elementos:
    elemento.aceptar(visitor2)