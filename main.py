import tkinter as tk
from biblioteca import Biblioteca
from persistencia import cargar_datos, guardar_datos
from interfazTkinter import BibliotecaUI

if __name__ == "__main__":
    # Cargar datos al inicio
    arbol_libros, arbol_categorias = cargar_datos()
    biblioteca = Biblioteca()
    biblioteca.arbol_libros = arbol_libros
    biblioteca.arbol_categorias = arbol_categorias

    # Iniciar interfaz
    root = tk.Tk()
    app = BibliotecaUI(root, biblioteca)
    
    # Guardar al cerrar
    root.protocol("WM_DELETE_WINDOW", lambda: [
        guardar_datos(biblioteca),
        root.destroy()
    ])
    root.mainloop()