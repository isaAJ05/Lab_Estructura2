from tkinter import Image
from PIL import Image
import os
from NodoArbol import Tree, Nodo
import graphviz
import tempfile

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

    # Genera el árbol de ejemplo
    sample_tree = generate_sample_abb()

    # Crea un objeto de gráfico
    dot = graphviz.Digraph(comment='Árbol de Búsqueda Binaria')

    # Create a list to hold all temporary file paths
    temp_files = []
   # Recorre el árbol y agrega nodos y aristas
    def add_nodes_and_edges(node, parent=None):
        if node:
            
            # Get the directory of the script
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Join the script directory with the relative path to the image
            img_path = os.path.join(script_dir, f"data/{node.type}/{node.data}{node.typeImage}")

            img = Image.open(img_path)

            # Create a temporary file for the PNG image
            fd, path = tempfile.mkstemp(suffix=".png")
            temp_files.append(path)  # Add the path to the list
            try:
                with os.fdopen(fd, 'wb') as tmp:
                    # Save the image in PNG format
                    img.save(tmp, "PNG")

                # Agrega el nodo con la imagen como etiqueta
                dot.node(str(node.data), label='', image=path, shape='none')

                if parent:
                    dot.edge(str(parent.data), str(node.data))
                add_nodes_and_edges(node.left, node)
                add_nodes_and_edges(node.right, node)

            except Exception as e:
                print(f"Error: {e}")

    add_nodes_and_edges(sample_tree.root)

    # Guarda el código fuente en un archivo
    dot.render('arbol-binario.gv', view=True)

    # Now that we're done with the graph, we can delete the temp files
    for path in temp_files:
        os.remove(path)

if __name__ == "__main__":
    main()
