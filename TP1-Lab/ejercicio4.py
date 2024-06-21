class Cafetera:

    def __init__(self, capacidadMaxima=1000, cantidadActual=0):
        self.capacidadMaxima = capacidadMaxima
        self.cantidadActual = cantidadActual

    def llenar(self):
        self.cantidadActual = self.capacidadMaxima

    def servir(self,cantidad):
        if cantidad > 0 and cantidad <= self.cantidadActual:
            self.cantidadActual-=cantidad
            return "Se sirvio " + str(cantidad) + " Cc"
        else:
            return "Cantidad INVALIDA"
      
    def vaciar(self):
        self.cantidadActual = 0
    
    def agregar(self,cantidad):
        if cantidad > 0 and (self.cantidadActual + cantidad) <= self.capacidadMaxima:
                self.cantidadActual+= cantidad
        else:
            print("cantidad NO VALIDA")
        
cafetera = Cafetera(1000,0)
print(cafetera.cantidadActual)
cafetera.agregar(500)
print(cafetera.cantidadActual)
cafetera.agregar(100)
print(cafetera.cantidadActual)