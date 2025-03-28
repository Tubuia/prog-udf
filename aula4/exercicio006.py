n = int(input("Digite uma numero: "))

while n != 0:
    if n % 2 == 0:
        print('Par')
        n = int(input("Digite uma numero: "))
    elif n % 2 != 0:
        print('Impar')
        n = int(input("Digite uma numero: "))