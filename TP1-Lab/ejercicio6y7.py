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