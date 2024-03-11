from typing import Any, List, Optional, Tuple
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
        self.type = type(data)
        self.size: int = 0

    def __str__(self) -> str:
        return str(self.data)
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
