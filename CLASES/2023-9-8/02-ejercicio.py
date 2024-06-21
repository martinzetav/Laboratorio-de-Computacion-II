# Clase Inmueble:
# Atributos:
# - identificador inmobiliario (numero)
# - cantidadHabitaciones (numero)
# - area (numero) en metros cuadrados
# - direccion (texto)
# - precioVenta (numero)
# Metodos:
# + calcularPrecio(valorArea): calcular y devolver precioVenta = area * valorArea
# + __str__(): devolver todos los atributos.

class Inmueble:
    def __init__(self, identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta):
        self.identificador_inmobiliario = identificador_inmobiliario
        self.cantidad_habitaciones = cantidad_habitaciones
        self.area = area
        self.direccion = direccion
        self.precio_venta = precio_venta

    def calcular_precio(self, valor_area):
        return f"{(self.area * valor_area):.2f}"
    
    def __str__(self):
        return (
            f"id inmobiliario: {self.identificador_inmobiliario}, "
            f"habitaciones: {self.cantidad_habitaciones}, "
            f"area: {self.area}m2, "
            f"direccion: {self.direccion}, "
            f"precio: ${self.precio_venta}"
        )

inmueble_uno = Inmueble(238, 3, 15.8, "Calle Urquiza", 15000)
print(inmueble_uno.calcular_precio(3000))
print(inmueble_uno)
    

# Clase Casa: hereda de Inmueble:
# Atributos:
# - cantidadPisos (numero)
# Metodos:
# + __str__(): devolver todos los atributos.

class Casa(Inmueble):
    def __init__(self, identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta, cantidad_pisos):
        super().__init__(identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta)
        self.cantidad_pisos = cantidad_pisos
    
    def __str__(self):
        return super().__str__() + f", pisos: {self.cantidad_pisos}"
    
casa_uno = Casa(501, 5, 12.5, "Calle Balmaceda", 40000, 2)
print(casa_uno)
    
# Clase Departamento, hereda de Inmueble:
# Atributos:
# - numeroPiso (numero)
# Metodos:
# + __str__(): devolver todos los atributos.

class Departamento(Inmueble):
    def __init__(self, identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta, numero_piso):
        super().__init__(identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta)
        self.numero_piso = numero_piso

    def __str__(self):
        return super().__str__() + f", numero de piso: {self.numero_piso}"
    
departamento_uno = Departamento(652, 3, 11.3, "Calle Sismondi", 35000, 7)
print(departamento_uno)
    
# Clase CasaRural, hereda de Casa:
# Atributos:
# - distancia (numero) a la municipalidad mas cercana
# - altitud (numero)
# Metodos:
# + __str__(): devolver todos los atributos.

class CasaRural(Casa):
    def __init__(self, identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta, cantidad_pisos, distancia_municipalidad, altitud):
        super().__init__(identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta, cantidad_pisos)
        self.distancia_municipalidad = distancia_municipalidad
        self.altitud = altitud

    def __str__(self):
        return super().__str__() + f", distancia mas cercana a municipalidad: {self.distancia_municipalidad}, altitud: {self.altitud}"
    
casa_rural_uno = CasaRural(720, 3, 12.3, "Calle Ramon Navarro", 80000, 2, 200, 13)
print(casa_rural_uno)
    
# Clase CasaUrbana, hereda de Casa:
# Atributos:
# - tienePileta (boolean)
# Metodos:
# + __str__(): devolver todos los atributos.

class CasaUrbana(Casa):
    def __init__(self, identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta, cantidad_pisos, tiene_pileta):
        super().__init__(identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta, cantidad_pisos)
        self.tiene_pileta = tiene_pileta
    
    def __str__(self):
        return super().__str__() + f", tiene pileta: {self.tiene_pileta}"
    
casa_urbana_uno = CasaUrbana(429, 4, 21.9, "Calle Manuel Belgrano", 102000, 7, True)
print(casa_urbana_uno)
    
# Clase DepartamentoFamiliar, hereda de Departamento:
# atributos:
# - cantidadFamiliares (numero)
# Metodos:
# + __str__(): devolver todos los atributos.

class DepartamentoFamiliar(Departamento):
    def __init__(self, identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta, numero_piso, cantidad_familiares):
        super().__init__(identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta, numero_piso)
        self.cantidad_familiares = cantidad_familiares

    def __str__(self):
        return super().__str__() + f", {self.cantidad_habitaciones}"
    
depa_familiar_uno = DepartamentoFamiliar(832, 4, 102.3, "Calle Grimberg", 159000, 8, 5)
print(depa_familiar_uno)
    
# Clase DepartamentoEstudio, hereda de Departamento
# atributos:
# - cantidadEmpleados (boolean)
# Metodos:
# + __str__(): devolver todos los atributos.

class DepartamentoEstudio(Departamento):
    def __init__(self, identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta, numero_piso, cantidad_empleados):
        super().__init__(identificador_inmobiliario, cantidad_habitaciones, area, direccion, precio_venta, numero_piso)
        self.cantidad_empleados = cantidad_empleados

    def __str__(self):
        return super().__str__() + f", empleados: {self.cantidad_empleados}"

departamento_estudio_uno = DepartamentoEstudio(2103, 6, 200, "Calle Baltazar", 175000, 8, 3)
print(departamento_estudio_uno)
