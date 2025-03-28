n1 = int(input('Digite sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media > 6:
    print('Você está aprovado')
else:
    print('Você está de recuperação')
    n3 = int(input('Digite a nota prova de Recuperação: '))
    mediaR = (n1 + n2 + n3) / 3
    if mediaR > 6:
        print('Você está aprovado')
    else:
        print('Você está reprovado')