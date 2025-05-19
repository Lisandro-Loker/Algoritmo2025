def SumaRec(numero):

    if numero == 1:
        return 1
    else:
        return numero + SumaRec(numero - 1)

print(SumaRec(5))

def Factorial(num):

    if num == 1:
        return 1
    else:
        return num * Factorial(num -1)

print(Factorial(5))

def mostrarlistarec (lista,index):
    if index != len(lista):
        print(lista[index])
        mostrarlistarec(lista,index+1)

lista = [1,2,3,4,5]
mostrarlistarec(lista,0)