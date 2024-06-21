class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    
    def esEquilatero(self):
        return self.ladoA == self.ladoB and self.ladoA == self.ladoC
    
    def esIsosceles(self):
        if self.ladoA == self.ladoB and self.ladoA != self.ladoC:
            return True
        elif self.ladoA == self.ladoC and self.ladoA != self.ladoB:
            return True
        elif self.ladoC == self.ladoB and self.ladoC != self.ladoA:
            return True
        else:
            return False
    
    def esEscaleno(self):
        return self.ladoA != self.ladoB and self.ladoA != self.ladoC and self.ladoB != self.ladoC
    
triangulo = Triangulo(20,20,21)
print(triangulo.esEquilatero())
print(triangulo.esIsosceles())
print(triangulo.esEscaleno())