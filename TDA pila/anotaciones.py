pila = [1,2,3,4,5]
print(pila)
# La pila se trata como lista

pila.append(7)
print(pila)
# Añadir en el ultimo lugar un valor

pila.pop()
print(pila)

# Elimina el ultimo numero de la pila

# ejemplos del profesor

class Stack:
    elements = [1,2,3]

    def mostrar_elementos(self):
        print(self.elements)

stack = Stack()
stack.elements[1] = 99
stack.mostrar_elementos()


print (stack.elements)
