from typing import Any, List, Optional, Tuple
import graphviz
import tempfile
from tkinter import Image
from PIL import Image
import os
class Stack: #Clase pila
    def __init__(self) -> None:
        self.stack: List[Any] = []

    def add(self, elem: Any) -> None:
        self.stack.append(elem)

    def remove(self) -> Any:
        return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

class Cola: #Clase cola
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
        self.data = data #Dato del nodo(metrica)
        self.left: Optional['Nodo'] = None
        self.right: Optional['Nodo'] = None
        self.padre: Optional['Nodo'] = None #Se agrega el atributo padre
        self.factor_balance:int = 0         #Se agrega el atributo factor de balanceo inicializado en 0
        self.height = 1 #Altura del nodo inicializada en 1
        self.type = self.determinar_type(str(self.data))  #Se determina el tipo de imagen, se llama metodo
        self.typeImage: str = self.determinar_typeImage(str(self.data)) #Se determina el formato de la imagen, se llama metodo
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{self.type}/{self.data}{self.typeImage}")
        #se obtiene el directorio del script y se une el directorio del script con la ruta relativa de la imagen (para verificación de existencia de la imagen)
        self.size = self.get_size_archivo(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{self.type}/{self.data}{self.typeImage}")) #Se obtiene el tamaño del archivo
        self.actualizar_factor_balance() #Se actualiza el factor de balanceo
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
        if nodo is None: #Si el nodo es nulo, se retorna 0 (caso base)
            return 0
        return max(self.calcular_altura(nodo.left), self.calcular_altura(nodo.right)) + 1 #Se retorna el máximo entre la altura del subárbol izquierdo y derecho más 1

    def calcular_factor_balance(self) ->None: #Se calcula el factor de balanceo
        altura_izquierda = self.calcular_altura(self.left) #Se obtiene la altura del subárbol izquierdo
        altura_derecha = self.calcular_altura(self.right) #Se obtiene la altura del subárbol derecho
        self.factor_balance = altura_derecha-altura_izquierda #Se hace la resta
        return  altura_derecha-altura_izquierda #Se retorna el factor de balanceo
    
    def actualizar_factor_balance(self) -> None: #Se actualiza el factor de balanceo en el atributo del nodo
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

    def search(self, elem: Any) -> Tuple[Optional["Nodo"], Optional["Nodo"]]: #Busca un nodo
        p, pad = self.root, None #Se inicializa el nodo y su padre
        while p is not None:#Mientras el nodo no sea nulo
            if elem == p.data: #Si el elemento es igual al dato del nodo, se retorna el nodo y su padre
                return p, pad
            elif elem < p.data:#Si el elemento es menor que el dato del nodo (izq), se actualiza el padre y se va al hijo izquierdo
                pad = p
                p = p.left
            else: #Si el elemento es mayor que el dato del nodo (der), se actualiza el padre y se va al hijo derecho
                pad = p
                p = p.right
        #Si no se encuentra el nodo, se retorna None
        return p, pad
    
 
         
    def level_order(self) -> None: #Recorrido por niveles recursivo
        if self.root is None: #Si el árbol está vacío, se imprime un mensaje
            print("El árbol está vacío.")
            return
        q = Cola() #Se inicializa una cola
        q.add(self.root) #Se agrega la raíz a la cola
        self.ayuda(q) #Se llama al método ayuda para recorrer el árbol 
      #  self.postorder() #Se llama al método postorder para verificar el factor de balanceo de cada nodo
    
    def ayuda(self,q:Cola) -> None: #Método para recorrer el árbol (ayuda al método level_order)
        if q.is_empty(): #Si la cola está vacía (caso base)
            return None
        else: #Si la cola no está vacía
            p = q.remove() #Se remueve el primer elemento de la cola
            print(p.data) #Se imprime el dato del nodo
            
            if p.left is not None: #Si el nodo tiene hijo izquierdo, se agrega a la cola
                q.add(p.left)
            if p.right is not None:#Si el nodo tiene hijo derecho, se agrega a la cola
                q.add(p.right)
            self.ayuda(q) #Se llama recursivamente al método ayuda para recorrer el árbol
                   
    def searchOnlyHim(self, elem: Any) -> Optional["Nodo"]:#Busca un nodo
        p = self.root #Se inicializa el nodo
        while p is not None:#Mientras el nodo no sea nulo
            if elem == p.data: #Si el elemento es igual al dato del nodo, se retorna el nodo
                return p
            elif elem < p.data: #Si el elemento es menor que el dato del nodo (izq), se va al hijo izquierdo
                p = p.left
            else: #Si el elemento es mayor que el dato del nodo (der), se va al hijo derecho
                p = p.right
        return p
    
    def search_nodos_categoria_rango(self, categoria: str, rango1: float, rango2: float) -> List["Nodo"]:
        # Lista para almacenar los nodos que cumplen con los criterios, incialemente vacía
        nodos_aprobados = []

        # Función auxiliar para recorrer el árbol
        def traverse(nodo):
            if nodo:
                # Verifica si el nodo cumple con los criterios
                if nodo.type == categoria and rango1 <= nodo.size < rango2:
                    nodos_aprobados.append(nodo) # Si cumple, se agrega a la lista

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
    
    def graficar(self) -> None: #Método para graficar el árbol
        # Crea un objeto de gráfico
        dot = graphviz.Digraph(comment='Árbol de Búsqueda Binaria')

        # Recorre el árbol y agrega nodos y aristas
        def add_nodes_and_edges(node, parent=None):
            if node:
                # Poner factor de balanceo de cada nodo en el gráfico
                balance_factor = node.calcular_factor_balance()
                dot.node(str(node.data), label=f"{str(node.data)}\n{balance_factor}", shape='circle', fontname="Arial Bold", fontcolor='red', labelloc='b')
                
                if parent:
                    dot.edge(str(parent.data), str(node.data))
                add_nodes_and_edges(node.left, node)
                add_nodes_and_edges(node.right, node)

        add_nodes_and_edges(self.root)

        # Guarda el código fuente en un archivo
        dot.render('arbol-binario.gv', view=True)

    def altura(self) -> int: #Altura del arbol
        p=self.root #Se inicializa el nodo
        if p is None: #Si el nodo es nulo, se retorna 0
            return 0    
        else:
            alt_left = self.altura(p.left) #Se obtiene la altura del subárbol izquierdo
            alt_right = self.altura(p.right) #Se obtiene la altura del subárbol derecho
            return max(alt_left, alt_right) + 1 #Se retorna el máximo entre la altura del subárbol izquierdo y derecho más 1

    def get_nivel(self,nodo:Any) -> int: #Obtiene el nivel del nodo
        p=self.root #Se inicializa el nodo
        c=0 #Se inicializa el contador en 0 
        while p.data!=nodo.data: #Mientras el dato del nodo sea diferente al dato del nodo
            c+=1 #Se aumenta el contador
            if nodo.data<p.data: #Si el dato del nodo es menor que el dato del nodo (izq), se va al hijo izquierdo
                p=p.left  
            else: #Si el dato del nodo es mayor que el dato del nodo (der), se va al hijo derecho
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
        p, pad = self.root, None #Se inicializa el nodo y su padre
        s, flag = Stack(), False #Se inicializa una pila y un flag en False
        while (p is not None or not s.is_empty()) and not flag: #Mientras el nodo no sea nulo o la pila no esté vacía y el flag sea falso
            if p is not None: #Si el nodo no es nulo
                if p.data == data_s: #Si el dato del nodo es igual al dato del nodo buscado
                    if pad is not None: #Si el padre no es nulo, se retorna el padre
                        return pad  
                    flag = True #Se cambia el flag a verdadero
                else: #Si el dato del nodo no es igual al dato del nodo buscado
                    s.add(p) #Se agrega el nodo a la pila
                    pad = p #Se actualiza el padre
                    p = p.left #Se va al hijo izquierdo
            else: #Si el nodo es nulo
                p = s.remove() #Se remueve el nodo de la pila
                pad = p #Se actualiza el padre
                p = p.right #Se va al hijo derecho

        if not flag or pad is None: #Si el flag es falso o el padre es nulo, se retorna None
            return None 

    def find_sibling_ayudita(self, data_s: Any) -> Optional["Nodo"]: #Método para buscar el hermano de un nodo
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
            print(f'The sibling of {data_!r} is {sibling.data!r}') #Si se encuentra el hermano, se imprime
        else:
            print(f'There is no sibling for {data_!r}') #Si no se encuentra el hermano, se imprime
    
    #Buscar tio : hermano del padre
    def search_tio(self,data_s:Any)->None:
      tio =None
      padre=self.search_daddy(data_s)#Se busca el padre del nodo
      if padre is not None: # Si tiene padre, se busca el hermano del padre
        tio=self.find_sibling_ayudita(padre.data)
      if tio is not None: #Si se encuentra el tio, se imprime
        print(f' El tio de {data_s!r} es {tio.data}')  
      else:
        print(f' {data_s!r} no tiene tio') #Si no se encuentra el tio, se imprime     
    
    # Buscar ABUELO: padre del padre
    def search_granpa(self,data_s:Any)->None:
      pa=self.search_daddy(data_s) #Se busca el padre del nodo
      granpa=None # Se inicializa la variable abuelo
      if pa is not None: #Si tiene padre, se busca el padre del padre
        granpa=self.search_daddy(pa.data)
      if granpa is not None: #Si se encuentra el abuelo, se imprime
        print(f' El abuelo de {data_s!r} es {granpa.data}')
      else:
        print(f' {data_s!r} no tiene abuelo') #Si no se encuentra el abuelo, se imprime
            

    def balancear(self, p: "Nodo") -> "Nodo": #Método para balancear el árbol
        if p is not None:
            p.calcular_factor_balance() 
            print("---Factor de balanceo ",p.data,": ", p.factor_balance)  #Se imprime el factor de balanceo del nodo
            if p.factor_balance > 1: #Si el factor de balanceo es mayor que 1
                if p.left is not None and p.left.factor_balance >= 0: #Si el hijo izquierdo del nodo no es nulo y el factor de balanceo del hijo izquierdo es mayor o igual que 0
                    p = self.rot_der(p)  #Se rota a la derecha el nodo
                else:
                    p = self.rot_izq_der(p) #Se rota a la izquierda-derecha el nodo
            elif p.factor_balance < -1: #Si el factor de balanceo es menor que -1
                if p.right is not None and p.right.factor_balance <= 0: #Si el hijo derecho del nodo no es nulo y el factor de balanceo del hijo derecho es menor o igual que 0
                    p = self.rot_izq(p) #Se rota a la izquierda el nodo
                else:  
                    p = self.rot_der_izq(p)     #Se rota a la derecha-izquierda el nodo

            p.calcular_factor_balance() #Se recalcula el factor de balanceo del nodo

            p.left = self.balancear(p.left) #Se balancea el hijo izquierdo del nodo
            p.right = self.balancear(p.right)   #Se balancea el hijo derecho del nodo

        return p
            

    def rot_der(self, p: "Nodo") -> "Nodo":  #Método para rotar a la derecha
        print("Rotación derecha") #Se imprime el tipo de rotación
        if p.left is None: #Si el hijo izquierdo del nodo es nulo, se retorna el nodo
            return p
        q = p.left #Se obtiene el hijo izquierdo del nodo
        if q.right is not None: #Si el hijo derecho del hijo izquierdo del nodo no es nulo
            p.left = q.right #Se cambia el hijo izquierdo del nodo por el hijo derecho del hijo izquierdo del nodo
            q.right.padre = p #Se cambia el padre del hijo derecho del hijo izquierdo del nodo por el nodo
        q.right = p #Se cambia el hijo derecho del hijo izquierdo del nodo por el nodo
        if p.padre is not None: #Si el padre del nodo no es nulo
            if p.padre.left == p: #Si el nodo es el hijo izquierdo del padre, se cambia el hijo izquierdo del padre por el nodo
                p.padre.left = q 
            else:
                p.padre.right = q #Si el nodo es el hijo derecho del padre, se cambia el hijo derecho del padre por el nodo
        q.padre = p.padre #Se cambia el padre del nodo por el padre del nodo
        p.padre = q #Se cambia el padre del nodo por el nodo
        p.actualizar_factor_balance() #Se actualiza el factor de balanceo del nodo
        q.actualizar_factor_balance() #Se actualiza el factor de balanceo del nodo
        return q

    def rot_izq(self, p: "Nodo") -> "Nodo": #Método para rotar a la izquierda
        print("Rotación izquierda") #Se imprime el tipo de rotación
        if p.right is None: #Si el hijo derecho del nodo es nulo, se retorna el nodo
            return p
        q = p.right #Se obtiene el hijo derecho del nodo
        if q.left is not None: #Si el hijo izquierdo del hijo derecho del nodo no es nulo
            p.right = q.left #Se cambia el hijo derecho del nodo por el hijo izquierdo del hijo derecho del nodo
            q.left.padre = p #Se cambia el padre del hijo izquierdo del hijo derecho del nodo por el nodo
        q.left = p #Se cambia el hijo izquierdo del hijo derecho del nodo por el nodo
        if p.padre is not None: #Si el padre del nodo no es nulo
            if p.padre.left == p: #Si el nodo es el hijo izquierdo del padre, se cambia el hijo izquierdo del padre por el nodo
                p.padre.left = q 
            else:
                p.padre.right = q #Si el nodo es el hijo derecho del padre, se cambia el hijo derecho del padre por el nodo
        q.padre = p.padre #Se cambia el padre del nodo por el padre del nodo
        p.padre = q #Se cambia el padre del nodo por el nodo
        p.actualizar_factor_balance() #Se actualiza el factor de balanceo del nodo
        q.actualizar_factor_balance() 
        return q

    def rot_izq_der(self, p: "Nodo") -> "Nodo": #Método para rotar a la izquierda-derecha
        print("Rotación izquierda-derecha") #Se imprime el tipo de rotación
        if p.left is not None: #Si el hijo izquierdo del nodo no es nulo
            p.left = self.rot_izq(p.left) #Se rota a la izquierda el hijo izquierdo del nodo
        return self.rot_der(p) #Se rota a la derecha el nodo

    def rot_der_izq(self, p: "Nodo") -> "Nodo": #Método para rotar a la derecha-izquierda
        print("Rotación derecha-izquierda") #Se imprime el tipo de rotación
        if p.right is not None: #Si el hijo derecho del nodo no es nulo
            p.right = self.rot_der(p.right) #Se rota a la derecha el hijo derecho del nodo
        return self.rot_izq(p)  #Se rota a la izquierda el nodo

    def actualizar_factores_balance(self, nodo: "Nodo") -> None: #Método para actualizar los factores de balanceo
        while nodo is not None: #Mientras el nodo no sea nulo
            nodo.calcular_factor_balance() #Se calcula el factor de balanceo del nodo
            nodo = nodo.padre #Se actualiza el nodo al padre
    def encontrar_nodo(self, valor): #Método para encontrar un nodo
        nodo_actual = self.root #Se inicializa el nodo actual
        while nodo_actual: #Mientras el nodo actual no sea nulo
            if valor < nodo_actual.data: #Si el valor es menor que el dato del nodo actual, se va al hijo izquierdo
                nodo_actual = nodo_actual.left 
            elif valor > nodo_actual.data: #Si el valor es mayor que el dato del nodo actual, se va al hijo derecho
                nodo_actual = nodo_actual.right
            else:
                return nodo_actual #Si el valor es igual al dato del nodo actual, se retorna el nodo actual
        return None
    def encontrar_primer_nodo_desbalanceado(self, nodo): #Método para encontrar el primer nodo desbalanceado
        if nodo: #Si el nodo no es nulo
            nodo_izquierdo_desbalanceado = self.encontrar_primer_nodo_desbalanceado(nodo.left)  #Se busca el primer nodo desbalanceado en el hijo izquierdo
            if nodo_izquierdo_desbalanceado: #Si se encuentra el nodo desbalanceado, se retorna
                return nodo_izquierdo_desbalanceado     
            nodo_derecho_desbalanceado = self.encontrar_primer_nodo_desbalanceado(nodo.right) #Se busca el primer nodo desbalanceado en el hijo derecho
            if nodo_derecho_desbalanceado: #Si se encuentra el nodo desbalanceado, se retorna
                return nodo_derecho_desbalanceado  
            nodo.calcular_factor_balance() #Se calcula el factor de balanceo del nodo
            if nodo.factor_balance not in [-1, 0, 1]: #Si el factor de balanceo no está en [-1, 0, 1], se retorna el nodo
                return nodo 
        return None #Si no se encuentra el nodo desbalanceado, se retorna None
#
    def postorder(self, node: Optional["Nodo"] = None) -> None: #Método para recorrer el árbol en postorden
        if node is None: #Si el nodo es nulo, se retorna
            node = self.root
        if node is not None: #Si el nodo no es nulo
            if node.left is not None:
                self.postorder(node.left) #Se llama recursivamente al método postorder para recorrer el subárbol izquierdo
            if node.right is not None:
                self.postorder(node.right) #Se llama recursivamente al método postorder para recorrer el subárbol derecho
         #   print("Factor de balance de ",node.data,": ", node.factor_balance) #Se imprime el factor de balanceo del nodo
            node.actualizar_factor_balance() #Se actualiza el factor de balanceo del nodo
            if node.factor_balance == 2 or node.factor_balance == -2: #Si el factor de balanceo es 2 o -2
              #  print("El nodo ", node.data, " está desequilibrado") #Se imprime que el nodo está desequilibrado
                self.__balancear(node) #Se balancea el nodo
          #  if node.factor_balance == 1 or node.factor_balance == -1 or node.factor_balance == 0: #Si el factor de balanceo es 1, -1 o 0
              #  print("El nodo ", node.data, " está equilibrado")   #Se imprime que el nodo está equilibrado
            

