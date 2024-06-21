class Cola:
    
    def __init__(self):
        self.lista = []

    def agregar(self, elemento):
        self.lista.append(elemento)

    def quitar(self):
        if not self.estaVacia():
            return self.lista.pop(0)
        else:
            print("La lista esta vacia")

    def estaVacia(self):
        return len(self.lista) == 0
    
    def cantidad(self):
        return len(self.lista)
    
cola = Cola()

cola.agregar(2)
cola.agregar(4)
cola.agregar(6)

print(cola.lista)

print(f"Se quito: {cola.quitar()}")

print(cola.lista)
