class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return (f"Libro(titulo='{self.titulo}', autor='{self.autor}', "
                f"isbn='{self.isbn}', disponible={self.disponible})")