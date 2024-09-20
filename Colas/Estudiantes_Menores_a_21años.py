class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ColaSimple:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:
            self.frente = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
        self.final = nuevo_nodo

    def desencolar(self):
        if self.frente is None:
            return None
        else:
            dato = self.frente.dato
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            return dato

    def esta_vacia(self):
        return self.frente is None

cola_principal = ColaSimple()
edades = [20, 22, 19, 21, 23, 18, 20, 21, 19, 22, 20, 21, 19, 22, 20, 21, 19, 22, 20, 21]
for edad in edades:
    cola_principal.encolar(edad)

cola_auxiliar = ColaSimple()
while not cola_principal.esta_vacia():
    edad = cola_principal.desencolar()
    if edad < 21:
        cola_auxiliar.encolar(edad)

print("edades de los estudiantes menores de 21 años:")
while not cola_auxiliar.esta_vacia():
    edad = cola_auxiliar.desencolar()
    print(edad)