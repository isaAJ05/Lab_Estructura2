from typing import Any, List, Optional, Tuple
import graphviz
import tempfile
from tkinter import Image
from PIL import Image
import os
class Stack:
    def __init__(self) -> None:
        self.stack: List[Any] = []

    def add(self, elem: Any) -> None:
        self.stack.append(elem)

    def remove(self) -> Any:
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

class Cola:
    def __init__(self) -> None:
        self.cola: List[Any] = []
    def add(self, elem: Any) -> None:
        self.cola.append(elem)
    def remove(self) -> Any:
        return self.cola.pop(0)
    def is_empty(self) -> bool:
        return len(self.cola) == 0

class Nodo:

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: Optional['Nodo'] = None
        self.right: Optional['Nodo'] = None
        self.factor_balance:int = 0
        self.type = self.determine_type(str(self.data)) # Agrega el atributo 'type'
        self.size: int = 0
        self.typeImage: str = self.determine_typeImage(str(self.data))

    def __str__(self) -> str:
        return str(self.data)
    def determine_type(self, data: str) -> str:
        # Define las reglas para determinar el tipo según el nombre del archivo
        if "bike" in data:
            return "bike"
        elif "carsgraz" in data:
            return "cars"
        elif "cat" in data:
            return "cats"
        elif "dog" in data:
            return "dogs"
        elif str(data).startswith("0"):
            return "flowers"
        elif "horse" in data:
            return "horses"
        elif "rider" in data:
            return "human"
        else:
            return "unknown"  # Si no se encuentra una clasificación específica
    def determine_typeImage(self, data: str) -> str:
        # Define las reglas para determinar el tipo según el nombre del archivo
        if "bike" in data:
            return ".bmp"
        elif "carsgraz" in data:
            return ".bmp"
        elif "cat" in data:
            return ".jpg"
        elif "dog" in data:
            return ".jpg"
        elif str(data).startswith("0"):
            return ".png"
        elif "horse" in data:
            return ".jpg"
        elif "rider" in data:
            return ".jpg"
        else:
            return "unknown"  # Si no se encuentra una clasificación específica

    def calcular_factor_balance(self) -> None: #Calcula el factor de balance
        if self.left is not None:
            self.factor_balance = self.left.get_niveles()
        else:
            self.factor_balance = 0
        if self.right is not None:
            self.factor_balance -= self.right.get_niveles()
        else:
            self.factor_balance -= 0


    def get_niveles(self) -> int: #Altura del nodo
        if self.left is not None and self.right is not None:
            return 1 + max(self.left.get_niveles(), self.right.get_niveles())
        elif self.left is not None:
            return 1 + self.left.get_niveles()
        elif self.right is not None:
            return 1 + self.right.get_niveles()
        else:
            return 1

class Tree:
    # El arbol debe insertar, eliminar, buscar, buscar todos los nodos de cierta categoria,buscar segun size
    # El arbol debe tener un metodo para balancear
    # recorrido por niveles recursivo
    # Obtener el nivel del nodo.
    # b. Obtener el factor de balanceo (equilibrio) del nodo.
    # c. Encontrar el padre del nodo.
    # d. Encontrar el abuelo del nodo.
    # e. Encontrar el tío del nodo.
    def __init__(self, root: "Nodo"=None) -> None: #Inicializa el arbol
        self.root = root

    def search(self, elem: Any) -> Tuple[Optional["Nodo"], Optional["Nodo"]]:
        p, pad = self.root, None
        while p is not None:
            if elem == p.data:
                return p, pad
            elif elem < p.data:
                pad = p
                p = p.left
            else:
                pad = p
                p = p.right
        return p, pad

    def insert(self, elem: Any) -> bool:
        to_insert = Nodo(elem)
        if self.root is None:
            self.root = to_insert
            return True
        else:
            p, pad = self.search(elem)
            if p is None:
                if elem < pad.data:
                    pad.left = to_insert
                else:
                    pad.right = to_insert
                # rebalancear arbol

                return True
            return False

    def delete(self, elem: Any, mode: bool = True) -> bool:
        p, pad = self.search(elem)
        if p is not None:
            if p.left is None and p.right is None:
                if p == pad.left:
                    pad.left = None
                else:
                    pad.right = None
                del p
            elif p.left is not None and p.right is None:
                if p == pad.left:
                    pad.left = p.left
                else:
                    pad.right = p.left
                del p
            elif p.left is None and p.right is not None:
                if p == pad.left:
                    pad.left = p.right
                else:
                    pad.right = p.right
                del p
            else:
                if mode:
                    pred, pad_pred = self.__pred(p)
                    p.data = pred.data
                    if pred.left is not None:
                        if pad_pred == p:
                            pad_pred.left = pred.left
                        else:
                            pad_pred.right = pred.left
                    else:
                        if pad_pred == p:
                            pad_pred.left = None
                        else:
                            pad_pred.right = None
                    del pred
                else:
                    sus, pad_sus = self.__sus(p)
                    p.data = sus.data
                    if sus.right is not None:
                        if pad_sus == p:
                            pad_sus.right = sus.right
                        else:
                            pad_sus.left = sus.right
                    else:
                        if pad_sus == p:
                            pad_sus.right = None
                        else:
                            pad_sus.left = None
                    del sus
            return True
        return False

    def __pred(self, node: "Nodo") -> Tuple["Nodo", "Nodo"]:
        p, pad = node.left, node
        while p.right is not None:
            p, pad = p.right, p
        return p, pad

    def __sus(self, node: "Nodo") -> Tuple["Nodo", "Nodo"]:
        p, pad = node.right, node
        while p.left is not None:
            p, pad = p.left, p
        return p, pad
    
    def graficar(self) -> None:
            # Crea un objeto de gráfico
            dot = graphviz.Digraph(comment='Árbol de Búsqueda Binaria')

            # Crea una lista para almacenar todas las rutas de archivos temporales
            temp_files = []

            # Recorre el árbol y agrega nodos y aristas
            def add_nodes_and_edges(node, parent=None):
                if node:
                    # Obtén el directorio del script
                    script_dir = os.path.dirname(os.path.abspath(__file__))

                    # Une el directorio del script con la ruta relativa de la imagen
                    img_path = os.path.join(script_dir, f"data/{node.type}/{node.data}{node.typeImage}")

                    img = Image.open(img_path)

                    # Crea un archivo temporal para la imagen PNG
                    fd, path = tempfile.mkstemp(suffix=".png")
                    temp_files.append(path)  # Añadir la ruta a la lista
                    try:
                        with os.fdopen(fd, 'wb') as tmp:
                            # Guardar la imagen en formato PNG
                            img.save(tmp, "PNG")

                        # Agrega el nodo con la imagen como etiqueta
                        dot.node(str(node.data), label=str(node.data), image=path, shape='none', fontname="Arial Bold",
                                 fontcolor='red', labelloc='b')

                        if parent:
                            dot.edge(str(parent.data), str(node.data))
                        add_nodes_and_edges(node.left, node)
                        add_nodes_and_edges(node.right, node)

                    except Exception as e:
                        print(f"Error: {e}")

            add_nodes_and_edges(self.root)

            # Guarda el código fuente en un archivo
            dot.render('arbol-binario.gv', view=True)

            # Ahora que hemos terminado con el gráfico, podemos eliminar los archivos temporales
            for path in temp_files:
                os.remove(path)

    def altura(self) -> int: #Altura del arbol
        p=self.root
        if p is None:
            return 0
        else:
            alt_left = self.altura(p.left)
            alt_right = self.altura(p.right)
            return max(alt_left, alt_right) + 1



    def rot_der(self, p: "Nodo") -> "Nodo":
        pass
    def rot_izq(self, p: "Nodo") -> "Nodo":
        pass
    def rot_izq_der(self, p: "Nodo") -> "Nodo":
        pass
    def rot_der_izq(self, p: "Nodo") -> "Nodo":
        pass
