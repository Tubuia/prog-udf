velocidade = int(input('Digite a velocidade do seu veiculo em km/h: '))
limite = 80
multa = 5

if velocidade > limite:
    print('Você foi multado')
    excesso = velocidade - limite
    print(f'Você deve pagar o valor de R${multa * excesso}')

else:
    print('Você não foi multado')