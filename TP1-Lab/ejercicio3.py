class Contador:
    def __init__(self, cuenta=0):
        self.cuenta = cuenta

    def mostrar(self):
        print(f"La cuenta actual es de: {self.cuenta}")

    def incrementar(self, valor=1):
        if valor >= 0:
            self.cuenta += valor

    def decrementar(self, valor=1):
        if valor <= 0:
            self.cuenta -= valor

    def reiniciar(self):
        self.cuenta = 0

contador = Contador()
contador.mostrar()
contador.incrementar(100)
contador.decrementar()
contador.mostrar()