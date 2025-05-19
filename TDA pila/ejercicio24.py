class PersonajeMCU:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

    def __str__(self):
        return f"Nombre: {self.nombre}, Películas: {self.cantidad_peliculas}"

class PilaPersonajes:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return not self.items

    def apilar(self, personaje):
        self.items.append(personaje)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def tamanio(self):
        return len(self.items)

pila_mcu = PilaPersonajes()

pila_mcu.apilar(PersonajeMCU("Iron Man", 10))
pila_mcu.apilar(PersonajeMCU("Capitán América", 9))
pila_mcu.apilar(PersonajeMCU("Thor", 8))
pila_mcu.apilar(PersonajeMCU("Hulk", 5))
pila_mcu.apilar(PersonajeMCU("Viuda Negra", 8))
pila_mcu.apilar(PersonajeMCU("Spider-Man", 6))
pila_mcu.apilar(PersonajeMCU("Doctor Strange", 4))
pila_mcu.apilar(PersonajeMCU("Guardianes de la Galaxia", 3))
pila_mcu.apilar(PersonajeMCU("Rocket Raccoon", 7))
pila_mcu.apilar(PersonajeMCU("Groot", 6))
pila_mcu.apilar(PersonajeMCU("Capitana Marvel", 3))
pila_mcu.apilar(PersonajeMCU("Ant-Man", 4))
pila_mcu.apilar(PersonajeMCU("Drax", 4))
pila_mcu.apilar(PersonajeMCU("Gamora", 4))

def encontrar_posicion_personajes(pila, nombre1, nombre2):
    pila_auxiliar = PilaPersonajes()
    posicion1 = -1
    posicion2 = -1
    posicion_actual = 1

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje.nombre == nombre1 and posicion1 == -1:
            posicion1 = posicion_actual
        if personaje.nombre == nombre2 and posicion2 == -1:
            posicion2 = posicion_actual
        pila_auxiliar.apilar(personaje)
        posicion_actual += 1

    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

    if posicion1 != -1:
        print(f"{nombre1} se encuentra en la posición: {posicion1}")
    else:
        print(f"{nombre1} no se encontró en la pila.")

    if posicion2 != -1:
        print(f"{nombre2} se encuentra en la posición: {posicion2}")
    else:
        print(f"{nombre2} no se encontró en la pila.")

encontrar_posicion_personajes(pila_mcu, "Rocket Raccoon", "Groot")

def personajes_mas_de_5_peliculas(pila):
    print("\nPersonajes que participaron en más de 5 películas:")
    pila_auxiliar = PilaPersonajes()
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje.cantidad_peliculas > 5:
            print(f"- {personaje.nombre}: {personaje.cantidad_peliculas} películas")
        pila_auxiliar.apilar(personaje)
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

personajes_mas_de_5_peliculas(pila_mcu)

def cantidad_peliculas_personaje(pila, nombre_personaje):
    pila_auxiliar = PilaPersonajes()
    cantidad = 0
    encontrado = False
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje.nombre == nombre_personaje:
            cantidad = personaje.cantidad_peliculas
            encontrado = True
        pila_auxiliar.apilar(personaje)
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

    if encontrado:
        print(f"\nViuda Negra (Black Widow) participó en {cantidad} películas.")
    else:
        print(f"\nViuda Negra (Black Widow) no se encontró en la pila.")

cantidad_peliculas_personaje(pila_mcu, "Viuda Negra")

def personajes_con_letras(pila, letras):
    print(f"\nPersonajes cuyos nombres empiezan con {', '.join(letras)}:")
    pila_auxiliar = PilaPersonajes()
    letras_minusculas = [letra.lower() for letra in letras]
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje.nombre[0].lower() in letras_minusculas:
            print(f"- {personaje.nombre}")
        pila_auxiliar.apilar(personaje)
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

letras_a_buscar = ["C", "D", "G"]
personajes_con_letras(pila_mcu, letras_a_buscar)