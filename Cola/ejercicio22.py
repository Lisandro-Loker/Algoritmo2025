from collections import deque

class PersonajeMCU:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

    def __str__(self):
        return f"{{ {self.nombre_personaje}, {self.nombre_superheroe}, {self.genero} }}"

cola_mcu = deque()
cola_mcu.append(PersonajeMCU("Tony Stark", "Iron Man", "M"))
cola_mcu.append(PersonajeMCU("Steve Rogers", "Capitán América", "M"))
cola_mcu.append(PersonajeMCU("Natasha Romanoff", "Black Widow", "F"))
cola_mcu.append(PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"))
cola_mcu.append(PersonajeMCU("Scott Lang", "Ant-Man", "M"))
cola_mcu.append(PersonajeMCU("Wanda Maximoff", "Bruja Escarlata", "F"))
cola_mcu.append(PersonajeMCU("Peter Parker", "Spider-Man", "M"))
cola_mcu.append(PersonajeMCU("Gamora", "", "F"))
cola_mcu.append(PersonajeMCU("Stephen Strange", "Doctor Strange", "M"))
cola_mcu.append(PersonajeMCU("Bucky Barnes", "Soldado del Invierno", "M"))
cola_mcu.append(PersonajeMCU("Sam Wilson", "Falcon", "M"))
cola_mcu.append(PersonajeMCU("Sharon Carter", "Agente 13", "F"))

def obtener_personaje_capitana_marvel(cola):
    cola_auxiliar = deque(cola)
    while cola_auxiliar:
        personaje = cola_auxiliar.popleft()
        if personaje.nombre_superheroe == "Capitana Marvel":
            return personaje.nombre_personaje
    return None

personaje_capitana_marvel = obtener_personaje_capitana_marvel(cola_mcu)
print(f"a. El personaje de Capitana Marvel es: {personaje_capitana_marvel}")

def mostrar_superheroes_femeninos(cola):
    superheroes_femeninos = []
    cola_auxiliar = deque(cola)
    while cola_auxiliar:
        personaje = cola_auxiliar.popleft()
        if personaje.genero == "F" and personaje.nombre_superheroe:
            superheroes_femeninos.append(personaje.nombre_superheroe)
    return superheroes_femeninos

nombres_superheroes_femeninos = mostrar_superheroes_femeninos(cola_mcu)
print(f"\nb. Nombres de los superhéroes femeninos: {nombres_superheroes_femeninos}")

def mostrar_personajes_masculinos(cola):
    personajes_masculinos = []
    cola_auxiliar = deque(cola)
    while cola_auxiliar:
        personaje = cola_auxiliar.popleft()
        if personaje.genero == "M":
            personajes_masculinos.append(personaje.nombre_personaje)
    return personajes_masculinos

nombres_personajes_masculinos = mostrar_personajes_masculinos(cola_mcu)
print(f"\nc. Nombres de los personajes masculinos: {nombres_personajes_masculinos}")

def obtener_superheroe_scott_lang(cola):
    cola_auxiliar = deque(cola)
    while cola_auxiliar:
        personaje = cola_auxiliar.popleft()
        if personaje.nombre_personaje == "Scott Lang":
            return personaje.nombre_superheroe
    return None

superheroe_scott_lang = obtener_superheroe_scott_lang(cola_mcu)
print(f"\nd. El superhéroe de Scott Lang es: {superheroe_scott_lang}")

def mostrar_personajes_con_s(cola):
    personajes_con_s = []
    cola_auxiliar = deque(cola)
    while cola_auxiliar:
        personaje = cola_auxiliar.popleft()
        if personaje.nombre_personaje.startswith("S") or personaje.nombre_superheroe.startswith("S"):
            personajes_con_s.append(str(personaje))
    return personajes_con_s

datos_personajes_con_s = mostrar_personajes_con_s(cola_mcu)
print(f"\ne. Datos de los personajes cuyos nombres comienzan con 'S': {datos_personajes_con_s}")

def verificar_carol_danvers(cola):
    cola_auxiliar = deque(cola)
    while cola_auxiliar:
        personaje = cola_auxiliar.popleft()
        if personaje.nombre_personaje == "Carol Danvers":
            return True, personaje.nombre_superheroe
    return False, None

existe_carol, superheroe_carol = verificar_carol_danvers(cola_mcu)
if existe_carol:
    print(f"\nf. Carol Danvers se encuentra en la cola y su superhéroe es: {superheroe_carol}")
else:
    print("f. Carol Danvers no se encuentra en la cola.")