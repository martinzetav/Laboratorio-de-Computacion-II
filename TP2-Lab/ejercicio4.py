# Crea las siguientes clases:
# Motor:
#  + Atributos: nivel_aceite, temperatura, encendido
#  + Metodos: arrancar, detener, str()
# Rueda:
#  + Atributos: rodado, presion
#  + Metodos: inflar, desinflar, str()
# Ventana:
#  + Atributos: polarizado
#  + Metodos: abrir, cerrar, str()
# Puerta: (con una ventana)
# + Atributos: color
# + Metodos: abrir, cerrar, str()
# Auto:
#  + Atributos: motor, 4 ruedas, dos puertas
#  + metodos: str() (con todos los atributos)

class Motor:
    def __init__(self, nivel_aceite, temperatura, encendido=False):
        self.nivel_aceite = nivel_aceite
        self.temperatura = temperatura
        self.encendido = encendido

    def arrancar(self):
        self.encendido = True

    def detener(self):
        self.encendido = False

    def __str__(self):
        return f"Aceite: {self.nivel_aceite}, temperatura: {self.temperatura}, encendido: {self.encendido}"
    
class Rueda:
    def __init__(self, rodado, presion=0):
        self.rodado = rodado
        self.presion = presion

    def inflar(self, presion):
        if presion > 0:
            self.presion += presion

    def desinflar(self, presion):
        if presion > 0 and presion < self.presion:
            self.presion -= presion
        elif presion > 0 and presion > self.presion:
            self.presion = 0

    def __str__(self):
        return f"Rodado: {self.rodado}, presion: {self.presion}"

class Ventana:
    def __init__(self, polarizado):
        self.polarizado = polarizado

    def abrir(self):
        print("Ventana abierta")

    def cerrar(self):
        print("Ventana cerrada")

    def __str__(self):
        return f"Polarizado: {self.polarizado}"
    

class Puerta:
    def __init__(self, color, ventana):
        self.color = color
        self.ventana = ventana

    def abrir(self):
        print("Puerta abierta")

    def cerrar(self):
        print("Puerta Cerrada")

class Auto:
    def __init__(self, motor, rueda1, rueda2, rueda3, rueda4, puerta1, puerta2):
        self.motor = motor
        self.rueda1 = rueda1
        self.rueda2 = rueda2
        self.rueda3 = rueda3
        self.rueda4 = rueda4
        self.puerta1 = puerta1
        self.puerta2 = puerta2

    def __str__(self):
        return f"Motor: {self.motor}, ruedas: {self.rueda1}, {self.rueda2}, {self.rueda3}, {self.rueda4}, puertas: {self.puerta1}, {self.puerta2}"

motor = Motor(3, 30)
rueda1 = Rueda(12,90)
rueda2 = Rueda(12,90)
rueda3 = Rueda(12,90)
rueda4 = Rueda(12,90)
ventana1 = Ventana(True)
ventana2 = Ventana(True)
puerta1 = Puerta("Rojo", ventana1)
puerta2 = Puerta("Rojo", ventana2)

auto = Auto(motor, rueda1, rueda2, rueda3, rueda4, puerta1, puerta2)

