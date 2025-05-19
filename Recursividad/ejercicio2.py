def SumaRec(numero):

    if numero == 1:
        return 1
    else:
        return numero + SumaRec(numero - 1)
    
print("De hasta el numero que quiere que sea sumado")
num = int(input())

print(SumaRec(num))