from graph import Graph
import math

g = Graph(is_directed=False)

#A-  ada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora.

print("Ejercicio A.")

esquema_red = [
        ("Red Hat", "Notebook"), 
        ("Debian", "Notebook"), 
        ("Arch", "Notebook"),
        ("Manjaro", "PC"), 
        ("Parrot", "PC"), 
        ("Fedora", "PC"),
        ("Ubuntu", "PC"), 
        ("Mint", "PC"),
        ("Guaraní", "Servidor"), 
        ("MongoDB", "Servidor"),
        ("Switch 1", "Switch"), 
        ("Switch 2", "Switch"),
        ("Router 1", "Router"), 
        ("Router 2", "Router"), 
        ("Router 3", "Router"),
        ("Impresora", "Impresora")
]

for dato, tipo in esquema_red:
    g.insert_vertex(dato)

esquema_data = [
        ('Red Hat', 'Router 2', 25),
        ('Debian', 'Switch 1', 17),
        ('Ubuntu', 'Switch 1', 18),
        ('Impresora', 'Switch 1', 22),
        ('Mint', 'Switch 1', 80),
        ('Switch 1', 'Router 1', 29),
        ('Router 1', 'Router 2', 37),
        ('Router 1', 'Router 3', 43),
        ('Router 2', 'Guaraní', 9),
        ('Router 2', 'Router 3', 50),
        ('Router 3', 'Switch 2', 61),
        ('Switch 2', 'Manjaro', 40),
        ('Switch 2', 'Parrot', 12),
        ('Switch 2', 'Fedora', 3),
        ('Switch 2', 'Arch', 56),
        ('Switch 2', 'MongoDB', 5)
]

for origen, destino, peso in esquema_data:
    g.insert_edge(origen, destino, peso)

print("Esquema de red cargado.")
g.show()

print("\nFin Ejercicio A.")

#B- Realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch.

print("\nEjercicio B.")

def ejecutar_barridos(nombre_notebook):
    
    print(f"\nBarrido en Profundidad desde {nombre_notebook}")
    g.deep_sweep(nombre_notebook)
    
    print(f"\nBarrido en Amplitud desde {nombre_notebook}")
    g.amplitude_sweep(nombre_notebook)  

notebooks_a_probar = ["Red Hat", "Debian", "Arch"]

for notebook in notebooks_a_probar:
    ejecutar_barridos(notebook)

print("\nFin Ejercicio B.")

#C- Encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora.

print ("\nEjercicio C.")

pcs = ["Manjaro", "Red Hat", "Fedora"]
for pc in pcs:
    path = g.dijkstra(pc)
    destination = 'Impresora'
    peso_total = None
    camino_completo = []
    
    while path.size() > 0:
        value = path.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]
    camino_completo.reverse()

    if peso_total is not None and peso_total is not math.inf:
        print(f'Camino desde {pc}: {" -> ".join(camino_completo)} (Costo: {peso_total})')
    else:
        print(f'No se encontró camino desde {pc} a la Impresora.')

print("\nFin Ejercicio C.")

#-D Encontrar el árbol de expansión mínima.