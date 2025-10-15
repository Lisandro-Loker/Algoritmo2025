from lista_jedis import jedis_data
from list_ import List

def order_by_name(item):
    return item.nombre
def order_by_species(item):
    return item.especie

class Jedi:
    
    def __init__(self, nombre, maestro, sable_luz, especie):
        self.nombre = nombre
        self.maestro = maestro
        self.sable_luz = sable_luz
        self.especie = especie

    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Maestro: {self.maestro}\n"
            f"Sable de Luz: {', '.join(self.sable_luz)}\n"
            f"Especie: {self.especie}\n"
        )
    
jedis_lista = List()
jedis_lista.add_criterion('nombre', order_by_name)
jedis_lista.add_criterion('especie', order_by_species)

for datos in jedis_data:
    jedi = Jedi(
        datos['nombre'],
        datos['maestro'],
        datos['sable_luz'],
        datos['especie']
    )
    jedis_lista.append(jedi)

#A- Listado ordenado por nombre y especie
def order_by_name_and_species(item):
    return (item.nombre, item.especie)
#Añado un nuevo criterio a la lista, ordenar por nombre y especie

jedis_lista.add_criterion('nombre_especie', order_by_name_and_species)
print("Punto A")
print("Listado ordenado por nombre y especie:")
jedis_lista.sort_by_criterion('nombre_especie')
jedis_lista.show()
print("Fin punto A\n")

#B- Mostrar toda la información de Asoka Tano y kit fisto
def mostrar_info_jedi(lista, nombre):
    index = lista.search(nombre, 'nombre')
    if index is not None:
        print(f"Información de {nombre}:\n{lista[index]}")
    else:
        print(f"{nombre} no encontrado en la lista.")
print("Punto B")
mostrar_info_jedi(jedis_lista, 'Ahsoka Tano')
mostrar_info_jedi(jedis_lista, 'Kit Fisto')
print("Fin punto B\n")

#C- Mostrar todos los padawans de Yoda y luke skywalker
def mostrar_padawans(lista, maestro):
    print(f"Padawans de {maestro}:")
    encontrados = 0
    for jedi in lista:
        if maestro in jedi.maestro:
            print(jedi.nombre)
            encontrados += 1
    if encontrados == 0:
        print(f"No se encontraron padawans de {maestro}.")
    print()
    
print("Punto C")
mostrar_padawans(jedis_lista, 'Yoda')
mostrar_padawans(jedis_lista, 'Luke Skywalker')
print("Fin punto C\n")

#D- Mostrar los jedis de especie humana y twi'lek
def mostrar_jedis_por_especie(lista, especie):
    print(f"Jedis de especie {especie}:")
    for jedi in lista:
        if jedi.especie.lower() == especie.lower():
            print(jedi.nombre)
    print()

print("Punto D")
mostrar_jedis_por_especie(jedis_lista, 'Humano')
mostrar_jedis_por_especie(jedis_lista, 'Twi´lek')
print("Fin punto D\n")


#E- Listar los jedis que comienzan con A
def listar_jedis_por_letra(lista):
    for jedi in lista:
        if jedi.nombre.startswith('A'):
            print(jedi.nombre)

print("Punto E")
print("Jedis que comienzan con la letra A:")
listar_jedis_por_letra(jedis_lista)
print("Fin punto E\n")


#F- Mostrar los jedis que usaron un sable de luz de mas de un color
def mostrar_jedis_sable_multiple(lista):
    print("Jedis con sables de luz de más de un color:")
    for jedi in lista:
        if len(jedi.sable_luz) > 1:
            print(f"{jedi.nombre}: {', '.join(jedi.sable_luz)}")
    print()

print("Punto F")
mostrar_jedis_sable_multiple(jedis_lista)
print("Fin punto F\n")

#G- Mostrar los jedis que utilizaron sable de luz amarillo o violeta
def mostrar_jedis_por_sable(lista, colores):
    print(f"Jedis con sable de luz {', '.join(colores)}:")
    for jedi in lista:
        if any(color in jedi.sable_luz for color in colores):
            print(jedi.nombre)
    print()

print("Punto F")
mostrar_jedis_por_sable(jedis_lista, ['Amarillo', 'Violeta'])
print("Fin punto F\n")

#H- Mostrar los nombres de los padawans de Qui-Gon Jinn y Mace Windu, si tuvieron
print("Punto H")
mostrar_padawans(jedis_lista, 'Qui-Gon Jinn')
mostrar_padawans(jedis_lista, 'Mace Windu')
print("Fin punto H\n")

