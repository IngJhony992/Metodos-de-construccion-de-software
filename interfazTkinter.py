from tkinter import *
import tkinter as tk
from tkinter import messagebox
from biblioteca import Biblioteca
import datetime

class BibliotecaUI:
    def __init__(self, root, biblioteca=None):
        # Crear un frame principal para organizar verticalmente

        self.root = root
        self.root.title("Sistema de gestión de biblioteca")
        self.biblioteca = biblioteca
        frame_principal = tk.Frame(root)
        frame_principal.pack(pady=20)

        # Título arriba de todo
        self.label_titulo = tk.Label(frame_principal, text="Sistema de Gestión de Biblioteca - Jhonatan Becerra", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # Botones debajo del título
        self.btn_busqueda_avanzada = tk.Button(frame_principal, text="Búsqueda Avanzada", command=self.menu_busqueda_avanzada)
        self.btn_busqueda_avanzada.pack(pady=5)

        self.btn_registrar_libro = tk.Button(frame_principal, text="Registrar Libro", command=self.registrar_libro)
        self.btn_registrar_libro.pack(pady=5)

        self.btn_buscar_libro = tk.Button(frame_principal, text="Buscar Libro", command=self.buscar_libro)
        self.btn_buscar_libro.pack(pady=5)

        self.btn_registrar_usuario = tk.Button(frame_principal, text="Registrar Usuario", command=self.registrar_usuario)
        self.btn_registrar_usuario.pack(pady=5)

        self.btn_prestar_libro = tk.Button(frame_principal, text="Prestar Libro", command=self.prestar_libro)
        self.btn_prestar_libro.pack(pady=5)

        self.btn_devolver_libro = tk.Button(frame_principal, text="Devolver Libro", command=self.devolver_libro)
        self.btn_devolver_libro.pack(pady=5)

        tk.Button(frame_principal, text="Gestionar Categorías", command=self.menu_categorias).pack(pady=5)

    def menu_busqueda_avanzada(self):
        """Ventana para búsquedas avanzadas usando árboles."""
        ventana = tk.Toplevel(self.root)
        ventana.title("Búsqueda Avanzada")
        
        tk.Label(ventana, text="Seleccione el tipo de búsqueda:").pack(pady=10)
        
        # Botones para diferentes tipos de búsqueda
        btn_buscar_isbn = tk.Button(
            ventana, 
            text="Buscar por ISBN (Árbol ABB)", 
            command=self.buscar_por_isbn
        )
        btn_buscar_isbn.pack(pady=5)
        
        btn_buscar_categoria = tk.Button(
            ventana, 
            text="Buscar por Categoría (Árbol N-ario)", 
            command=self.buscar_por_categoria
        )
        btn_buscar_categoria.pack(pady=5)

    def buscar_por_isbn(self):
        """Búsqueda en el árbol binario por ISBN."""
        ventana = tk.Toplevel(self.root)
        ventana.title("Buscar por ISBN")
        
        tk.Label(ventana, text="Ingrese ISBN:").pack(pady=10)
        entry_isbn = tk.Entry(ventana)
        entry_isbn.pack(pady=5)
        
        def buscar():
            isbn = entry_isbn.get()
            if self.biblioteca:
                libro = self.biblioteca.arbol_libros.buscar(isbn)
                if libro:
                    messagebox.showinfo("Resultado", f"Libro encontrado:\n{libro}")
                else:
                    messagebox.showerror("Error", "Libro no encontrado")
        
        tk.Button(ventana, text="Buscar", command=buscar).pack(pady=10)

    def buscar_por_categoria(self):
        """Búsqueda en el árbol n-ario por categoría."""
        ventana = tk.Toplevel(self.root)
        ventana.title("Buscar por Categoría")
        
        tk.Label(ventana, text="Ingrese categoría (ej: Ciencia.Física):").pack(pady=10)
        entry_categoria = tk.Entry(ventana)
        entry_categoria.pack(pady=5)
        
        def buscar():
            categoria = entry_categoria.get()
            if self.biblioteca:
                libros = self.biblioteca.arbol_categorias.buscar_categoria(categoria)
                if libros:
                    messagebox.showinfo("Resultado", f"Libros en {categoria}:\n{', '.join(libros)}")
                else:
                    messagebox.showerror("Error", "Categoría no encontrada")
        
        tk.Button(ventana, text="Buscar", command=buscar).pack(pady=10)
    
    def registrar_libro(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar Libro")

        tk.Label(ventana, text="Título:").grid(row=0, column=0, padx=10, pady=5)
        entry_titulo = tk.Entry(ventana)
        entry_titulo.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Autor:").grid(row=1, column=0, padx=10, pady=5)
        entry_autor = tk.Entry(ventana)
        entry_autor.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(ventana, text="ISBN:").grid(row=2, column=0, padx=10, pady=5)
        entry_isbn = tk.Entry(ventana)
        entry_isbn.grid(row=2, column=1, padx=10, pady=5)

        def guardar_libro():
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            isbn = entry_isbn.get()
            if titulo and autor and isbn:
                self.biblioteca.registrar_libro(titulo, autor, isbn)
                messagebox.showinfo("Éxito", "Libro registrado correctamente.")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")

        tk.Button(ventana, text="Guardar", command=guardar_libro).grid(row=3, column=1, pady=10)

    def buscar_libro(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Buscar Libro")

        tk.Label(ventana, text="ISBN:").grid(row=0, column=0, padx=10, pady=5)
        entry_isbn = tk.Entry(ventana)
        entry_isbn.grid(row=0, column=1, padx=10, pady=5)

        def buscar():
            isbn = entry_isbn.get()
            libro = self.biblioteca.buscar_libro(isbn)
            if libro:
                messagebox.showinfo("Resultado", f"Libro encontrado:\n{libro}")
            else:
                messagebox.showerror("Error", "Libro no encontrado.")

        tk.Button(ventana, text="Buscar", command=buscar).grid(row=1, column=1, pady=10)

    def registrar_usuario(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar Usuario")

        tk.Label(ventana, text="ID:").grid(row=0, column=0, padx=10, pady=5)
        entry_id = tk.Entry(ventana)
        entry_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.grid(row=1, column=1, padx=10, pady=5)

        def guardar_usuario():
            id = entry_id.get()
            nombre = entry_nombre.get()
            if id and nombre:
                self.biblioteca.registrar_usuario(id, nombre)
                messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")

        tk.Button(ventana, text="Guardar", command=guardar_usuario).grid(row=2, column=1, pady=10)

    def prestar_libro(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Prestar Libro")
        ventana.geometry("400x250")

        contenedor = tk.Frame(ventana, padx=20, pady=20)
        contenedor.pack(expand=True, fill="both")

        tk.Label(contenedor, text="ISBN:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        entry_isbn = tk.Entry(contenedor)
        entry_isbn.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(contenedor, text="ID Usuario:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_usuario_id = tk.Entry(contenedor)
        entry_usuario_id.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(contenedor, text="Fecha (AAAA-MM-DD):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_fecha = tk.Entry(contenedor)
        entry_fecha.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
        entry_fecha.grid(row=2, column=1, padx=10, pady=5)

        def prestar():
            isbn = entry_isbn.get().strip()
            usuario_id = entry_usuario_id.get().strip()
            fecha = entry_fecha.get().strip()

            try:
                datetime.datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha inválido. Use AAAA-MM-DD")
                return

            if self.biblioteca and hasattr(self.biblioteca, "prestar_libro"):
                if self.biblioteca.prestar_libro(isbn, usuario_id, fecha):
                    messagebox.showinfo("Éxito", f"Libro prestado correctamente el {fecha}")
                    ventana.destroy()
                else:
                    messagebox.showerror("Error", "No se pudo prestar el libro. Verifique:\n"
                                              "- Que el libro exista y esté disponible\n"
                                              "- Que el usuario esté registrado")
            else:
                messagebox.showerror("Error", "Sistema de biblioteca no disponible")

        tk.Button(contenedor, text="Prestar", command=prestar).grid(row=3, column=0, columnspan=2, pady=15)

    def devolver_libro(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Devolver Libro")

        tk.Label(ventana, text="ISBN:").grid(row=0, column=0, padx=10, pady=5)
        entry_isbn = tk.Entry(ventana)
        entry_isbn.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="ID Usuario:").grid(row=1, column=0, padx=10, pady=5)
        entry_usuario_id = tk.Entry(ventana)
        entry_usuario_id.grid(row=1, column=1, padx=10, pady=5)

        def devolver():
            isbn = entry_isbn.get()
            usuario_id = entry_usuario_id.get()
            if self.biblioteca.devolver_libro(isbn, usuario_id):
                messagebox.showinfo("Éxito", "Libro devuelto correctamente.")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo devolver el libro.")

        tk.Button(ventana, text="Devolver", command=devolver).grid(row=2, column=1, pady=10)

    def menu_categorias(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Categorías")
        
        tk.Label(ventana, text="ISBN:").grid(row=0, column=0)
        entry_isbn = tk.Entry(ventana)
        entry_isbn.grid(row=0, column=1)
        
        tk.Label(ventana, text="Categoría (ej: Ciencia.Física):").grid(row=1, column=0)
        entry_categoria = tk.Entry(ventana)
        entry_categoria.grid(row=1, column=1)
        
        def guardar():
            isbn = entry_isbn.get()
            categoria = entry_categoria.get()
            try:
                self.biblioteca.agregar_libro_a_categoria(isbn, categoria)
                messagebox.showinfo("Éxito", "Libro añadido a la categoría.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        tk.Button(ventana, text="Guardar", command=guardar).grid(row=2, column=1)