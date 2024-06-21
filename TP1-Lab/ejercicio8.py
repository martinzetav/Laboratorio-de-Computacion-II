class Pila:

    def __init__(self):
        self.lista = []

    def agregar(self, elemento):
        self.lista.append(elemento)

    def quitar(self):
        if not self.estaVacia():
            return self.lista.pop()
        else:
            print("La lista esta vacia")
    
    def estaVacia(self):
        return len(self.lista) == 0
    
    def cantidad(self):
        return len(self.lista)
    
pila = Pila()

pila.agregar(2)
pila.agregar(4)
pila.agregar(6)

print(pila.lista)    

print(f"Se quito: {pila.quitar()}")

print(pila.lista)