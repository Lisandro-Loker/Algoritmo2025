from lista_heroes import super_heroes

def busqueda_america(supher, indice=0):
    if indice >= len(supher):
        return indice, False
    elif supher[indice] == "Capitan America":
        return True
    else:
        return busqueda_america(supher, indice+1)
    
def lista_superheroes(supher, indice=0):
    if indice == len(supher):
        return 
    print(supher[indice])
    lista_superheroes(supher, indice +1)

print("Busqueda de Capita America")
if busqueda_america(super_heroes):
    print("Capitan America esta en la lista\n")
else:
    print("Capitan America no esta en la lista\n")

print("Ahora listamos a todos los superheroes y de paso confirmamos que esta el Capitan America")
lista_superheroes(super_heroes)
