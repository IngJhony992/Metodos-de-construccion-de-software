class NodoNario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = {}
        self.libros = []

class ArbolCategorias:
    def __init__(self):
        self.raiz = NodoNario("root")

    def agregar_categoria(self, ruta_categoria, isbn=None):
        partes = ruta_categoria.split('.')
        nodo_actual = self.raiz
        for parte in partes:
            if parte not in nodo_actual.hijos:
                nodo_actual.hijos[parte] = NodoNario(parte)
            nodo_actual = nodo_actual.hijos[parte]
        if isbn:
            nodo_actual.libros.append(isbn)

    def buscar_categoria(self, ruta_categoria):
        partes = ruta_categoria.split('.')
        nodo_actual = self.raiz
        for parte in partes:
            if parte not in nodo_actual.hijos:
                return None
            nodo_actual = nodo_actual.hijos[parte]
        return nodo_actual.libros
    