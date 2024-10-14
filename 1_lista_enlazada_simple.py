from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_multiplos_de_dos(self):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor % 2 == 0:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
            else:
                anterior = actual
            actual = actual.siguiente

lista = ListaEnlazada()
lista.insertar_al_final(1)
lista.insertar_al_final(2)
lista.insertar_al_final(3)
lista.insertar_al_final(4)
lista.insertar_al_final(5)
lista.insertar_al_final(6)
lista.insertar_al_final(7)
lista.insertar_al_final(8)
lista.insertar_al_final(9)
lista.insertar_al_final(10)
lista.insertar_al_final(11)
lista.insertar_al_final(12)

lista.eliminar_multiplos_de_dos()

actual = lista.cabeza
while actual:
    print(actual.valor)
    actual = actual.siguiente