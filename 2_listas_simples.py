from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def nombre_mas_largo(self):
        if not self.cabeza:
            return None
        actual = self.cabeza
        nombre_largo = actual.valor
        while actual:
            if len(actual.valor) > len(nombre_largo):
                nombre_largo = actual.valor
            actual = actual.siguiente
        return nombre_largo

    def unir_y_ordenar(self, otra_lista):
        nombres = []
        actual = self.cabeza
        while actual:
            nombres.append(actual.valor)
            actual = actual.siguiente

        actual = otra_lista.cabeza
        while actual:
            nombres.append(actual.valor)
            actual = actual.siguiente

        nombres.sort()
        lista_unida = ListaEnlazada()
        for nombre in nombres:
            lista_unida.agregar(nombre)
        return lista_unida

    def mostrar(self):
        nombres = []
        actual = self.cabeza
        while actual:
            nombres.append(actual.valor)
            actual = actual.siguiente
        return nombres

# Crear las listas de ejemplo
lista1 = ListaEnlazada()
lista1.agregar("ana")
lista1.agregar("bernardo")
lista1.agregar("carlos")

lista2 = ListaEnlazada()
lista2.agregar("darwin")
lista2.agregar("fernando")
lista2.agregar("gabriela")

# Parte a: Mostrar la lista que contenga el nombre más largo
nombre_largo1 = lista1.nombre_mas_largo()
nombre_largo2 = lista2.nombre_mas_largo()

if len(nombre_largo1) > len(nombre_largo2):
    print(f"El nombre más largo está en lista1: {nombre_largo1}")
else:
    print(f"El nombre más largo está en lista2: {nombre_largo2}")

# Parte b: Unir y ordenar las dos listas alfabéticamente
lista_unida_ordenada = lista1.unir_y_ordenar(lista2)
print("Lista unida y ordenada alfabéticamente:", lista_unida_ordenada.mostrar())
