def sumador(n: int) -> int:
    return n+1

def sumar(a: int, b: int) -> int:
    n = a
    for i in range(b):
        n = sumador(n)
    return n

def multiplicar(a: int, b: int) -> int:
    n = a
    for i in range(b-1):
        n = sumar(n,a)
    return n

def restar(a: int, b: int) -> int:
    n = 0
    while b < a:
        n = sumador(n)
        b = sumador(b)
    return n

def dividir(a: int, b: int) -> int:
    n = 0
    while a > 0:
        a = restar(a, b)
        n = sumador(n)
    return n

a = 6
b = 2
print(sumar(a, b))
print(multiplicar(a, b))
print(restar(a, b))
print(dividir(a, b))
