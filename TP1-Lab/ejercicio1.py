import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio**2)
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
circulo = Circulo(20)
print(f"El area del circulo es {circulo.area():.2f}")
print(f"El perimetro del circulo es {circulo.perimetro():.2f}")