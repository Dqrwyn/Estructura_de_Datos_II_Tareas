class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def mostrar_pares(self):
        if not self.esta_vacia():
            print("Los numeros pares en la cola son:")
            for item in self.items:
                if item % 2 == 0:
                    print(item)
        else:
            print("La cola está vacía.")

# Ejemplo de uso:
mi_cola = Cola()
mi_cola.encolar(3)
mi_cola.encolar(1)
mi_cola.encolar(5)
mi_cola.encolar(2)
mi_cola.encolar(4)

mi_cola.mostrar_pares()