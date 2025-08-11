from fractions import Fraction

def serie_numeros_recursiva(num):
    if num == 1:
        return Fraction(1,1)
    else:
        print(Fraction(1,num))
        return Fraction(1,num) + serie_numeros_recursiva(num-1)
    
print("De un numero a probar:")
numero=int(input())
print("Aqui se muestra cada fracción a sumar")
print(serie_numeros_recursiva(numero))
print("Y este numero final es la suma de todos.")