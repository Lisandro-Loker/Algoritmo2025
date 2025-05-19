def fibr(n):
    if n < 2:
        return n
    return fibr(n-1) + fibr(n-2)

print("De el numero para Fibonacci")
num = int(input ())

for x in range(num):
    print(fibr(x))