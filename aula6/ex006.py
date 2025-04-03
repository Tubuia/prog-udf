from random import randint

soma = 0
while soma < 1000:
    numero = randint(0, 100)
    print(numero)
    soma += numero

print(soma)