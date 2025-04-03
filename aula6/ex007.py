name = input('Digite seu nome: ')

while name != 'Joe':
    name = input('Digite seu nome: ')
 
for tentativas in range(3):
    senha = input('Digite a Senha: ')
    if senha == 'swordfish':
        print('Correto')
        break
    else:
        print('incorreta')

print('Encerrado')