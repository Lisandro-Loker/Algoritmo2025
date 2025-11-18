from pokemon_data import pokemon_list
from tree import BinaryTree

#A- Cargar 3 arboles diferentes segun "Numero", "Nombre" y "Tipo".

arbol_pokemon_numero = BinaryTree()
arbol_pokemon_nombre = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in pokemon_list:
    arbol_pokemon_nombre.insert(pokemon['nombre'], pokemon)

for pokemon in pokemon_list:
    arbol_pokemon_numero.insert(pokemon['numero'], pokemon)

for pokemon in pokemon_list:
    for tipo in pokemon['tipos']:
        
        nodo_tipo = arbol_tipo.search(tipo)
        
        if nodo_tipo is None:
            arbol_tipo.insert(tipo, [pokemon])
        else:
            nodo_tipo.other_values.append(pokemon)

#B- Mostrar todos los datos de un Pokemon a partir de su número y nombre (El nombre se busca con proximidad).

def buscar_por_numero(arbol_numeros, numero):   
    print(f"\n--- Buscando Pokémon N° {numero} ---")
    nodo = arbol_numeros.search(numero)
    
    if nodo:
        print("Resultado (Datos completos):")
        print(nodo.other_values)
    else:
        print(f"No se encontró ningún Pokémon con el número {numero}.")

#Modifico el proximity search para que me sirva en este ejercicio.
def buscar_por_nombre(arbol_nombres, texto_busqueda):
    """
    Busca Pokémon por proximidad en el nombre.
    """
    print(f"\nBuscando Pokémon por proximidad de nombre: '{texto_busqueda}'")
    nodos_encontrados = arbol_nombres.proximity_search_nombre(texto_busqueda)
    
    if nodos_encontrados:
        print(f"Se encontraron {len(nodos_encontrados)} coincidencias:")
        for nodo in nodos_encontrados:
            pokemon_data = nodo.other_values
            print(f"  -> {pokemon_data['nombre']} (N° {pokemon_data['numero']})")
    else:
        print(f"No se encontró ningún Pokémon coincidente con '{texto_busqueda}'.")

print("Ejercicio B.")
print("Empezamos con la busqueda por numero.")
try:
    numero_ingresado = input("Introduce el NÚMERO del Pokémon a buscar: ")
    numero_a_buscar = int(numero_ingresado)
    buscar_por_numero(arbol_pokemon_numero, numero_a_buscar)

except ValueError:
    print(f"Error: '{numero_ingresado}' no es un número válido. Se omitirá la búsqueda por número.")

print("\nAhora la busqueda por nombre.")
nombre_ingresado = input("Introduce el NOMBRE (o parte del nombre) del Pokémon a buscar: ").strip()

if nombre_ingresado:
    buscar_por_nombre(arbol_pokemon_nombre, nombre_ingresado)
else:
    print("No se ingresó ningún nombre. Se omitirá la búsqueda por nombre.")

print("\nFin Ejercicio B.")

#C- Mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico.

def mostrar_pokemons_por_tipo(arbol_tipos, tipo_a_buscar):
    print(f"\n--- Pokémon de Tipo '{tipo_a_buscar}' ---")
    
    nodo_resultado = arbol_tipos.search(tipo_a_buscar)
    
    if nodo_resultado:
        lista_de_pokemon = nodo_resultado.other_values
        
        print(f"Se encontraron {len(lista_de_pokemon)} Pokémon:")
        
        nombres = [p['nombre'] for p in lista_de_pokemon]
        
        for nombre in nombres:
            print(f"  - {nombre}")
            
    else:
        print(f"No se encontraron Pokémon del tipo '{tipo_a_buscar}'.")

print("\nEjercicio C.")

tipos_solicitados = ['Fantasma', 'Fuego', 'Acero', 'Eléctrico']

for tipo in tipos_solicitados:
    mostrar_pokemons_por_tipo(arbol_tipo, tipo)

print("\nFin Ejercicio C.")

#D- Realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre.
print("\nEjercicio D.")
print("Listado Ascendente por NÚMERO")
listado_numeros_ascendente = arbol_pokemon_numero.in_order()
print(listado_numeros_ascendente)

print("\nListado Ascendente por NOMBRE")
listado_nombres_ascendente = arbol_pokemon_nombre.in_order()
print(listado_nombres_ascendente)

print("\nListado por NIVEL por NOMBRE")
listado_nombres_nivel = arbol_pokemon_nombre.by_level()
print(listado_nombres_nivel)

print("\nFin Ejercicio D.")

#E- mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum.
print("\nEjercicio E.")
def tipo_por_nombre(arbol_nombres, nombre_exacto):
    nodo = arbol_nombres.search(nombre_exacto)
    if nodo is not None:
        return nodo.other_values['tipos']

def pokemon_debiles_contra(tipos_atacante, lista_pokemon_completa):
    set_tipos_atacante = set(tipos_atacante)
    nombres_debiles_encontrados = set()

    for pokemon_defensor in lista_pokemon_completa:
        
        debilidades_defensor = set(pokemon_defensor['debilidades'])
        
        if set_tipos_atacante.intersection(debilidades_defensor):
            nombres_debiles_encontrados.add(pokemon_defensor['nombre'])

    return sorted(list(nombres_debiles_encontrados))

tipos_jolteon = tipo_por_nombre(arbol_pokemon_nombre, 'Jolteon')
tipos_lycanroc = tipo_por_nombre(arbol_pokemon_nombre, 'Lycanroc (Midday)')
tipos_tyrantrum = tipo_por_nombre(arbol_pokemon_nombre, 'Tyrantrum')

print("Listado de Pokemon debiles a Jolteon.")
lista_debil_a_jolteon = pokemon_debiles_contra(tipos_jolteon, pokemon_list)
if lista_debil_a_jolteon:
    for nombre in lista_debil_a_jolteon:
        print(f"  - {nombre}")
else:
    print("  No se encontraron Pokémon débiles en la lista.")

print("\nListado de Pokemon debiles a Lycanroc.")
lista_debil_a_lycanroc = pokemon_debiles_contra(tipos_lycanroc, pokemon_list)
if lista_debil_a_lycanroc:
    for nombre in lista_debil_a_lycanroc:
        print(f"  - {nombre}")
else:
    print("  No se encontraron Pokémon débiles en la lista.")

print("\nListado de Pokemon debiles a Tyrantrum.")
lista_debil_a_tyrantrum = pokemon_debiles_contra(tipos_tyrantrum, pokemon_list)
if lista_debil_a_tyrantrum:
    for nombre in lista_debil_a_tyrantrum:
        print(f"  - {nombre}")
else:
    print("  No se encontraron Pokémon débiles en la lista.")

print("\nFin Ejercicio E.")


#F- Mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.

print("\nEjercicio F.")
# Creo un nuevo in order para adaptarlo a lo que necesito en este ejercicio en el Binarytree.

print("Listado de todos los Tipos de Pokémon.")
arbol_tipo.in_order_conteo()
print("\nFin Ejercicio F.")

#G- Determinar cuantos Pokémons tienen megaevolucion.
print("\nEjercicio G.")

contador_mega = 0

for pokemon in pokemon_list:
    if pokemon.get('mega_evolucion') == True:
        contador_mega += 1
        
print(f"Total de Pokémon con Mega Evolución: {contador_mega}")
print("\nFin Ejercicio G.")

#H- Determinar cuantos Pokémons tienen forma Gigamax.
print("\nEjercicio H.")

contador_giga = 0

for pokemon in pokemon_list:
    if pokemon.get('gigamax') == True:
        contador_giga += 1
        
print(f"Total de Pokémon con forma Gigamax: {contador_giga}")
print("\nFin Ejercicio H.")