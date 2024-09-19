class ColaSimple:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def obtener_mayor(self):
        if not self.esta_vacia():
            return max(self.items)
        else:
            return None

# Ejemplo de uso:
mi_cola = Cola()
mi_cola.encolar(3)
mi_cola.encolar(1)
mi_cola.encolar(5)
mi_cola.encolar(2)

numero_mayor = mi_cola.obtener_mayor()
print("El número mayor en la cola es:", numero_mayor)