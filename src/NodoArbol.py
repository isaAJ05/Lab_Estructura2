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
        self.padre: Optional['Nodo'] = None
        self.factor_balance:int = 0
        self.height = 1
        self.type = self.determinar_type(str(self.data)) 
        self.typeImage: str = self.determinar_typeImage(str(self.data))
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{self.type}/{self.data}{self.typeImage}")
        #se obtiene el directorio del script y se une el directorio del script con la ruta relativa de la imagen (para verificación de existencia de la imagen)
        self.size = self.get_size_archivo(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{self.type}/{self.data}{self.typeImage}"))
        self.actualizar_factor_balance()
    def __str__(self) -> str:
        return str(self.data)
    def determinar_type(self, data: str) -> str:
        # Se define las reglas para determinar el tipo según el nombre del archivo, la mayoría de las veces se basa en la presencia de ciertas palabras clave
        if "bike" in data:
            return "bike"
        elif "carsgraz" in data:
            return "cars"
        elif "cat" in data:
            return "cats"
        elif "dog" in data:
            return "dogs"
        elif str(data).startswith("0"): # En el caso de flowers se determina si el nombre del archivo comienza con un dígito
            return "flowers"
        elif "horse" in data:
            return "horses"
        elif "rider" in data:
            return "human"
        else:
            return "unknown"  # Si no se encuentra una clasificación específica
        
    def determinar_typeImage(self, data: str) -> str:
        # Es parecido al anterior, pero en este caso se determina el formato de imagen según el nombre del archivo
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
    
    def get_size_archivo(self, file_path):
        return os.path.getsize(file_path) #Se obtiene el tamaño del archivo en bytes a partir de la ruta del archivo con la función os.path.getsize

    def calcular_altura(self, nodo: Optional['Nodo']) -> int:
        if nodo is None:
            return 0
        return max(self.calcular_altura(nodo.left), self.calcular_altura(nodo.right)) + 1

    def calcular_factor_balance(self) ->None:
        altura_izquierda = self.calcular_altura(self.left)
        altura_derecha = self.calcular_altura(self.right)
        self.factor_balance = altura_derecha-altura_izquierda
        return  altura_derecha-altura_izquierda
    
    def actualizar_factor_balance(self) -> None:
        self.factor_balance = self.calcular_factor_balance()
        
    

class Tree:
    # El arbol debe insertar, eliminar, buscar, buscar todos los nodos de cierta categoria,buscar segun size
    # El arbol debe tener un metodo para balancear
    # recorrido por niveles recursivo
    # Obtener el nivel del nodo.
    # b. Obtener el factor de balanceo (equilibrio) del nodo.
    # c. Encontrar el padre del nodo.
    # d. Encontrar el abuelo del nodo.
    # e. Encontrar el tío del nodo.
    def __init__(self, data):
        self.root = Nodo(data)

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
    
 
    def level_order_recursive(self,root:Any, level=0)->None:
        if root is None:
            print("El árbol está vacío.")
            return
        if level == 0:
            print("Nivel 0:", root.data)
        
        if root.left:
            print(f"Nivel {level + 1} (izquierda):", root.left.data)
            self.level_order_recursive(root.left, level + 1)

        if root.right:
            print(f"Nivel {level + 1} (derecha):", root.right.data)
            self.level_order_recursive(root.right, level + 1)
         
    def level_order(self) -> None:
        if self.root is None:
            print("El árbol está vacío.")
            return
        q = Cola()
        q.add(self.root)
        self.ayuda(q)
        self.postorder()
    
    def ayuda(self,q:Cola) -> None:
        if q.is_empty():
            return None
        else:
            p = q.remove()
            print(p.data)
            
            if p.left is not None:
                q.add(p.left)
            if p.right is not None:
                q.add(p.right)
            self.ayuda(q)
                   
    def searchOnlyHim(self, elem: Any) -> Optional["Nodo"]:
        p = self.root
        while p is not None:
            if elem == p.data:
                return p
            elif elem < p.data:
                p = p.left
            else:
                p = p.right
        return p
    
    def search_nodos_categoria_rango(self, categoria: str, rango1: float, rango2: float) -> List["Nodo"]:
        # Lista para almacenar los nodos que cumplen con los criterios
        nodos_aprobados = []

        # Función auxiliar para recorrer el árbol
        def traverse(nodo):
            if nodo:
                # Verifica si el nodo cumple con los criterios
                if nodo.type == categoria and rango1 <= nodo.size < rango2:
                    nodos_aprobados.append(nodo)

                # Recorre los subárboles izquierdo y derecho
                traverse(nodo.left)
                traverse(nodo.right)

        # Comienza el recorrido desde la raíz del árbol
        traverse(self.root)
        return nodos_aprobados

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if not node:
            return Nodo(data)
        elif data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Caso izquierdo-izquierdo
        if balance > 1 and data < node.left.data:
            return self._rotate_right(node)

        # Caso derecho-derecho
        if balance < -1 and data > node.right.data:
            return self._rotate_left(node)

        # Caso izquierdo-derecho
        if balance > 1 and data > node.left.data:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Caso derecho-izquierdo
        if balance < -1 and data < node.right.data:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left if y else None

        if y:
            y.left = x
        x.right = T2

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        if y:
            y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right if x else None

        if x:
            x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        if x:
            x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _balance(self, nodo):
        if nodo is None:
            return nodo
        if nodo.factor_balance > 1:
            if nodo.right is not None and nodo.right.factor_balance < 0:
                nodo.right = self._rotate_right(nodo.right)
            nodo = self._rotate_left(nodo)
        elif nodo.factor_balance < -1:
            if nodo.left is not None and nodo.left.factor_balance > 0:
                nodo.left = self._rotate_left(nodo.left)
            nodo = self._rotate_right(nodo)
        return nodo

    def _rotate_left_right(self, nodo):
        if nodo is not None:
            nodo.left = self._rotate_left(nodo.left)
        return self._rotate_right(nodo)

    def _rotate_right_left(self, nodo):
        if nodo is not None:
            nodo.right = self._rotate_right(nodo.right)
        return self._rotate_left(nodo)
    
        

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        # Paso 1: eliminación estándar en un ABB
        if not root:
            return root
        elif data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._get_min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data)

        # Paso 2: actualización de la altura del nodo padre
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Paso 3: recalculación del factor de equilibrio
        balance = self._get_balance(root)

        # Paso 4: si el nodo está desequilibrado, entonces hay 4 casos
        # Caso izquierdo-izquierdo
        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._rotate_right(root)

        # Caso derecho-derecho
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._rotate_left(root)

        # Caso izquierdo-derecho
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Caso derecho-izquierdo
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self._get_min_value_node(root.left)
    
    def graficar(self) -> None:
            # Crea un objeto de gráfico
            dot = graphviz.Digraph(comment='Árbol de Búsqueda Binaria')

            # Crea una lista para almacenar todas las rutas de archivos temporales
            temp_files = []

            # Recorre el árbol y agrega nodos y aristas
            def add_nodes_and_edges(node, parent=None):
                if node:
                    
                    img_path = node.file_path

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
                         # Poner factor de balanceo de cada nodo en el gráfico
                        balance_factor = node.calcular_factor_balance()
                        dot.node(str(node.data), label=f"{str(node.data)}\n{balance_factor}", image=path, shape='none', fontname="Arial Bold", fontcolor='red', labelloc='b')
                        
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

    def get_nivel(self,nodo:Any) -> int: #Obtiene el nivel del nodo
        p=self.root
        c=0
        while p.data!=nodo.data:
            c+=1
            if nodo.data<p.data:
                p=p.left
            else:
                p=p.right
        return c
    
    def get_alturaNodo(self,nodo:Any) -> int: #Obtiene el altura del nodo
        p=self.root
        c=1 #solo se cambia la inicializacion de c
        while p.data!=nodo.data:
            c+=1
            if nodo.data<p.data:
                p=p.left
            else:
                p=p.right
        return c
                
            
        
            
    #Devuelve el padre de un nodo
    def search_daddy(self, data_s: Any) -> Optional["Nodo"]: #Busca el padre de un nodo
        p, pad = self.root, None
        s, flag = Stack(), False
        while (p is not None or not s.is_empty()) and not flag:
            if p is not None:
                if p.data == data_s:
                    if pad is not None:
                        return pad
                    flag = True
                else:
                    s.add(p)
                    pad = p
                    p = p.left
            else:
                p = s.remove()
                pad = p
                p = p.right

        if not flag or pad is None:
            return None

    def find_sibling_ayudita(self, data_s: Any) -> Optional["Nodo"]:
        parent = self.search_daddy(data_s) #Se busca el padre del nodo
        if parent is None: #Si no se encuentra el padre, no tiene hermano
            return None
        else:
          if parent.left is not None and parent.left.data == data_s: #Si el nodo es el hijo izquierdo, se devuelve el hijo derecho
              return parent.right
          elif parent.right is not None and parent.right.data == data_s: #Si el nodo es el hijo derecho, se devuelve el hijo izquierdo
              return parent.left
          else: #Si no se encuentra el nodo, no tiene hermano
              return None
          
    #se llama originalmente a esta para buscar al Hermano de un nodo
    def search_bro(self, data_: Any) -> None:
        sibling = self.find_sibling_ayudita(data_) #Se busca el hermano del nodo
        if sibling is not None:
            print(f'The sibling of {data_!r} is {sibling.data!r}')
        else:
            print(f'There is no sibling for {data_!r}')
    
    #Buscar tio : hermano del padre
    def search_tio(self,data_s:Any)->None:
      tio =None
      padre=self.search_daddy(data_s)#Se busca el padre del nodo
      if padre is not None: # Si tiene padre, se busca el hermano del padre
        tio=self.find_sibling_ayudita(padre.data)
      if tio is not None: #Si se encuentra el tio, se imprime
        print(f' El tio de {data_s!r} es {tio.data}')
      else:
        print(f' {data_s!r} no tiene tio')     
    
    # Buscar ABUELO: padre del padre
    def search_granpa(self,data_s:Any)->None:
      pa=self.search_daddy(data_s) #Se busca el padre del nodo
      granpa=None # Se inicializa la variable abuelo
      if pa is not None: #Si tiene padre, se busca el padre del padre
        granpa=self.search_daddy(pa.data)
      if granpa is not None: #Si se encuentra el abuelo, se imprime
        print(f' El abuelo de {data_s!r} es {granpa.data}')
      else:
        print(f' {data_s!r} no tiene abuelo')
            

    def balancear(self, p: "Nodo") -> "Nodo":
        if p is not None:
            p.calcular_factor_balance()
            print("---Factor de balanceo ",p.data,": ", p.factor_balance) 
            if p.factor_balance > 1:
                if p.left is not None and p.left.factor_balance >= 0:
                    p = self.rot_der(p) 
                else:
                    p = self.rot_izq_der(p)
            elif p.factor_balance < -1:
                if p.right is not None and p.right.factor_balance <= 0:
                    p = self.rot_izq(p)
                else:
                    p = self.rot_der_izq(p)

            p.calcular_factor_balance()

            p.left = self.balancear(p.left)
            p.right = self.balancear(p.right)

        return p
            

    def rot_der(self, p: "Nodo") -> "Nodo": 
        print("Rotación derecha")
        if p.left is None:
            return p
        q = p.left
        if q.right is not None:
            p.left = q.right
            q.right.padre = p
        q.right = p
        if p.padre is not None:
            if p.padre.left == p:
                p.padre.left = q
            else:
                p.padre.right = q
        q.padre = p.padre
        p.padre = q
        p.actualizar_factor_balance()
        q.actualizar_factor_balance()
        return q

    def rot_izq(self, p: "Nodo") -> "Nodo":
        print("Rotación izquierda")
        if p.right is None:
            return p
        q = p.right
        if q.left is not None:
            p.right = q.left
            q.left.padre = p
        q.left = p
        if p.padre is not None:
            if p.padre.left == p:
                p.padre.left = q
            else:
                p.padre.right = q
        q.padre = p.padre
        p.padre = q
        p.actualizar_factor_balance()
        q.actualizar_factor_balance()
        return q

    def rot_izq_der(self, p: "Nodo") -> "Nodo":
        print("Rotación izquierda-derecha")
        if p.left is not None:
            p.left = self.rot_izq(p.left)
        return self.rot_der(p)

    def rot_der_izq(self, p: "Nodo") -> "Nodo":
        print("Rotación derecha-izquierda")
        if p.right is not None:
            p.right = self.rot_der(p.right)
        return self.rot_izq(p)

    def actualizar_factores_balance(self, nodo: "Nodo") -> None:
        while nodo is not None:
            nodo.calcular_factor_balance()
            nodo = nodo.padre
    def encontrar_nodo(self, valor):
        nodo_actual = self.root
        while nodo_actual:
            if valor < nodo_actual.data:
                nodo_actual = nodo_actual.left
            elif valor > nodo_actual.data:
                nodo_actual = nodo_actual.right
            else:
                return nodo_actual
        return None
    def encontrar_primer_nodo_desbalanceado(self, nodo):
        if nodo:
            nodo_izquierdo_desbalanceado = self.encontrar_primer_nodo_desbalanceado(nodo.left)
            if nodo_izquierdo_desbalanceado:
                return nodo_izquierdo_desbalanceado
            nodo_derecho_desbalanceado = self.encontrar_primer_nodo_desbalanceado(nodo.right)
            if nodo_derecho_desbalanceado:
                return nodo_derecho_desbalanceado
            nodo.calcular_factor_balance()
            if nodo.factor_balance not in [-1, 0, 1]:
                return nodo
        return None
#
    def postorder(self, node: Optional["Nodo"] = None) -> None:
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.postorder(node.left)
            if node.right is not None:
                self.postorder(node.right)
            print("Factor de balance de ",node.data,": ", node.factor_balance)
            node.actualizar_factor_balance()
            if node.factor_balance == 2 or node.factor_balance == -2:
                print("El nodo ", node.data, " está desequilibrado")
                self.__balancear(node)
            if node.factor_balance == 1 or node.factor_balance == -1 or node.factor_balance == 0:
                print("El nodo ", node.data, " está equilibrado")
            

