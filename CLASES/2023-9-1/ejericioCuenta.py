# Realizar una clase CuentaBancaria con los siguientes atributos y metodos:
# - Atributos: apellido del titular, nombre del titular, numero de cuenta, saldo de la cuenta.
# - Metodos:
# + constructor: con saldo inicial en cero.
# + __str__(): devolver todos los atributos.
# + saldo(): mostrar el saldo de la cuenta.
# + ingresar(monto): ingresar un monto a la cuenta (verificar monto positivo)
# + retirar(monto): retirar un monto a la cuenta (verificar monto positivo y saldo suficiente)
# --------------------------------------------
# Incorporar a la clase anterior una lista con el historial de ingresos
# y retiros de la cuenta. Agregar tambien el metodo verHistorial() que muestre los movimientos.

class CuentaBancaria:

    def __init__(self, nombre, apellido, numeroDeCuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.numeroDeCuenta = numeroDeCuenta
        self.saldoDeCuenta = 0
        self.historial = []

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero de Cuenta: {self.numeroDeCuenta}\nSaldo: {self.saldoDeCuenta}"
    
    def saldo(self):
        print(f"El saldo de la cuenta es: {self.saldoDeCuenta}")

    def ingresar(self, monto):
        if monto > 0:
            self.historial.append(f"+{monto}")
            self.saldoDeCuenta+=monto

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldoDeCuenta:
            self.historial.append(f"-{monto}")
            self.saldoDeCuenta-=monto

    def verHistorial(self):
        print(f"Historial de INGRESOS y RETIROS: {self.historial}")

cuentaUno = CuentaBancaria("Jorge", "Fuentes", 213)
cuentaUno.saldo();
cuentaUno.ingresar(500)
cuentaUno.ingresar(1500)
cuentaUno.retirar(600)
cuentaUno.ingresar(1500)
cuentaUno.retirar(600)
cuentaUno.retirar(100)
cuentaUno.verHistorial()
