from NodoArbol import Tree, Nodo
def main()-> None:
    print("pruebita")

    def generate_sample_abb() -> "Tree":
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