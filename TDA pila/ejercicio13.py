class Traje:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f"Modelo: {self.modelo}, Película: {self.pelicula}, Estado: {self.estado}"

class PilaTrajes:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return not self.items

    def apilar(self, traje):
        self.items.append(traje)

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

    def mostrar_pila(self):
        for traje in reversed(self.items):
            print(traje)

pila_iron_man = PilaTrajes()

pila_iron_man.apilar(Traje("Mark I", "Iron Man", "Dañado"))
pila_iron_man.apilar(Traje("Mark III", "Iron Man", "Impecable"))
pila_iron_man.apilar(Traje("Mark XLII", "Iron Man 3", "Dañado"))
pila_iron_man.apilar(Traje("Mark XLIV (Hulkbuster)", "Avengers: Age of Ultron", "Dañado"))
pila_iron_man.apilar(Traje("Mark XLVI", "Capitan America: Civil War", "Dañado"))
pila_iron_man.apilar(Traje("Mark XLVII", "Spider-Man: Homecoming", "Impecable"))
pila_iron_man.apilar(Traje("Mark L", "Avengers: Infinity War", "Destruido"))
pila_iron_man.apilar(Traje("Mark LXXXV", "Avengers: Endgame", "Dañado"))
pila_iron_man.apilar(Traje("Mark XLIV (Hulkbuster)", "Avengers: Infinity War", "Destruido"))
pila_iron_man.apilar(Traje("Mark XLVII", "Capitan America: Civil War", "Dañado"))

def buscar_hulkbuster(pila):
    peliculas_hulkbuster = []
    pila_auxiliar = PilaTrajes()
    encontrado = False
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje.modelo == "Mark XLIV (Hulkbuster)":
            encontrado = True
            if traje.pelicula not in peliculas_hulkbuster:
                peliculas_hulkbuster.append(traje.pelicula)
        pila_auxiliar.apilar(traje)
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

    if encontrado:
        print("El modelo Mark XLIV (Hulkbuster) fue utilizado en las siguientes películas:")
        for pelicula in peliculas_hulkbuster:
            print(f"- {pelicula}")
    else:
        print("El modelo Mark XLIV (Hulkbuster) no se encontró en la pila.")

buscar_hulkbuster(pila_iron_man)

def mostrar_trajes_danados(pila):
    print("\nModelos de trajes dañados:")
    pila_auxiliar = PilaTrajes()
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje.estado == "Dañado":
            print(f"- {traje.modelo} (en {traje.pelicula})")
        pila_auxiliar.apilar(traje)
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

mostrar_trajes_danados(pila_iron_man)

def eliminar_trajes_destruidos(pila):
    print("\nEliminando trajes destruidos:")
    pila_auxiliar = PilaTrajes()
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje.estado == "Destruido":
            print(f"- {traje.modelo} (de {traje.pelicula}) fue destruido.")
        else:
            pila_auxiliar.apilar(traje)
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

eliminar_trajes_destruidos(pila_iron_man)

def agregar_traje(pila, nuevo_traje):
    pila_auxiliar = PilaTrajes()
    existe = False
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje.modelo == nuevo_traje.modelo and traje.pelicula == nuevo_traje.pelicula:
            existe = True
        pila_auxiliar.apilar(traje)
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

    if not existe:
        pila.apilar(nuevo_traje)
        print(f"\nEl traje {nuevo_traje.modelo} de la película {nuevo_traje.pelicula} ha sido agregado.")
    else:
        print(f"\nEl traje {nuevo_traje.modelo} ya existe en la película {nuevo_traje.pelicula}.")

agregar_traje(pila_iron_man, Traje("Mark LXXXV", "Avengers: Endgame", "Impecable"))
agregar_traje(pila_iron_man, Traje("Mark V", "Iron Man 2", "Dañado"))

def mostrar_trajes_por_pelicula(pila, pelicula):
    print(f"\nTrajes utilizados en '{pelicula}':")
    pila_auxiliar = PilaTrajes()
    encontrados = False
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje.pelicula == pelicula:
            print(f"- {traje.modelo}")
            encontrados = True
        pila_auxiliar.apilar(traje)
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

    if not encontrados:
        print("No se encontraron trajes para esta película.")

mostrar_trajes_por_pelicula(pila_iron_man, "Spider-Man: Homecoming")
mostrar_trajes_por_pelicula(pila_iron_man, "Capitan America: Civil War")