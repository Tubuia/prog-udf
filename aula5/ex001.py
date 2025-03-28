from random import randint

total = 0
count = 0

while True:
    n = randint(0, 9)
    if n == 0:
        print('Zero sorteado, encerrando a soma')
        break
    else:
        total += n
        count += 1
        print(f'Adicionando {n} ao total')

print(f'total da soma: {total}')
print(f'total de numeros sorteados: {count}')
