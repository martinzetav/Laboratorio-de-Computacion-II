import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def perimetro(self):
        PI = math.pi
        return 2 * PI * self.radio
    
    def area(self):
        PI = math.pi
        return PI * (self.radio**2)
    
obj = Circulo(10)

print("Perimetro:" , obj.perimetro())
print("Area:" , obj.area())