# Hay padres e hijos, los cuales son nodos descendientes los cuales los hijos descienden de los padres.
# Hojas son todos los nodos hijos que no son padres.
# Ramas son los nodos padres que son a su vez hijos.
# El grado del arbol es la cantidad de nodos de la rama con mas hijos.
# El camino es la secuencia de nodos para llegar al ultimo.
# Cada parte del arbol es un sub arbol.
# La raiz es el primer nodo.

from typing import Any

class _nodeTree:
    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value: Any):

        def __insert(root, value):
            print(f'insertar value {value}')
            if root is None:
                print ("Insertar Raiz")
                return _nodeTree(value)
            elif value < root.value:
                print (f'Insertar valor a la izquierda -> padre {root.value}')
                root.left = __insert(root.left, value)
            else:
                print (f'Insertar valor a la derecha -> padre {root.value}')
                root.right = __insert(root.right, value)
            
            return root
        
        self.root = __insert(self.root, value)


arbol = Tree()

arbol.insert(19)
arbol.insert(7)
arbol.insert(31)
arbol.insert(11)

print(arbol.root.value, arbol.root.left.value, arbol.root.right.value)