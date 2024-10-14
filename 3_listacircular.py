from nodo import Nodo

class ListaCircular:
    def __init__(self):
        self.p = None

    def es_vacia(self):
        return self.p is None

    def agregar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.es_vacia():
            self.p = nuevo_nodo
            self.p.siguiente = self.p
        else:
            actual = self.p
            while actual.siguiente != self.p:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.p

    def mostrar_lista(self):
        if self.es_vacia():
            return "la lista esta vacia."
        actual = self.p
        valores = []
        while True:
            valores.append(actual.valor)
            actual = actual.siguiente
            if actual == self.p:
                break
        return '\n'.join(valores) + '\n'

    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.es_vacia():
            self.p = nuevo_nodo
            self.p.siguiente = self.p
        else:
            actual = self.p
            while actual.siguiente != self.p:
                actual = actual.siguiente
            nuevo_nodo.siguiente = self.p
            actual.siguiente = nuevo_nodo
            self.p = nuevo_nodo

    def eliminar_inicio(self):
        if self.es_vacia():
            return "la lista esta vacia."
        if self.p.siguiente == self.p:
            self.p = None
        else:
            actual = self.p
            while actual.siguiente != self.p:
                actual = actual.siguiente
            self.p = self.p.siguiente
            actual.siguiente = self.p

    def eliminar_final(self):
        if self.es_vacia():
            return "la lista esta vacia."
        if self.p.siguiente == self.p:
            self.p = None
        else:
            actual = self.p
            anterior = None
            while actual.siguiente != self.p:
                anterior = actual
                actual = actual.siguiente
            anterior.siguiente = self.p



if __name__ == "__main__":
    lista = ListaCircular()
    lista.agregar_final("ana")
    lista.agregar_final("bernardo")
    lista.agregar_final("carlos")
    print(lista.mostrar_lista())

    lista.agregar_inicio("darwin")
    print(lista.mostrar_lista())

    lista.eliminar_inicio()
    print(lista.mostrar_lista())

    lista.eliminar_final()
    print(lista.mostrar_lista())
