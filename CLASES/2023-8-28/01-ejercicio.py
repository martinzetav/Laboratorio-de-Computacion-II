# Desarrollar una clase Cafetera con:
# Atributos:
# capacidadMaxima: Cantidad maxima de cafe que puede contener la cafetera en CC
# cantidadActual: cantidad actual de cafe que hay en la cafetera en CC
# Metodos:
# Constructor: considerar por defecto capacidad maxima de 1000 CC y cantidad actual en cero.
# llenar(): llena cafetera a la capacidad maxima.
# servir(cantidad): sirve una cantidad de cafe (verificar que cantidad sea positivo y no servir mas del actual)
# vaciar(): vaciar cafetera
# agregar(cantidad): añade una cantidad de cafe (verificar que cantidad sea positivo y no supere el maximo)

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
        if cantidad > 0:
            cantidadTotal = self.cantidadActual + cantidad
            if cantidadTotal < self.capacidadMaxima:
                self.cantidadActual+= cantidad
                return "La cafetera se lleno correctamente"
            else:
                return "La cantidad que se quiere servir supera la capacidad maxima de la cafetera que es de " + str(self.capacidadMaxima)
        else:
            return "No se puede llenar la cafetera con una cantidad negativa"
        
cafetera = Cafetera(1000,0)
print(cafetera.cantidadActual)
print(cafetera.agregar(500))
print(cafetera.cantidadActual)
print(cafetera.agregar(-5000))
print(cafetera.cantidadActual)

