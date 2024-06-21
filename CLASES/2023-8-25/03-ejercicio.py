class Cuenta:
    def __init__(self, cuenta = 0):
        self.cuenta = cuenta

    def mostrar(self):
        print(self.cuenta)

    def incrementar(self, valor=1):
        self.cuenta += valor
    
    def decrementar(self, valor=1):
        self.cuenta -= valor


obj = Cuenta()

obj.mostrar()
obj.decrementar()
obj.mostrar()