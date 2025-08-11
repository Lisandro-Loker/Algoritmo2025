def invertir_secuencia_recursiva(secuencia):
    if len(secuencia) <=1:
        return secuencia
    else:
        return secuencia[-1]+ invertir_secuencia_recursiva(secuencia[:-1])
    
def invertir_lista_recursiva (lista):
    if len(lista) <= 1:
        return lista
    else:
        return [lista[-1]]+ invertir_lista_recursiva(lista[:-1])

lista_original_numeros = [1, 2, 3, 4]
lista_original_letras = ["a", "b", "c", "d"]

print("Aqui las secuencias originales")
print(lista_original_letras)
print(lista_original_numeros)

print("Ahora invertidos")
print(invertir_lista_recursiva(lista_original_letras))
print(invertir_lista_recursiva(lista_original_numeros))