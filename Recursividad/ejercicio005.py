#5.Desarrollar una función que permita convertir un número romano en un número decimal

def romadecimal(numr):
    if len(numr) == 0:
        return 0
    elif numr[-1] == "M":
        if len(numr) > 1:
            if numr[-2] == "M":
                return 1000 + romadecimal(numr[:1])
            else:
                return 1000 - romadecimal(numr[:1])
        else:
            return 1000 - romadecimal(numr[:1])
    elif numr[-1] == "D":
        return 500 - romadecimal(numr[:1])
    elif numr[-1] == "V":
        return 5 - romadecimal(numr[:1])
    elif numr[-1] == "X":
        if len(numr) > 1:
            if numr[-2] == "X":
                return 10 + romadecimal(numr[:1])
            else:
                return 10 - romadecimal(numr[:1])
        else:
            return 10 - romadecimal(numr[:1])
    elif numr[-1] == "L":
        return 50 - romadecimal(numr[:1])
    elif numr[-1] == "C":
        if len(numr) > 1:
            if numr[-2] == "C":
                return 100 + romadecimal(numr[:1])
            else:
                return 100 - romadecimal(numr[:1])
        else:
            return 100 - romadecimal(numr[:1])
    elif numr[-1] == "I":
        return 1 + romadecimal(numr[:1])

print(romadecimal("XII"))