class ColaSimple:
    def __init__(self, tamano):
        self.cola = [None] * tamano
        self.frente = 0
        self.final = -1
        self.tamano = tamano

    def esta_vacia(self):
        return self.frente > self.final

    def esta_llena(self):
        return self.final == self.tamano - 1

    def encolar(self, elemento):
        if self.esta_llena():
            print("la cola esta llena")
            return
        self.final += 1
        self.cola[self.final] = elemento

    def desencolar(self):
        if self.esta_vacia():
            print("la cola esta vacia")
            return None
        elemento = self.cola[self.frente]
        self.frente += 1
        return elemento

    def contar_elementos_con_a(self):
        contador = 0
        for i in range(self.frente, self.final + 1):
            if self.cola[i] and self.cola[i][0] == 'A':
                contador += 1
        return contador

cola = ColaSimple(10)

cola.encolar("hola")
cola.encolar("Adios")
cola.encolar("juan")
cola.encolar("jon")
cola.encolar("Auto")
cola.encolar("Ave")

cantidad_con_a = cola.contar_elementos_con_a()

print("la cantidad de elementos que comienzan con la letra A es:", cantidad_con_a)