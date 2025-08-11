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

numbers = [1, 3, 4, 6]

def bus_bin_iter (array, value):
    first = 0
    last = len(array) -1
    while first <= last:
        middle = (first + last) // 2
        if array[middle] == value:
            position = middle
        elif array[middle] > value:
            last = middle -1
        else:
            first = middle + 1
    return position

print (bus_bin_iter(numbers, 3))

def bus_bin_rec(array, value, _first, _last):
    first = _first
    last = _last
    middle = (first + last) // 2
    if array[middle] == value:
        return middle
    else:
        if array[middle] > value:
            return bus_bin_rec(array, value, first, last - 1)
        else:
            return bus_bin_rec(array, value, first+1, last)
        
print(bus_bin_rec(numbers,3))