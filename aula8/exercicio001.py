#Escreva um programa que solicita que o usuário digite 5 números inteiros e os coloca em uma lista.
#Quando terminar, imprima a lista.
numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print(f"Os números digitados foram: {numeros}",)