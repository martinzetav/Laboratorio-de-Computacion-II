class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def perimietro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro
    
    def esEquilatero(self):
        return self.ladoA == self.ladoB and self.ladoA == self.ladoC
        
    def esIsosceles(self):
        if self.ladoA == self.ladoB and self.ladoA != self.ladoC:
            return True
        elif self.ladoA == self.ladoC and self.ladoA != self.ladoB:
            return True
        elif self.ladoB == self.ladoC and self.ladoB != self.ladoA:
            return True
        else:
            return False
    
    def esEscaleno(self):
        return self.ladoA != self.ladoB and self.ladoB != self.ladoC and self.ladoC != self.ladoA
        
obj = Triangulo(3,3,3)

print(obj.esEquilatero())
print(obj.esIsosceles())
print(obj.esEscaleno())