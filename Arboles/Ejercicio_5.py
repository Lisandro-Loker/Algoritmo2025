
from super_heroes_data import superheroes
from tree import BinaryTree

arbol = BinaryTree()

#A- Además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
for super_heros_data in superheroes:
    arbol.insert(super_heros_data['name'], super_heros_data)

#B- Listar los villanos ordenados alfabéticamente.
def ordenar_villanos(self):
    def __ordenar_villanos(root):
        if root is not None:
            __ordenar_villanos(root.left)
            if root.other_values["is_villain"] is True:
                print(root.value)
            __ordenar_villanos(root.right)
    
    if self.root is not None:
        __ordenar_villanos(self.root)

print ("Punto B: Villanos ordenados alfabeticamente")
ordenar_villanos(arbol)
print("Fin punto B \n")

# #C- Mostrar los superheroes que empiezan con C.
def superheroes_con_c(self):
    def __superheroes_con_c(root):
        if root is not None:
            __superheroes_con_c(root.left)
            if root.value.startswith('C'):
                print(root.value)
            __superheroes_con_c(root.right)
    
    if self.root is not None:
        __superheroes_con_c(self.root)

print ("Punto C: Superheroes que empiezan con C")
superheroes_con_c(arbol)
print("Fin punto C \n")

#D- Determinar cuantos suérheroes hay en el arbol.
def contar_heroes(self):
    def __contar_heroes(root):
        if root is None:
            return 0
        else:
            return 1 + __contar_heroes(root.left) + __contar_heroes(root.right)
        
    return __contar_heroes(self.root)

print ("Punto D: Cantidad de superheroes en el arbol")
print(f'Cantidad de superheroes: {contar_heroes(arbol)}')
print("Fin punto D \n")

#E- Dr Strange esta mal cargado. Utilizar una busqueda por proximidad para enccontrarlo en el arbol y modificar su nombre.
def modificar_dr_strange(self, nombre_incorrecto, nombre_correcto):
    searched = self.proximity_search("Dr")
    if searched is not None:
        for search in searched:
            if search.value == nombre_incorrecto:
                incorrecto = search.value
                deleted_value, other_values = self.delete(incorrecto)
                if deleted_value is not None:
                    other_values["name"] = nombre_correcto
                    self.insert(nombre_correcto, other_values)
                    print(f'Se ha modificado {incorrecto} por {nombre_correcto}')
                return
        print(f'Se encontraron superheroes que empiezan con "Dr" pero no {nombre_incorrecto}.')
    else:
        print(f'No se encontro ningun superheroe que empiece con "Dr".')

print ("Punto E: Modificar Dr Strange")
modificar_dr_strange(arbol, "Dr Strannnnge", "Dr Strange")
arbol.in_order()
print("Fin punto E \n")

#F- Listar los superheroes ordenados de manera descendente.
# def superheroes_descendente(self):
#     def __superheroes_descendente(root):
#         if root is not None:
#             __superheroes_descendente(root.right)
#             print(root.value)
#             __superheroes_descendente(root.left)
    
#     if self.root is not None:
#         __superheroes_descendente(self.root)

# print ("Punto F: Superheroes ordenados de manera descendente")
# superheroes_descendente(arbol)
# print("Fin punto F \n")

# #G-1 Generar un bosque a partir de este arbol, un árbol debe contener a los superheroes y otro a los villanos.

# def generar_bosque(self):
#     arbol_heroes = BinaryTree()
#     arbol_villanos = BinaryTree()

#     def __generar_bosque(root):
#         if root is not None:
#             __generar_bosque(root.left)
#             if root.other_values["is_villain"] is True:
#                 arbol_villanos.insert(root.value, root.other_values)
#             else:
#                 arbol_heroes.insert(root.value, root.other_values)
#             __generar_bosque(root.right)
    
#     if self.root is not None:
#         __generar_bosque(self.root)
    
#     return arbol_heroes, arbol_villanos

# arbol_heroes, arbol_villanos = generar_bosque(arbol)

# print ("Punto G1: Generar un bosque a partir del arbol")
# print("Arboles ya generados.")
# print("Fin punto G1 \n")

# #G-2 Determinar los nodos de cada arbol.
# def contar_nodos(self):
#     def __contar_nodos(root):
#         if root is None:
#             return 0
#         else:
#             return 1 + __contar_nodos(root.left) + __contar_nodos(root.right)
        
#     return __contar_nodos(self.root)

# print ("Punto G2: Cantidad de nodos en cada arbol del bosque")
# print(f'Cantidad de nodos en el arbol de heroes: {contar_nodos(arbol_heroes)}')
# print(f'Cantidad de nodos en el arbol de villanos: {contar_nodos(arbol_villanos)}')
# print("Fin punto G2 \n")

# #G-3 Realizar un barrido ordenado alfabeticamente de cada árbol.
# def barrido_ordenado(self):
#     def __barrido_ordenado(root):
#         if root is not None:
#             __barrido_ordenado(root.left)
#             print(root.value)
#             __barrido_ordenado(root.right)
    
#     if self.root is not None:
#         __barrido_ordenado(self.root)

# print ("Punto G3: Barrido ordenado alfabeticamente de cada arbol del bosque")
# print("Arbol de heroes:")
# barrido_ordenado(arbol_heroes)
# print('Fin arbol de heroes \n')
# print("Arbol de villanos:")
# barrido_ordenado(arbol_villanos)
# print('Fin arbol de villanos \n')
# print("Fin punto G3 \n")