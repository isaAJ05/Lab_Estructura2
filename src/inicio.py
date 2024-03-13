from NodoArbol import Tree, Nodo

def main() -> None:
    
    def generate_sample_abb() -> Tree:
        # Genera un árbol de búsqueda binaria de ejemplo
        tree = Tree(Nodo("bike_001"))
        tree.insert("dog.1")
        tree.insert("carsgraz_001")
        tree.insert("cat.1")
        tree.insert("0002")
        tree.insert("0001")
        tree.insert("0003")
        tree.insert("horse-1")
        tree.insert("rider-1")
        return tree
    
    print("\nBienvenidx")
    # Genera un árbol de búsqueda binaria de ejemplo
    sample_tree = generate_sample_abb()
    sample_tree.graficar()  # Genera el gráfico del árbol
    
    # Menú de opciones
    while True:
        print("OPERACIONES")
        print("1. Insertar nodo")
        print("2. Eliminar nodo")
        print("3. Buscar nodo")
        print("4. Buscar nodos por categoría y rango de peso")  
        print("5. Salir")
        option = input("\n->Ingrese una opción: ")

        if option == "1":
            #Operación para insertar un nodo
            node_data = input("Ingrese el dato del nodo a insertar: ")
            sample_tree.insert(node_data)
            sample_tree.graficar()  # Vuelve a generar el gráfico

        elif option == "2":
            #Operación para eliminar un nodo
            node_data = input("Ingrese el dato del nodo a eliminar: ")
            sample_tree.delete(node_data)
            sample_tree.graficar()  # Vuelve a generar el gráfico

        elif option == "3":
            #Operación para buscar un nodo
            node_data = input("Ingrese el dato del nodo a buscar: ")
            found_node = sample_tree.search(node_data)
            if found_node:
                print("El nodo se encuentra en el árbol.")
            else:
                print("El nodo no se encuentra en el árbol.")

        elif option == "4":
            # Buscar nodos por categoría y peso
            categoria = input("Ingrese la categoría: ").lower()
            print("Ingrese un rango (en bytes) del peso del archivo")
            rango1 = float(input("De: "))
            rango2 = float(input("Hasta: "))
            nodos_encontrados= sample_tree.search_nodos_categoria_rango(categoria, rango1, rango2)
            if nodos_encontrados:
                print("Nodos encontrados:")
                for nodo in nodos_encontrados:
                    print(nodo.data)
            else:
                print("No se encontraron nodos con la categoría y peso especificados.")

        elif option == "5":
            #Salir del programa
            print("¡Muchas gracias por implementar el programa!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        print("*************************************************************\n")
if __name__ == "__main__":
    main()
