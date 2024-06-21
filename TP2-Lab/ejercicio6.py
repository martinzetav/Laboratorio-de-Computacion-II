class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Paginas: {self.paginas}"
    
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def ordenar_lista_por_titulo(self):
        f = 0
        while f==0:
            f=1
            aux = ""
            for i in range(len(self.libros)-1):
                if self.libros[i].titulo > self.libros[i+1].titulo:
                    aux = self.libros[i]
                    self.libros[i] = self.libros[i+1]
                    self.libros[i+1] = aux
                    f = 0
        
        for libro in self.libros:
            print(libro)

    def ordenar_lista_por_autor(self):
        f = 0
        while f==0:
            f=1
            aux = ""
            for i in range(len(self.libros)-1):
                if self.libros[i].autor > self.libros[i+1].autor:
                    aux = self.libros[i]
                    self.libros[i] = self.libros[i+1]
                    self.libros[i+1] = aux
                    f = 0
        
        for libro in self.libros:
            print(libro)

    # def ordenar_lista_por_titulo(self):
    #     libros_titulo = sorted(self.libros, key= lambda libro: libro.titulo)
    #     for libro in libros_titulo:
    #         print(libro)
                
    # def ordenar_lista_por_autor(self):
    #     self.libros.sort(key= lambda libro: libro.autor)
        
    #     for libro in self.libros:
    #         print(libro)

    def numero_libros(self):
        return len(self.libros)
    
    def eliminar_libro(self, indice):
        self.libros.pop(indice)

    def __str__(self):
        info = ""
        for libro in self.libros:
            info += f"Libro: {libro}\n"
        return info

libro1 = Libro("Bob Esponja", "Patrick", 90)
libro2 = Libro("Piratas", "Federick", 120)
libro3 = Libro("Harry potter", "Mistou", 98)

biblio = Biblioteca()
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
biblio.agregar_libro(libro3)

# print(biblio)
# print("1-----------------------")
# biblio.ordenar_lista_por_titulo()
print("2---------------")
biblio.ordenar_lista_por_autor()