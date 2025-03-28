soma = 0

while True:
    n = int(input('Digite um numero: '))

    if n > 0:
        soma += n
    else:
        print(f'Está á a soma dos numeros{soma}')
        break