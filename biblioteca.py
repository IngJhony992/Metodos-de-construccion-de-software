from libro import Libro
from usuario import Usuario
from arboles import ArbolLibros, ArbolPrestamos
from arbol_nario import ArbolCategorias


class Biblioteca:
    def __init__(self):
        self.libros = []  # Lista para almacenar libros
        self.usuarios = {}  # Diccionario para almacenar usuarios (clave: ID)
        self.libros_recientes = []  # Lista para libros recientes (simula una pila)
        self.solicitudes_prestamo = []  # Lista para solicitudes de préstamo (simula una cola)
        self.arbol_libros = ArbolLibros()  # Nuevo: Árbol para búsquedas rápidas
        self.arbol_prestamos = ArbolPrestamos()  # Nuevo: Árbol AVL para préstamos
        self.arbol_categorias = ArbolCategorias() # Nuevo árbol para crear categorías

    def registrar_libro(self, titulo, autor, isbn):
        libro = Libro(titulo, autor, isbn)
        self.libros.append(libro)
        self.libros_recientes.append(libro)  # Simula una pila
        self.arbol_libros.insertar(isbn, libro)  # Insertar en el árbol ABB

    def buscar_libro(self, isbn):
        return self.arbol_libros.buscar(isbn) 

    def registrar_usuario(self, id, nombre):
        self.usuarios[id] = Usuario(id, nombre)

    def prestar_libro(self, isbn, usuario_id, fecha):
        libro = self.buscar_libro(isbn)
        usuario = self.usuarios.get(usuario_id)
        if libro and libro.disponible and usuario:
            libro.disponible = False
            usuario.agregar_libro_prestado(isbn)
            self.arbol_prestamos.insertar(fecha, {"usuario": usuario_id, "isbn": isbn})
            return True
        return False

    def devolver_libro(self, isbn, usuario_id):
        libro = self.buscar_libro(isbn)
        usuario = self.usuarios.get(usuario_id)
        if libro and not libro.disponible and usuario:
            libro.disponible = True
            usuario.devolver_libro(isbn)
            return True
        return False

    def agregar_libro_a_categoria(self, isbn, ruta_categoria):
        if not any(libro.isbn == isbn for libro in self.libros):
            raise ValueError("ISBN no registrado.")
        self.arbol_categorias.agregar_categoria(ruta_categoria, isbn)