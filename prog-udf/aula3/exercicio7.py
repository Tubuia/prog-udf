n1 = int(input('Digite a nota 1: '))
p1 = int(input('Digite o peso dessa nota: '))

n2 = int(input('Digite a nota 2: '))
p2 = int(input('Digite o peso dessa nota: '))

n3 = int(input('Digite a nota 3: '))
p3 = int(input('Digite o peso dessa nota: '))

media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print(f'Sua nota é {media}')