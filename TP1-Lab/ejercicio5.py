class Persona:

    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
    
    def nombreCompleto(self):
        return f"Apellido y Nombre: {self.apellido} {self.nombre}"
    
    def esMayor(self):
        if self.edad >= 18:
            return f"Es MAYOR de edad porque tiene {self.edad} años"
        else:
            return f"Es MENOR de edad porque tiene {self.edad} años"

    def imc(self, peso, altura):
        imc = peso / (altura**2)
        return imc
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nAltura: {self.altura}\nPeso: {self.peso}"
    
martin = Persona("Martin", "Zalazar", 22, 1.73, 70)
print(martin.nombreCompleto())
print(martin.esMayor())
print(martin.imc(martin.peso, martin.altura))
print(martin.__str__())