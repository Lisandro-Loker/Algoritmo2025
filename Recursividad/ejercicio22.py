def usar_la_fuerza(mochila, contador=0):
    if not mochila:
        return False, contador
    objeto = mochila[0]
    if objeto == "sable de luz":
        return True, contador + 1
    else:
        return usar_la_fuerza(mochila[1:], contador + 1)


mochila = ["Pancho", "Cubo Rubik", "Granada", "Botella de agua", "Campera", "Pelota"]
encontrado, objetos_revisados = usar_la_fuerza (mochila)

print("¿Se encontró el sable de luz?", "Sí" if encontrado else "No")
print("Objetos revisados: ", objetos_revisados)
print("En la mochila hay ", len(mochila), " objetos.")