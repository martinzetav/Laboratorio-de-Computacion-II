# 7- Se requiere desarrollar un programa que modele un sistema de peaje. Las estaciones de peaje
# tienen un nombre, departamento en que están ubicadas y una lista de vehículos que pasaron.
# Los vehículos que llegan a un peaje tienen una placa (tipo String). El peaje cobra diferentes
# valores de peaje según el tipo de vehículo. Si es un auto, el valor del peaje es de $300. Si es una
# moto, $150. Si es un camión, el valor del peaje depende del número de ejes, se cobra $500 por cada
# eje.
# Se requiere que la estación de peaje calcule el valor del peaje de cada vehículo que llegue y
# el total de peajes recolectados. Así, al finalizar, el sistema debe imprimir en pantalla un listado con
# los vehículos que llegaron al peaje y el total acumulado.
# Atributos y métodos de las clases:
# • Vehiculo:
# ◦ Atributos: placa
# • Moto: Hereda de vehiculo
# ◦ Atributos: valor_peaje
# ◦ Métodos: __init__(placa)
# • Auto: Hereda de vehiculo:
# ◦ Atributos: valor_peaje
# ◦ Métodos: __init__(placa)
# • Camion: Hereda de vehiculo
# ◦ Atributos: valor_peaje, cantidad_ejes
# ◦ Métodos: __init__(placa, cantidad_ejes)
# • Peaje:
# ◦ Atributos: nombre, departamento, vehiculos
# ◦ Métodos: agregar_vehiculo(), calcular_total_peaje(), cantidad_vehiculos()

class Vehiculo:
    def __init__(self, placa, valor_peaje):
        self.placa = placa
        self.valor_peaje = valor_peaje


class Moto(Vehiculo):
    def __init__(self, placa):
        super().__init__(placa, 150)


class Auto(Vehiculo):
    def __init__(self, placa):
        super().__init__(placa, 300)


class Camion(Vehiculo):
    def __init__(self, placa, cantidad_ejes):
        super().__init__(placa, cantidad_ejes * 500)
        self.cantidad_ejes = cantidad_ejes


class Peaje:
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        self.vehiculos = []
    
    def agregar_vehiculos(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def calcular_total_peaje(self):
        total = 0
        for vehiculo in self.vehiculos:
            total+= vehiculo.valor_peaje
        return total

    def cantidad_vehiculos(self):
        print(f"Hay {len(self.vehiculos)} vehiculos")

    
