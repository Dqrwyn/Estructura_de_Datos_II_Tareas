class Cola:
    def __init__(self, max):
        self.front = -1
        self.back = -1
        self.max = max
        self.Cola = [None] * (max + 1)

    def Enqueue(self, dato):
        if self.es_llena():
            print("la cola es llena")
            return
        if self.front == -1:
            self.front = 0
        self.back = (self.back +1) % self.max
        self.Cola[self.back] = dato

    def Dequeue(self):
        if self.es_vacia():
            print("la cola es vacia")
            return
        dato = self.Cola[self.front]
        if self.front == self.back:
            self.front = self.back = -1
        else:
            self.front = (self.front + 1) % self.max
        return dato

    def Size(self):
        if self.es_vacia():
            return 0
        return (self.back - self.front + 1) % self.max

    def es_llena(self):
        return (self.back + 1) % self.max == self.front

    def es_vacia(self):
        return self.front == -1

    def mostrar(self):
        if self.es_vacia():
            print("la cola es vacia")
            return
        for i in range(self.Size()):
            print(self.Cola[(self.front + i) % self.max], end=" ")
        print()

cola = Cola(4)
cola.Enqueue(10)
cola.Enqueue(20)
cola.Enqueue(30)
cola.mostrar()
print("tamaño de la colaes :", cola.Size())
cola.Dequeue()
cola.mostrar() 