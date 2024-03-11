from NodoArbol import Tree, Nodo
#from graphviz import Digraph
def main()-> None:
    print("pruebita")

    def generate_sample_abb() -> "Tree": #Genera un arbol de busqueda binaria de ejemplo
        tree = Tree(Nodo(20))
        print(tree.insert(21))
        print(tree.insert(33))
        print(tree.insert(14))
        print(tree.insert(18))
        print(tree.insert(10))
        print(tree.insert(21))
        print(tree.insert(40))
        print(tree.insert(25))

        return tree