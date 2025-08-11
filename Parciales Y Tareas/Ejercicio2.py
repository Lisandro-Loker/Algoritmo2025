from super_heroes_data import superheroes
from queue import Queue
from lista import List

class Personaje:
    def __init__(self, name, alias, real_name, first_appearance, short_bio=None, is_villain=False):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"Nombre: {self.name}\n Apodo: {self.alias}\n Nombre real: {self.real_name}\n Bio: {self.short_bio}\n Año de aparición: {self.first_appearance}\n Afiliación: {self.is_villain}\n\n"
    
def ordenados_por_nombre(ord):
    return ord.name

def ordenados_por_nombre_real(ord):
    return ord.real_name if ord.real_name is not None else ""

def ordenados_por_aparición(ord):
    return ord.first_appearance

lista_personaje = List (
    [
        Personaje(
            name = hero["name"],
            alias = hero["alias"],
            real_name = hero["real_name"],
            short_bio = hero["short_bio"],
            first_appearance = hero["first_appearance"],
            is_villain = hero["is_villain"],
        )
        for hero in superheroes
    ]
)

# Punto A
lista_personaje.add_criterion("name", ordenados_por_nombre)

print("Personajes ordenados por su nombre:")
lista_personaje.sort_by_criterion("name")
lista_personaje.show
print("")

#Punto B
posición_thing= lista_personaje.search("The Thing", "name")
posición_Rocket= lista_personaje.search("Rocket Racoon", "name")

print("Aqui esta la posicion de The thing")
print(posición_thing)
print("Aqui esta la posicion de Rocket")
print(posición_Rocket)
print("")

# Punto C

villanos = List()

for c in lista_personaje:
    if c.is_villain:
        villanos.append(c)

print("Los villanos que hay:")
villanos.show()
print("")

# Punto D

q_villanos = Queue()

for d in villanos:
    q_villanos.arrive(d)

print("Los villanos que aparecen antes de 1980:")
while q_villanos.size() > 0:
    villanos = q_villanos.attention()

    if villanos.first_appearance < 1980:
        print(f"Nombre del villano: {villanos.name}\n Primera aparición: {villanos.first_appearance}\n")

# Punto E

iniciales = ("Bl", "g", "My", "W")

personajes_segun_iniciales = List()
for e in lista_personaje:
    if e.name.startswith(iniciales):
        personajes_segun_iniciales.append(e)

print("Personajes que empiezan con las iniciales dadas:")
personajes_segun_iniciales.show()
print("")

# Punto F

lista_personaje.add_criterion("real_name", ordenados_por_nombre_real)

print("Personajes ordenados por su nombre Real:")
lista_personaje.sort_by_criterion("real_name")
lista_personaje.show()
print("")

#Punto G

lista_personaje.add_criterion("first_appearance", ordenados_por_aparición)

print("Personajes ordenados por su fecha de aparición;")
lista_personaje.sort_by_criterion("first_appearance")
lista_personaje.show()
print("")

#Punto H

antman = lista_personaje.search("Ant Man", "name")
if antman is not "":
    lista_personaje[antman].real_name = "Scott Lang"

#Punto I

print("Personajes que incluyan en su BIO la palabra Time-Traveling o Suit")
for y in lista_personaje:
    bio = y.short_bio.lower()
    if ("time-traveling" or "suit") in bio:
        print(f"Nombre: {y.name}")

print("")

#Punto J

lista_de_eliminados = List()
eliminar = ["Electro", "Baron Zemo"]
for name in eliminar:
    posicion = lista_personaje.search(name, "name")
    
    if posicion is not "":
        eliminado = lista_personaje.pop(posicion)
        lista_de_eliminados.append(eliminado)

for j in lista_de_eliminados:
    print(f"Eliminado:\n{j}")

    