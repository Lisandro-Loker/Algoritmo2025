from lista_superheroes import superheroes
from list_ import List

def order_by_name(item):
    return item.nombre

class Superheroe:
    
    def __init__(self, nombre, aparicion, casa, biografia):
        self.nombre = nombre
        self.aparicion = aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Aparición: {self.aparicion}\n"
            f"Casa: {self.casa}\n"
            f"Biografía: {self.biografia}\n"
        )
        
superheroes_lista = List()
superheroes_lista.add_criterion('nombre', order_by_name)

for datos in superheroes:
    heroe = Superheroe(
        datos['nombre'],
        datos['aparicion'],
        datos['casa'],
        datos['biografia']
    )
    superheroes_lista.append(heroe)

# A- Eliminar a linterna verde de la lista

def eliminar_linterna_verde(lista):
    lista.delete_value('Linterna Verde', 'nombre')

print("Punto A")
eliminar_linterna_verde(superheroes_lista)
print("Lista de heroes sin linterna verde:")
superheroes_lista.show()
print("Fin punto A\n")

#B- Mostrar el año de aparición de Wolverine
def mostrar_ano_wolverine(lista):
    index = lista.search('Wolverine', 'nombre')
    if index is not None:
        print(f"Año de aparición de Wolverine: {lista[index].aparicion}")
    else:
        print("Wolverine no encontrado en la lista.")

print("Punto B")
mostrar_ano_wolverine(superheroes_lista)
print("Fin punto B\n")

#C- Cambiar la casa de Dr Strange a Marvel
def cambiar_casa_dr_strange(lista):
    index = lista.search('Doctor Strange', 'nombre')
    if index is not None:
        lista[index].casa = 'Marvel'
        print("Casa de Doctor Strange cambiada a Marvel.")
    else:
        print("Doctor Strange no encontrado en la lista.")

print("Punto C")
cambiar_casa_dr_strange(superheroes_lista)
print("Datos de Doctor Strange después del cambio:")
index = superheroes_lista.search('Doctor Strange', 'nombre')
if index is not None:
    print(superheroes_lista[index])
print("Fin punto C\n")

#D- mostrar el nombre de los superheroes que en la biografia mencionen la palabra "traje" o "armadura"
def mostrar_heroes_con_traje_o_armadura(lista):
    print("Superhéroes que mencionan 'traje' o 'armadura' en su biografía:")
    for heroe in lista:
        if 'traje' in heroe.biografia.lower() or 'armadura' in heroe.biografia.lower():
            print(heroe.nombre)

print("Punto D")
mostrar_heroes_con_traje_o_armadura(superheroes_lista)
print("Fin punto D\n")

#E- mostrar el nombre y la casa de los superheroes que hayan aparecido antes de 1963
def mostrar_heroes_antes_de_1963(lista):
    print("Superhéroes que aparecieron antes de 1963:")
    for heroe in lista:
        if heroe.aparicion < 1963:
            print(f"Nombre: {heroe.nombre}, Casa: {heroe.casa}")

print("Punto E")
mostrar_heroes_antes_de_1963(superheroes_lista)
print("Fin punto E\n")

#F- Mostrar la casa a la que pertenecen la capitana marvel y mujer maravilla
def mostrar_casa_especificas(lista):
    for nombre in ['Capitana Marvel', 'Mujer Maravilla']:
        index = lista.search(nombre, 'nombre')
        if index is not None:
            print(f"{nombre} pertenece a la casa: {lista[index].casa}")
        else:
            print(f"{nombre} no encontrado en la lista.")

print("Punto F")
mostrar_casa_especificas(superheroes_lista)
print("Fin punto F\n")

#G- Mostrar toda la información de Flash y de Star-Lord
def mostrar_info_especificas(lista):
    for nombre in ['Flash', 'Star-Lord']:
        index = lista.search(nombre, 'nombre')
        if index is not None:
            print(f"Información de {nombre}:\n{lista[index]}")
        else:
            print(f"{nombre} no encontrado en la lista.")

print("Punto G")
mostrar_info_especificas(superheroes_lista)
print("Fin punto G\n")

#H- Listar los superheroes que comiencen con la letra B, M y S.
def listar_heroes_por_letra(lista):
    for hero in lista:
        if hero.nombre.startswith(('B', 'M', 'S')):
            print(hero.nombre)

print("Punto H")
listar_heroes_por_letra(superheroes_lista)
print("Fin punto H\n")

#I- Determinar cuantos superheroes hay de cada casa (Marvel y DC)
def contar_heroes_por_casa(lista):
    conteo = {'Marvel': 0, 'DC': 0}
    for heroe in lista:
        if heroe.casa == 'Marvel':
            conteo['Marvel'] += 1
        if heroe.casa == 'DC':
            conteo['DC'] += 1
    print(f"Cantidad de superhéroes de Marvel: {conteo['Marvel']}")
    print(f"Cantidad de superhéroes de DC: {conteo['DC']}")
    return conteo
print("Punto I")
contar_heroes_por_casa(superheroes_lista)
print("Fin punto I\n")