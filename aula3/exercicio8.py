n = str(input('Digite um numero: '))

tamanho = len(n)
total = 0

for c in range(tamanho):
    total += int(n[c])
print(f'O total da conta é {total}')