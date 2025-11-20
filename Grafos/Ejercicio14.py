from graph import Graph

g=Graph(is_directed=False)

habitaciones=[
    "cocina",
    "comedor",
    "Cochera",
    "Quincho",
    "Baño 1",
    "Baño 2",
    "Habitacion 1",
    "Habitacion 2",
    "Sala de estar",
    "Terraza",
    "Patio"
]

for habitacion in habitaciones:
    g.insert_vertex(habitacion)

#A- Cargar al menos tres aristas a cada vértice.
#Y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros.

print("Ejercicio A.")

aristas = [
    # NODO CENTRAL 1: Sala de estar (5 aristas)
    ("Sala de estar", "comedor", 5),      # Conexión 1
    ("Sala de estar", "Baño 1", 3),       # Conexión 2
    ("Sala de estar", "Habitacion 1", 4), # Conexión 3
    ("Sala de estar", "Habitacion 2", 4), # Conexión 4
    ("Sala de estar", "Terraza", 7),      # Conexión 5

    # NODO CENTRAL 2: Patio (5 aristas)
    ("Patio", "cocina", 5),    # Conexión 1
    ("Patio", "comedor", 6),   # Conexión 2
    ("Patio", "Cochera", 4),   # Conexión 3
    ("Patio", "Quincho", 5),   # Conexión 4
    ("Patio", "Terraza", 6),   # Conexión 5
    
    # cocina (ya tiene Patio, faltan 2)
    ("cocina", "comedor", 4),
    ("cocina", "Cochera", 8),

    # Cochera (ya tiene Patio y cocina, falta 1)
    ("Cochera", "Quincho", 3),

    # Quincho (ya tiene Patio y Cochera, falta 1)
    ("Quincho", "Terraza", 5),

    # Baño 1 (ya tiene Sala, faltan 2)
    ("Baño 1", "Habitacion 1", 2),
    ("Baño 1", "Habitacion 2", 2),

    # Baño 2 (necesita 3)
    ("Baño 2", "Habitacion 1", 3),
    ("Baño 2", "Habitacion 2", 3),
    ("Baño 2", "Terraza", 8)
]

for origen, destino, peso in aristas:
    g.insert_edge(origen, destino, peso)

g.show()

print ("\nFin Ejercicio A.")

#B- Obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes.
print("\nEjercicio B.")

expansion_minima = g.kruskal('Sala de estar')
print(expansion_minima)

peso_total = 0

for edge in expansion_minima.split(";"):
    origen, destino, peso = edge.split('-')
    peso_total += int(peso)

print(f"\n Los metros de cables necesarios para conectar todos los ambientes son: {peso_total} metros.")

print("\nFin Ejercicio B.")

#C- Determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar
# para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

print("\nEjercicio C.")

camino = g.dijkstra("Habitacion 1")
destino = 'Sala de estar'
peso_total = None
camino_completo = []
    
while camino.size() > 0:
    valor = camino.pop()
    if valor[0] == destino:
        if peso_total is None:
            peso_total = valor[1]
        camino_completo.append(valor[0])
        destino = valor[2]
camino_completo.reverse()

if peso_total is not None:
    print(f'\nEl camino desde Habitacion 1 hasta Sala de estar pasa por estos lugares. [{" --> ".join(camino_completo)}] (Tuvo un costo de: {peso_total} metros)')
else:
    print('No hay/no se encontro un camino desde Habitacion 1 hasta Sala de estar.')

print("\nFin Ejercicio C.")