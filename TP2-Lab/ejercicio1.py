# Realizar una clase CuentaBancaria con los siguientes atributos y metodos:
# ATRIBUTOS: nombre y apellido del titular, saldo de la cuenta.
# METODOS:
# + constructor:
# + __str__(): devolver todos los atributos.
# + saldo(): mostrar el saldo de la cuenta.
# + ingresar(monto): ingresar un monto a la cuenta(verificar monto positivo)
# + retirar(monto): retirar un monto de la cuenta no superior al saldo(verificar monto positivo)

class CuentaBancaria:

    def __init__(self, nombre, apellido_titular, saldo_cuenta):
        self.nombre = nombre
        self.apellido_titular = apellido_titular
        self.saldo_cuenta = saldo_cuenta

    def __str__(self):
        return f"{self.nombre}, {self.apellido_titular}, saldo: {self.saldo_cuenta}"
    
    def saldo(self):
        print(f"Saldo de la cuenta: {self.saldo_cuenta}")
    
    def ingresar(self, monto):
        if monto >= 0:
            self.saldo_cuenta += monto
        else:
            print("Error no se puede ingresar un numero negativo")
    
    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo_cuenta:
            self.saldo_cuenta -= monto
        else:
            print("No es posible retirar debido a que el monto supera al saldo de la cuenta")


# Las clases CuentaAhorro y CuentaCorriente heredan los atributos y metodos de CuentaBancaria.

# La clase CuentaAhorro tiene ademas un atributo para determinar si la cuenta esta inactiva si el saldo es menor a 10000
# y activa si es mayor. Tiene los siguientes metodos:
# + ingresar(monto): se puede ingresar dinero invocando al metodo heredado cuando esta activa la cuenta.
# + retirar(monto): se puede retirar si la cuenta esta activa. Debe invocar al metodo heredado.
# + __str__(): devolver todos los atributos incluyendo si esta activa o no.

class CuentaAhorro(CuentaBancaria):

    def __init__(self, nombre, apellido_titular, saldo_cuenta):
        super().__init__(nombre, apellido_titular, saldo_cuenta)
        self.estado_cuenta = ""
        if self.saldo_cuenta >= 10000:
            self.estado_cuenta = "Cuenta Activa"
        else:
            self.estado_cuenta = "Cuenta Inactiva"

    def ingresar(self, monto):
        if self.estado_cuenta == "Cuenta Activa":
            super().ingresar(monto)
        else:
            print("No se puede ingresar dinero porque la cuenta esta INACTIVA")

    def retirar(self, monto):
        if self.estado_cuenta == "Cuenta Activa":
            super().retirar(monto)
            if self.saldo_cuenta < 10000:
                self.estado_cuenta = "Cuenta Inactiva"

    def __str__(self):
        return super().__str__() + f", estado: {self.estado_cuenta}"

cuenta = CuentaAhorro("Jerome", "ZV", 10000)   
print(cuenta)
cuenta.retirar(11000)
print(cuenta)

    
# La clase CuentaCorriente tiene ademas un atributo de sobregiro inicializada en cero. Ademas los siguientes metodos:
# + ingresar(monto): se puede ingresar, pero si hay sobregiro se reduce la cantidad agregada.
# + retirar(monto): se puede retirar un monto superior al saldo, el dinero que se debe queda como sobregiro.
# Invocar al metodo heredado.
# + __str__(): devolver todos los atributos incluyendo el sobregiro. Invocar el metodo heredado.

class CuentaCorriente(CuentaBancaria):

    def __init__(self, nombre, apellido_titular, saldo_cuenta):
        super().__init__(nombre, apellido_titular, saldo_cuenta)
        self.sobregiro = 0

    def ingresar(self, monto):
        monto_real = 0
        if self.sobregiro > 0 and monto >= self.sobregiro:
            monto_real = monto - self.sobregiro
            self.sobregiro = 0
        elif monto > 0:
            monto_real = monto - self.sobregiro
            self.sobregiro -= monto
            if monto_real < 0:
                monto_real = 0

        super().ingresar(monto_real)

    # def ingresar(self, monto):
    #     monto_real = 0
    #     if self.sobregiro < 0 and monto >= self.sobregiro:
    #         monto_real = self.sobregiro + monto
    #         self.sobregiro = 0
    #     elif self.sobregiro < 0:
    #         monto_real = self.sobregiro + monto
    #         self.sobregiro+= monto_real
    #     else:
    #         monto_real+=monto
    #     super().ingresar(monto_real)

    def retirar(self, monto):
        if monto > 0 and monto > self.saldo_cuenta:
            self.sobregiro = abs(self.saldo_cuenta - monto)
            self.saldo_cuenta = 0
        else:
            super().retirar(monto)

    # def retirar(self, monto):
    #     if monto > self.saldo_cuenta:
    #         self.sobregiro = (self.saldo_cuenta - monto)
    #         self.saldo_cuenta = 0
    #     else:
    #         self.saldo_cuenta-=monto

    def __str__(self):
        return super().__str__() + f", sobregiro: {self.sobregiro}"

##OBJETO CUENTA CORRIENTE
# cuentaCorrienta = CuentaCorriente("Facundo", "Lucero", 100)
# cuentaCorrienta.saldo()
# cuentaCorrienta.retirar(400)
# print(cuentaCorrienta)
# cuentaCorrienta.ingresar(100)
# print(cuentaCorrienta)


# #OBJETO CUENTA AHORRO
# cuentaAhorro = CuentaAhorro("Martin", "Zalazar", 10000)
# # cuentaAhorro.ingresar(500)
# cuentaAhorro.retirar(11000)
# cuentaAhorro.saldo()