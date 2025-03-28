import cmath

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite outro numero: '))
delta = n2 ** 2 - 4 * n1 * n3

if delta > 0:
    raiz1 = (-n2 + cmath.sqrt(delta)) / (2 * n1)
    raiz2 = (-n2 - cmath.sqrt(delta)) / (2 * n1)
    print("As raízes são reais")
    print(f"Raiz 1: {raiz1.real}")
    print(f"Raiz 2: {raiz2.real}")
else:
    raiz1 = (n1 + cmath.sqrt(delta)) / (2 * n1)
    raiz2 = (n1 - cmath.sqrt(delta)) / (2 * n1)
    print("As raízes são complexas.")
    print(f"Raiz 1: {raiz1}")
    print(f"Raiz 2: {raiz2}")