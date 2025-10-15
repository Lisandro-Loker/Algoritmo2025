from tree import BinaryTree
from criaturas_data import Criaturas

# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla (fuera del archivo)
arbol_criaturas = BinaryTree()

for criaturas_data in Criaturas:
    arbol_criaturas.insert(criaturas_data['Nombre'], criaturas_data)

#A- Listado inorden de las criaturas y quienes la derrotaron.
print("Punto A: Listado inorden de las criaturas y quienes la derrotaron.")
def listado_inorden_derrotados(arbol_criaturas):
    def __listado_inorden_derrotados(root):
        if root is not None:
            __listado_inorden_derrotados(root.left)
            print(f"Criatura: {root.value}, Derrotado por: {root.other_values['Derrotado por']}")
            __listado_inorden_derrotados(root.right)
    
    if arbol_criaturas.root is not None:
        __listado_inorden_derrotados(arbol_criaturas.root)

listado_inorden_derrotados(arbol_criaturas)
print("Fin punto A \n")

#B- poder cargar una descripción de cada criatura.
# def cargar_descripcion(arbol_criaturas, nombre, descripcion):
#     root = arbol_criaturas.search(nombre)
#     if root is not None:
#         root.other_values['descripción'] = descripcion
#         print(f"Descripción actualizada para {nombre}.")
#     else:
#         print(f"Criatura {nombre} no encontrada en el árbol.")

# print("Punto B: Cargar una descripción de cada criatura.")
# for criatura in Criaturas:
#     nombre = criatura['Nombre']
#     descripcion = input(f"Ingrese la descripción para {nombre}: ")
#     cargar_descripcion(arbol_criaturas, nombre, descripcion)
# print("Fin punto B \n")

#C- Mostrar toda la info de la criatura Talos
def mostrar_info_Talos(arbol_criaturas, nombre):
    root = arbol_criaturas.search(nombre)
    print(f"Información de {nombre}: {root.other_values}")

print("Punto C: Mostrar toda la info de la criatura Talos")
mostrar_info_Talos(arbol_criaturas, "Talos")
print("Fin punto C \n")

#D- Demostras los 3 Heroes o Dioses que derrotaron más criaturas.
def top_3_victorias(arbol_criaturas):
    derrotadores_count = {}

    def __contar_derrotadores(root):
        if root is not None:
            derrotador = root.other_values['Derrotado por']
            if derrotador != "-":
                if derrotador in derrotadores_count:
                    derrotadores_count[derrotador] += 1
                else:
                    derrotadores_count[derrotador] = 1
            __contar_derrotadores(root.left)
            __contar_derrotadores(root.right)

    if arbol_criaturas.root is not None:
        __contar_derrotadores(arbol_criaturas.root)

    top_3 = sorted(derrotadores_count.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Top 3 Heroes o Dioses que derrotaron más criaturas:")
    for derrotador, count in top_3:
        print(f"{derrotador}: {count} criaturas derrotadas")

print("Punto D: Top 3 Heroes o Dioses que derrotaron más criaturas")
top_3_victorias(arbol_criaturas)
print("Fin punto D \n")

#E- Lista de criaturas que derroto Heracles
def criaturas_derrotadas_por(arbol_criaturas, nombre):
    criaturas = []

    def __buscar_criaturas(root):
        if root is not None:
            if root.other_values['Derrotado por'] == nombre:
                criaturas.append(root.value)
            __buscar_criaturas(root.left)
            __buscar_criaturas(root.right)

    __buscar_criaturas(arbol_criaturas.root)
    return criaturas

print("Punto E: Lista de criaturas que derroto Heracles")
criaturas_heracles = criaturas_derrotadas_por(arbol_criaturas, "Heracles")
print(f"Criaturas derrotadas por Heracles: {criaturas_heracles}")
print("Fin punto E \n")

#F- Lista de crituras que no han sido derrotadas.
def criaturas_no_derrotadas(arbol_criaturas):
    criaturas = []

    def __buscar_no_derrotadas(root):
        if root is not None:
            if root.other_values['Derrotado por'] == "-":
                criaturas.append(root.value)
            __buscar_no_derrotadas(root.left)
            __buscar_no_derrotadas(root.right)

    __buscar_no_derrotadas(arbol_criaturas.root)
    return criaturas

print("Punto F: Lista de criaturas que no han sido derrotadas")
criaturas_sin_derrotar = criaturas_no_derrotadas(arbol_criaturas)
print(f"Criaturas no derrotadas: {criaturas_sin_derrotar}")
print("Fin punto F \n")

#H- Modificar los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó.
def capturar_criatura(arbol_criaturas, nombre, capturado_por):
    root = arbol_criaturas.search(nombre)
    if root is not None:
        root.other_values['capturado_por'] = capturado_por

print("Punto H: Modificar nodos de ciertas criaturas indicando que Heracles las atrapó")
criaturas_a_capturar = ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]
for criatura in criaturas_a_capturar:
    capturar_criatura(arbol_criaturas, criatura, "Heracles")
arbol_criaturas.in_order()
print("Fin punto H \n")

#I- Se debe permitir busqueda por coincidencia.
def busqueda_por_coincidencia(arbol_criaturas, texto):
    resultados = []

    def __buscar_coincidencia(root):
        if root is not None:
            if texto.lower() in root.value.lower():
                resultados.append(root.value)
            __buscar_coincidencia(root.left)
            __buscar_coincidencia(root.right)

    __buscar_coincidencia(arbol_criaturas.root)
    return resultados

print("Punto I: Búsqueda por coincidencia")
texto = input("Ingrese el texto para buscar coincidencias: ")
coincidencias = busqueda_por_coincidencia(arbol_criaturas, texto)
print(f"Criaturas que coinciden con '{texto}': {coincidencias}")
print("Fin punto I \n")

#J- Eliminar a Basilisco y Sirenas del árbol.
def eliminar_criatura(arbol_criaturas, nombre):
    deleted_value, other_values = arbol_criaturas.delete(nombre)
    if deleted_value is not None:
        print(f"Criatura {nombre} eliminada del árbol.")

print("Punto J: Eliminar a Basilisco y Sirenas del árbol")
criaturas_a_eliminar = ["Basilisco", "Sirenas"]
for criatura in criaturas_a_eliminar:
    eliminar_criatura(arbol_criaturas, criatura)
arbol_criaturas.in_order()
print("Fin punto J \n")

#K- Modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias.
def agregar_derrotas(arbol_criaturas, nombre, derrotado_por):
    root = arbol_criaturas.search(nombre)
    if root is not None:
        root.other_values['Derrotado por'] = derrotado_por

print("Punto K: Modificar el nodo de las Aves del Estínfalo, agregando que Heracles derroto a varias")
agregar_derrotas(arbol_criaturas, "Aves del Estínfalo", "Heracles")
arbol_criaturas.in_order()
print("Fin punto K \n")

#L- Modificar el nombre de la criatura Ladón por Dragón Ladón.
def modificar_nombre(arbol_criaturas, nombre_actual, nuevo_nombre):
    root = arbol_criaturas.search(nombre_actual)
    if root is not None:
        other_values = root.other_values
        arbol_criaturas.delete(nombre_actual)
        arbol_criaturas.insert(nuevo_nombre, other_values)

print("Punto L: Modificar el nombre de la criatura Ladón por Dragón Ladón")
modificar_nombre(arbol_criaturas, "Ladón", "Dragón Ladón")
arbol_criaturas.in_order()
print("Fin punto L \n")

#M- Realizar un listado por nivel del árbol.
print("Punto M: Listado por nivel del árbol")
arbol_criaturas.by_level()
print("Fin punto M \n")

#N- Mostrar las criaturas capturadas por Heracles.
def criaturas_capturadas_por(arbol_criaturas, nombre):
    criaturas = []

    def __buscar_capturadas(root):
        if root is not None:
            if root.other_values.get('capturado_por') == nombre:
                criaturas.append(root.value)
            __buscar_capturadas(root.left)
            __buscar_capturadas(root.right)

    __buscar_capturadas(arbol_criaturas.root)
    return criaturas

print("Punto N: Mostrar las criaturas capturadas por Heracles")
criaturas_capturadas = criaturas_capturadas_por(arbol_criaturas, "Heracles")
print(f"Criaturas capturadas por Heracles: {criaturas_capturadas}")
print("Fin punto N \n")