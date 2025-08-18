# Hay padres e hijos, los cuales son nodos descendientes los cuales los hijos descienden de los padres.
# Hojas son todos los nodos hijos que no son padres.
# Ramas son los nodos padres que son a su vez hijos.
# El grado del arbol es la cantidad de nodos de la rama con mas hijos.
# El camino es la secuencia de nodos para llegar al ultimo.
# Cada parte del arbol es un sub arbol.
# La raiz es el primer nodo.

from typing import Any, Optional

class _nodeTree:
    def __init__(self, value: Any, other_values: Optional[Any] = None):
        self.value = value
        self.other_values = other_values
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value: Any):

        def __insert(root, value):
            print(f'insertar valor {value}')
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
        
    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value)
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value)
                __in_order(root.right)
        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)
        if self.root is not None:
            __post_order(self.root)

    def search(self, value: Any):
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    return root
                elif root.value < value:
                    return __search(root.right, value)
                else:
                    return __search(root.right, value)

        Aux = None        
        if self.root is not None:
            Aux = __search(self.root, value)
        return Aux    


arbol = Tree()

arbol.insert(19)
arbol.insert(7)
arbol.insert(31)
arbol.insert(11)
arbol.insert(19)
arbol.insert(27)
arbol.insert(45)

arbol.in_order()
arbol.post_order()
arbol.pre_order()