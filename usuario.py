class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []

    def agregar_libro_prestado(self, isbn):
        self.libros_prestados.append(isbn)

    def devolver_libro(self, isbn):
        if isbn in self.libros_prestados:
            self.libros_prestados.remove(isbn)

    def __str__(self):
        return (f"Usuario(id='{self.id}', nombre='{self.nombre}', "
                f"libros_prestados={self.libros_prestados})")