# Definición de la clase abstracta / interfaz para las diferentes expresiones
class Expresion:
    def interpretar(self):
        pass

# Definición de la clase expresión terminal Numero
class Numero(Expresion):
    def __init__(self, valor):
        self.valor = valor

    def interpretar(self):
        return self.valor

# Definición de la clase expresión no terminal sumar
class Sumar(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def interpretar(self):
        return self.izquierda.interpretar() + self.derecha.interpretar()

# Definición de la clase expresión no terminal restar
class Restar(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def interpretar(self):
        return self.izquierda.interpretar() - self.derecha.interpretar()

# Definición de la clase expresión no terminal multiplicar
class Multiplicar(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def interpretar(self):
        return self.izquierda.interpretar() * self.derecha.interpretar()

# Definición de la clase expresión no terminal dividir
class Dividir(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def interpretar(self):
        return self.izquierda.interpretar() / self.derecha.interpretar()

exp1 = Sumar(Numero(7), Numero(3))
print(exp1.interpretar())

exp2 = Multiplicar(Numero(2), Restar(Numero(8), Numero(2)))
print(exp2.interpretar())