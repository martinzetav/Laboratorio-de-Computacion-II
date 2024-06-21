class Persona:
    def __init__(self, apellido, nombre):
        self.apellido = apellido
        self.nombre = nombre
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    

# class Estudiante(Persona):
#     def __init__(self, apellido, nombre, nota):
#         Persona.__init__(self, apellido, nombre)
#         self.nota = nota

class Estudiante(Persona):
    def __init__(self, apellido, nombre, nota):
        super().__init__(apellido, nombre)
        self.nota = nota

    def __str__(self):
        return super().__str__ + f", {self.nota}"
        # return f"{self.apellido}, {self.nombre}, {self.nota}"

estudiante = Estudiante("Sanchez", "Pepe",8)
print(estudiante)

persona = Persona("Otra", "Persona")
print(persona)