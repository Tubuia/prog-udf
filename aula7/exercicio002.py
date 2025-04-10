# Escreva um codigo que gera numeros aleatorios de A a B e vai executando C operações com esses numeros.
#c = soma, subtração e multiplicação
from random import randint
def funcao(a, b, c):
    n1 = randint(a, b)
    n2 = randint(a, b)
    print(f'Os numeros sorteados foram {n1} e {n2}')
    if c == 'soma':
        print('somando os numeros')
        soma = n1 + n2
        print(f'A soma foi {soma}')
    elif c == 'subtração':
        print('somando os numeros')
        subtracao = n1 - n2
        print(f'A subtração foi {subtracao}')
    elif c == 'multiplicação':
        print('multiplicando os numeros')
        multiplcacao = n1 * n2
        print(f'A multiplicaçãp foi {multiplcacao}')

print(funcao(0, 10, 'soma'))