from random import randint

total = 0
maior = 0
menor = 0

for c in range(0, 10):
    n =  randint(0, 1000)
    if c == 0:
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    elif n % 10 == 0:
        print('bonus')
    else:
        print(n)

    total += n
    print(f'numero sorteado {n}')

print(f'O menor numero sorteado foi {menor}')
print(f'O maior numero sorteado foi {maior}')
print(f'A soma dos numeros sorteados foi {total}')
