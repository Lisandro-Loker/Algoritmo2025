class Pila:
    def __init__(self):
        self.items=[]
    def esta_vacia(self):
        return len(self.items) == 0
    def apilar(self,elemento):
        self.items.append(elemento)
    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()
    def cima(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items[-1]
    def tamanio(self):
        return len(self.items)

def contar_ocurrencias(pila,elemento_buscado):
    contador=0
    pila_temporal = Pila()
    while not pila.esta_vacia():
        elemento_actual = pila.desapilar()
        if elemento_actual == elemento_buscado:
            contador += 1
        pila_temporal.apilar(elemento_actual)
    while not pila_temporal.esta_vacia():
        pila.apilar(pila_temporal.desapilar())
    return contador

if __name__ == "__main__":
    mi_pila = Pila()
    mi_pila.apilar(1)
    mi_pila.apilar(2)
    mi_pila.apilar(2)
    mi_pila.apilar(5)
    mi_pila.apilar(3)
    mi_pila.apilar(6)
    mi_pila.apilar(4)
    mi_pila.apilar(1)
    mi_pila.apilar(2)
    mi_pila.apilar(10)

print(f"Elementos en la pila: {mi_pila.items}")

elemento_a_buscar = 2
ocurrencias = contar_ocurrencias(mi_pila, elemento_a_buscar)
print (f"El elemento {elemento_a_buscar} aparece {ocurrencias} veces en la pila")