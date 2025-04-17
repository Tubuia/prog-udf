#Faça um programa que solicita uma quantidade indefinida de números positivos (deve parar quando um número negativo for digitado).
#Armazene todos os números digitados em uma lista, sem repetição.
def main():
    numeros = []

    while True:
        try:
            numero = int(input("Digite um número positivo (ou um número negativo para sair): "))
            
            if numero < 0:
                break

            if numero not in numeros:
                numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número válido.")

    print("\nNúmeros digitados (sem repetição):")
    print(numeros)

if __name__ == "__main__":
    main()