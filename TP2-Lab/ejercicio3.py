# Definir una clase Punto con atributos x e y. Luego definir una clase Linea con dos atributos:
# punto_a y punto_b a partir de la clase Punto.
# Agregar los siguientes métodos a la clase Linea:
# • __init__(a, b): Constructor que recibe los puntos a y b instanciados previamente.
# • __str__(): Retornar la posición de la linea en el siguiente formato ((xa,ya), (xb, yb))
# • distancia(): Calcular y retornar la distancia entre los puntos.
# • mover_derecha(cantidad): Mover linea a la derecha
# • mover_izquierda(cantidad): Mover linea a la izquierda
# • mover_arriba(cantidad): Mover linea hacia arriba
# • mover_abajo(cantidad): Mover linea hacia abajo
import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Linea:
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    def __str__(self):
        return f"({self.punto_a}, {self.punto_b})"
    
    def distancia(self):
        dx = self.punto_b.x - self.punto_a.x
        dy = self.punto_b.y - self.punto_a.y
        return math.sqrt(dx**2 + dy**2)
    
    def mover_derecha(self, cantidad):
        self.punto_a.x += cantidad
        self.punto_b.x += cantidad

    def mover_izquierda(self, cantidad):
        self.punto_a.x -= cantidad
        self.punto_b.x -= cantidad

    def mover_arriba(self, cantidad):
        self.punto_a.y += cantidad
        self.punto_b.y += cantidad

    def mover_abajo(self, cantidad):
        self.punto_a.y -= cantidad
        self.punto_b.y -= cantidad
    

punto1 = Punto(0, 0)
punto2 = Punto(3, 4)
linea = Linea(punto1, punto2)

print("Posición inicial de la línea:", linea)
print("Distancia entre los puntos:", linea.distancia())

linea.mover_derecha(2)
print("Línea movida a la derecha:", linea)

linea.mover_abajo(1)
print("Línea movida hacia abajo:", linea)