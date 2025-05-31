import pickle
import json
from arbol_nario import ArbolCategorias, NodoNario
from arboles import ArbolLibros

def guardar_datos(biblioteca):
    try:
        # Guardar árbol ABB
        with open('arbol_libros.pkl', 'wb') as f:
            pickle.dump(biblioteca.arbol_libros, f)
        
        # Guardar árbol n-ario (como JSON)
        def _to_dict(nodo):
            return {
                "libros": nodo.libros,
                "hijos": {nombre: _to_dict(hijo) for nombre, hijo in nodo.hijos.items()}
            }
        with open('categorias.json', 'w') as f:
            json.dump(_to_dict(biblioteca.arbol_categorias.raiz), f, indent=2)
    except Exception as e:
        print(f"Error al guardar: {e}")

def cargar_datos():
    try:
        # Cargar árbol ABB
        with open('arbol_libros.pkl', 'rb') as f:
            arbol_libros = pickle.load(f)
        
        # Cargar árbol n-ario
        def _from_dict(data, nodo):
            nodo.libros = data.get("libros", [])
            for nombre, hijo_data in data.get("hijos", {}).items():
                nodo.hijos[nombre] = NodoNario(nombre)
                _from_dict(hijo_data, nodo.hijos[nombre])
        
        arbol_categorias = ArbolCategorias()
        with open('categorias.json', 'r') as f:
            data = json.load(f)
            _from_dict(data, arbol_categorias.raiz)
        
        return arbol_libros, arbol_categorias
    except FileNotFoundError:
        return ArbolLibros(), ArbolCategorias()