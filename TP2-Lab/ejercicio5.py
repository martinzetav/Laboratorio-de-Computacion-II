class Cancion:
    def __init__(self, titulo, autor, duracion):
        self.titulo = titulo
        self.__autor = autor
        self.duracion = duracion

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.__autor}, Duracion: {self.duracion}"
    
class Album:
    def __init__(self, titulo):
        self.titulo = titulo
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def numero_canciones(self):
        return len(self.canciones)
    
    def eliminar_canciones(self, indice):
        self.canciones.pop(indice)

    def duracion_total(self):
        total_duracion = 0
        for cancion in self.canciones:
            total_duracion+= cancion.duracion
        return total_duracion
    
    def __str__(self):
        info = ""
        for i in range(len(self.canciones)):
            info += f"Pista: {i+1} => {self.canciones[i]}\n"
        return info
    
    
cancion0 = Cancion("Titulo 0", "Autor 0", 150)
cancion1 = Cancion("Titulo 1", "Autor 1", 250)
cancion2 = Cancion("Titulo 2", "Autor 2", 350)

print(cancion0.__autor)
# cancion0.__autor = ""

# album = Album("El album del siglo")
# album.agregar_cancion(cancion0)
# album.agregar_cancion(cancion1)
# album.agregar_cancion(cancion2)

# print(album.numero_canciones())
# print(album.canciones[1])
# print(album.duracion_total())
# print(album)