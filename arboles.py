# Árbol Binario de Búsqueda (ABB) para libros por ISBN
class NodoLibro:
    def __init__(self, isbn, libro):
        self.isbn = isbn
        self.libro = libro
        self.izquierda = None
        self.derecha = None

class ArbolLibros:
    def __init__(self):
        self.raiz = None

    def insertar(self, isbn, libro):
        self.raiz = self._insertar(self.raiz, isbn, libro)

    def _insertar(self, nodo, isbn, libro):
        if nodo is None:
            return NodoLibro(isbn, libro)
        if isbn < nodo.isbn:
            nodo.izquierda = self._insertar(nodo.izquierda, isbn, libro)
        else:
            nodo.derecha = self._insertar(nodo.derecha, isbn, libro)
        return nodo

    def buscar(self, isbn):
        return self._buscar(self.raiz, isbn)

    def _buscar(self, nodo, isbn):
        if nodo is None or nodo.isbn == isbn:
            return nodo.libro if nodo else None
        if isbn < nodo.isbn:
            return self._buscar(nodo.izquierda, isbn)
        return self._buscar(nodo.derecha, isbn)

# Árbol AVL para préstamos por fecha (simplificado)

class NodoAVL:
    def __init__(self, clave, dato):
        self.clave = clave  # Ej: fecha "2023-10-25"
        self.dato = dato    # Ej: objeto Prestamo
        self.izquierda = None
        self.derecha = None
        self.altura = 1     # Altura inicial del nodo

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _obtener_equilibrio(self, nodo):
        if not nodo:
            return 0
        return self._obtener_altura(nodo.izquierda) - self._obtener_altura(nodo.derecha)

    def _rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        # Rotación
        y.derecha = z
        z.izquierda = T3

        # Actualizar alturas
        z.altura = 1 + max(self._obtener_altura(z.izquierda), self._obtener_altura(z.derecha))
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))

        return y  # Nueva raíz

    def _rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        # Rotación
        y.izquierda = z
        z.derecha = T2

        # Actualizar alturas
        z.altura = 1 + max(self._obtener_altura(z.izquierda), self._obtener_altura(z.derecha))
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))

        return y  # Nueva raíz

    def insertar(self, clave, dato):
        self.raiz = self._insertar(self.raiz, clave, dato)

    def _insertar(self, nodo, clave, dato):
        # 1. Inserción estándar en ABB
        if not nodo:
            return NodoAVL(clave, dato)
        if clave < nodo.clave:
            nodo.izquierda = self._insertar(nodo.izquierda, clave, dato)
        else:
            nodo.derecha = self._insertar(nodo.derecha, clave, dato)

        # 2. Actualizar altura del nodo actual
        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierda),
                              self._obtener_altura(nodo.derecha))

        # 3. Calcular factor de equilibrio
        equilibrio = self._obtener_equilibrio(nodo)

        # 4. Rebalancear si es necesario
        # Caso izquierda-izquierda
        if equilibrio > 1 and clave < nodo.izquierda.clave:
            return self._rotar_derecha(nodo)
        # Caso derecha-derecha
        if equilibrio < -1 and clave > nodo.derecha.clave:
            return self._rotar_izquierda(nodo)
        # Caso izquierda-derecha
        if equilibrio > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        # Caso derecha-izquierda
        if equilibrio < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def buscar(self, clave):
        return self._buscar(self.raiz, clave)

    def _buscar(self, nodo, clave):
        if not nodo or nodo.clave == clave:
            return nodo.dato if nodo else None
        if clave < nodo.clave:
            return self._buscar(nodo.izquierda, clave)
        return self._buscar(nodo.derecha, clave)
    
class NodoPrestamo:
    def __init__(self, fecha, prestamo):
        self.fecha = fecha
        self.prestamo = prestamo
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolPrestamos:
    def __init__(self):
        self.raiz = None

    def insertar(self, fecha, prestamo):
        self.raiz = self._insertar(self.raiz, fecha, prestamo)

    def _insertar(self, nodo, fecha, prestamo):
        if nodo is None:
            return NodoAVL(fecha, prestamo)
        if fecha < nodo.fecha:
            nodo.izquierda = self._insertar(nodo.izquierda, fecha, prestamo)
        else:
            nodo.derecha = self._insertar(nodo.derecha, fecha, prestamo)
        
        return nodo