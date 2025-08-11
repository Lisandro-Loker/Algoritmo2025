from list__ import List
from super_heroes_data_ import superheroes

lista = List()
#se crea la clase personaje
class Personaje:
    def __init__(self, name, apodo, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.apodo = apodo
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
            return f"Nombre: {self.name} - Apodo: {self.apodo} - Nombre real: {self.real_name} - Bio: {self.short_bio} - Año de aparición: {self.first_appearance} - Tipo: {self.is_villain}"

#se pasan los personajes de la lista importada superheores (la del profe)
for superhero in superheroes:
    hero = Personaje(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    lista.append(hero)
#se define el criterio para la busqueda u ordenamiento
def criterioNombre(personaje):
     return personaje.nombre

#se añade el criterio a la lista 
lista.add_criterion("nombre", criterioNombre)

#se hace una funcion para ordenar, aunque no hace falta como tal.
def ordenarNombre():
    lista.sort_by_criterion("nombre")

#se llama a la funcion que ordena y se muestra abajo.
ordenarNombre()
lista.show() #lista ordenada por nombre

#como mencioné antes, podes ordenar sin la funcion así:
#lista.sort_by_criterion("nombre")
#es decir, llamando directamente al método para ordenar.
     