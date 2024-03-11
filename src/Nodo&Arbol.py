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

    def __str__(self) -> str:
        return str(self.data)
    def calcular_factor_balance(self) -> None: #Calcula el factor de balance
        if self.left is not None:
            self.factor_balance = self.left.get_height()
        else:
            self.factor_balance = 0
        if self.right is not None:
            self.factor_balance -= self.right.get_height()
        else:
            self.factor_balance -= 0


    def get_height(self) -> int: #Altura del nodo
        if self.left is not None and self.right is not None:
            return 1 + max(self.left.get_height(), self.right.get_height())
        elif self.left is not None:
            return 1 + self.left.get_height()
        elif self.right is not None:
            return 1 + self.right.get_height()
        else:
            return 1

class Tree:

    def __init__(self, root: "Nodo") -> None: #Inicializa el arbol
        self.root = root
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
