from NodoArbol import Tree, Nodo
from typing import Any, List, Optional, Tuple

def main() -> None:
    
    def generate_sample_abb() -> Tree:
        # Genera un árbol de búsqueda binaria de ejemplo
        tree = Tree("dog.161")
        tree.insert("0129")
        tree.insert("horse-42")
        tree.insert("bike_107")
        tree.insert("cat.142")
        tree.insert("dog.73")
        tree.insert("rider-107")
        tree.insert("bike_110")
        tree.insert("horse-9")
        tree.insert("carsgraz_177")
        tree.insert("carsgraz_100")
        tree.insert("rider-37")
        tree.insert("cat.72")
        tree.insert("0038")
        tree.insert("dog.60")
        tree.insert("bike_238")
        tree.insert("horse-198")
        tree.insert("0177")
        tree.insert("carsgraz_354")
        tree.insert("cat.153")
        tree.insert("carsgraz_127")
        tree.insert("bike_072")
        tree.insert("rider-201")
        tree.insert("rider-125")
        tree.insert("cat.100")
        tree.insert("dog.165")
        tree.insert("horse-139")
        tree.insert("0130")
        return tree
    
    print("\nBienvenidx")
    # Genera un árbol de búsqueda binaria de ejemplo
    sample_tree = generate_sample_abb()
    sample_tree.graficar()  # Genera el gráfico del árbol
    
   
    while True:
        # Menú principal de opciones
        print("OPERACIONES")
        print("1. Insertar nodo")
        print("2. Eliminar nodo")
        print("3. Buscar nodo")
        print("4. Buscar nodos por categoría y rango de peso") 
        print("5. Recorrido por niveles del árbol ") 
        print("6. Salir")
        option = input("\n->Ingrese una opción: ")

        if option == "1":
            #Operación para insertar un nodo
            node_data = input("Ingrese el dato del nodo a insertar: ")
            sample_tree.insert(node_data) # Inserta el nodo en el árbol
            sample_tree.graficar()  # Vuelve a generar el gráfico

        elif option == "2":
            #Operación para eliminar un nodo
            node_data = input("Ingrese el dato del nodo a eliminar: ")
            sample_tree.delete(node_data) # Elimina el nodo del árbol
            sample_tree.graficar()  # Vuelve a generar el gráfico

        elif option == "3":
            #Operación para buscar un nodo
            node_data = input("Ingrese el dato del nodo a buscar: ") 
            found_node = sample_tree.search(node_data) # Busca el nodo en el árbol
        
            if found_node: # Si el nodo fue encontrado
                print("El nodo se encuentra en el árbol.")
                print("Desea realizar mas acciones con este nodo? (S/N)")
                moreop= input("\n->Ingrese una opción: ")
                # Submenú de opciones para trabajar con el nodo encontrado
                while(moreop=="s" or moreop=="S"):
                    print("a. Obtener nivel del nodo")
                    print("b. Obtener factor de Balanceo del nodo")
                    print("c. Obtener el padre del nodo")
                    print("d. Obtener el abuelo del nodo")
                    print("e. Obtener el tío del nodo")
                    opp = input("\n->Ingrese una opción: ")
                    match(opp):
                        case "a":
                            # Obtener nivel del nodo
                            print("El nivel del nodo es: ", sample_tree.get_nivel(found_node[0]))
                        case "b":
                            # Obtener factor de balanceo del nodo
                            found_node[0].actualizar_factor_balance()
                            print("El factor de balanceo del nodo es: ", found_node[0].factor_balance)
                        case "c":
                            # Obtener el padre del nodo - si existe
                            if(sample_tree.search_daddy(found_node[0].data)==None):
                                pass
                               # print("El nodo no tiene padre.")
                            else:
                                print("El padre del nodo es: ", sample_tree.search_daddy(found_node[0].data).data)
                        case "d":
                            # Obtener el abuelo del nodo - si existe
                            if(sample_tree.search_granpa(found_node[0].data)==None):
                                pass
                                #print("El nodo no tiene abuelo.")
                            else:
                                print("El abuelo del nodo es: ", sample_tree.search_granpa(found_node[0].data).data)
                        case "e":
                            # Obtener el tío del nodo - si existe
                            if(sample_tree.search_tio(found_node[0].data)==None):
                                pass
                                #print("El nodo no tiene tío.")
                            else:
                                print("El tío del nodo es: ", sample_tree.search_tio(found_node[0].data).data)
                    print("\n Desea realizar mas acciones con este nodo? (S/N)")
                    moreop= input("\n->Ingrese una opción: ")  
                            
            else:
                print("El nodo no se encuentra en el árbol.")

        elif option == "4":
            # Buscar nodos por categoría y peso
            categoria = input("Ingrese la categoría: ").lower()
            print("Ingrese un rango (en bytes) del peso del archivo")
            rango1 = float(input("De: ")) # Rango inferior
            rango2 = float(input("Hasta: ")) # Rango superior
            nodos_encontrados= sample_tree.search_nodos_categoria_rango(categoria, rango1, rango2) # Busca los nodos según rango de bytes y categoría
            if nodos_encontrados:
                print("Nodos encontrados:")
                for nodo in nodos_encontrados:
                    print(nodo.data) # Imprime los nodos encontrados
                
                print("Desea realizar mas acciones con algun nodo? (S/N)")
                moreop= input("\n->Ingrese una opción: ")
                
                while(moreop=="s" or moreop=="S"):
                    
                    print ("Ingrese el nombre del nodo con el que desea trabajar")
                    name = input("->Ingrese nombre: ") # Ingresa el nombre del nodo con el que se desea trabajar
                    found = None 
                    while found == None: # Verifica que el nodo ingresado sea válido
                        for nodo in nodos_encontrados: # Busca el nodo en la lista de nodos encontrados
                            if nodo.data == name:
                                found = nodo # Si el nodo es válido, lo almacena
                                break
                        if found == None:
                            
                            print("El nodo no se encuentra en la lista de nodos encontrados.")
                            print ("\n Ingrese correctamente el nombre del nodo con el que desea trabajar")
                            name = input("->Ingrese nombre: ")
                    # Submenú de opciones para trabajar con el nodo encontrado    
                    print("\na. Obtener nivel del nodo")
                    print("b. Obtener factor de Balanceo nodo")
                    print("c. Obtener el padre del nodo")
                    print("d. Obtener el abuelo del nodo")
                    print("e. Obtener el tío del nodo")
                    opp = input("\n->Ingrese una opción: ")
                    match(opp):
                        case "a":
                            # Obtener nivel del nodo
                            print("El nivel del nodo es: ", sample_tree.get_nivel(found))
                        case "b":
                            # Obtener factor de balanceo del nodo
                            found.actualizar_factor_balance()
                            print("El factor de balanceo del nodo es: ", found.factor_balance)
                        case "c":
                            # Obtener el padre del nodo - si existe
                            if(sample_tree.search_daddy(found.data)==None):
                                pass
                                #print("El nodo no tiene padre.")
                            else:
                                print("El padre del nodo es: ", sample_tree.search_daddy(found.data).data)
                        case "d":
                            # Obtener el abuelo del nodo - si existe
                            if(sample_tree.search_granpa(found.data)==None):
                                pass
                                #print("El nodo no tiene abuelo.")
                            else:
                                print("El abuelo del nodo es: ", sample_tree.search_granpa(found.data).data)
                        case "e":
                            # Obtener el tío del nodo - si existe
                            if(sample_tree.search_tio(found.data)==None):
                                pass
                                #print("El nodo no tiene tío.")
                            else:
                                print("El tío del nodo es: ", sample_tree.search_tio(found.data).data)
                    print("\n Desea realizar mas acciones con algun nodo? (S/N)")
                    moreop= input("\n->Ingrese una opción: ")
            else:
                print("No se encontraron nodos con la categoría y peso especificados.")
        elif option == "5":
            #Recorrido por niveles del árbol
            print("Recorrido por niveles del árbol:")
            sample_tree.level_order()
        elif option == "6":
            #Salir del programa
            print("¡Muchas gracias por implementar el programa!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        print("*************************************************************\n")
if __name__ == "__main__":
    main()
