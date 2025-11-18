from graph import Graph

g = Graph(is_directed=False)

#C- cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
print("Ejercicio A.")
personajes = [
    "Luke Skywalker",
    "Darth Vader",
    "Yoda",
    "Boba Fett",
    "C-3PO", 
    "Leia",
    "Rey",
    "Kylo Ren",
    "Chewbacca",
    "Han Solo",
    "R2-D2",
    "BB-8"
]

for personaje in personajes:
    g.insert_vertex(personaje)

#A- Cada vértice debe almacenar el nombre de un personaje.
#   Las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan.
g.insert_edge("BB-8", "C-3PO", 3)
g.insert_edge("BB-8", "R2-D2", 2)

g.insert_edge("C-3PO", "R2-D2", 9)

g.insert_edge("Darth Vader", "Boba Fett", 2)

g.insert_edge("Han Solo", "Boba Fett", 2)
g.insert_edge("Han Solo", "Chewbacca", 4)

g.insert_edge("Kylo Ren", "Chewbacca", 2)
g.insert_edge("Kylo Ren", "Han Solo", 1)

g.insert_edge("Leia", "Chewbacca", 4)
g.insert_edge("Leia", "Han Solo", 4)

g.insert_edge("Luke Skywalker", "Chewbacca", 3)
g.insert_edge("Luke Skywalker", "Darth Vader", 3)
g.insert_edge("Luke Skywalker", "Han Solo", 3)
g.insert_edge("Luke Skywalker", "Leia", 4)
g.insert_edge("Luke Skywalker", "Yoda", 3)

g.insert_edge("Rey", "BB-8", 3)
g.insert_edge("Rey", "Chewbacca", 3)
g.insert_edge("Rey", "Kylo Ren", 3)
g.insert_edge("Rey", "Leia", 3)
g.insert_edge("Rey", "R2-D2", 2)

g.insert_edge("Yoda", "Darth Vader", 2)

print("Ejercicio Realizado en el codigo.")
print("Fin Ejercicio A.")

#B- Hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia.
print("\nEjercicio B.")

print("AEM de C-3PO:")
print(g.kruskal('C-3PO'))

print("\nAEM de Yoda:")
print(g.kruskal('Yoda'))

print("\nAEM de Leia:")
print(g.kruskal('Leia'))

print("\nFin Ejercicio B.")

#C- Determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número.

epis_max = 0
pairs = []

for vertex in g:
    for edge in vertex.edges:
        if edge.weight > epis_max:
            epis_max = edge.weight
            pairs = [(vertex, edge)]
        elif edge.weight == epis_max:
                pairs.append((vertex,edge))
print("\nEjercicio C.")
print(f"El número máximo de episodios (peso) compartido es: {epis_max}")
print("\nPares de personajes que coinciden con el máximo:")

for one, two in pairs:
    print(f"- {one.value} y {two.value}")

print("\nFin Ejercicio C.")

#E- Calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader.

def mostrar_camino_corto(g, origin, destiny):
    path = g.dijkstra(origin)
    total_weight = None
    full_path = []
    current_destiny = destiny
    
    while path.size() > 0:
        value = path.pop()
        if value[0] == current_destiny:
            if total_weight is None:
                total_weight = value[1]
            full_path.append(value[0])
            current_destiny = value[2]
    
    full_path.reverse()
    print(f'{" - ".join(full_path)} pasando por un total de {total_weight} caminos')

print("\nEjercicio E.")

mostrar_camino_corto(g, "C-3PO", "R2-D2")
mostrar_camino_corto(g, "Yoda", "Darth Vader")

print("\nFin ejercicio E.")

#F- Indicar qué personajes aparecieron en los nueve episodios de la saga.

found = []
for vertex in g:
    for edge in vertex.edges:
        if edge.weight == 9:
            if vertex.value not in found:
                found.append(vertex.value)

            if edge.value not in found:
                found.append(edge.value)

print("\nEjercicio F.")

print(f"f) Personajes que aparecieron en los nueve episodios de la saga: {found}")

print("\nFin ejercicio F.")
