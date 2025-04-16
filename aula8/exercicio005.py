#Faça um programa que solicita uma quantidade indefinida de números positivos (deve parar quando um número negativo for digitado).
#Armazene-os em duas listas:
#uma para os números pares;
#outra para os números ímpares.
#A seguir, mostre a porcentagem de pares e ímpares digitados.
def main():
    numeros_pares = []
    numeros_impares = []

    while True:
        try:
            numero = int(input("Digite um número positivo (ou um número negativo para parar): "))
            if numero < 0:
                break
            if numero % 2 == 0:
                numeros_pares.append(numero)
            else:
                numeros_impares.append(numero)
        except ValueError:
            print("Por favor, digite um número válido.")

    total_numeros = len(numeros_pares) + len(numeros_impares)
    
    if total_numeros == 0:
        print("Nenhum número foi digitado.")
    else:
        porcentagem_pares = (len(numeros_pares) / total_numeros) * 100
        porcentagem_impares = (len(numeros_impares) / total_numeros) * 100

        print(f"Porcentagem de números pares: {porcentagem_pares:.2f}%")
        print(f"Porcentagem de números ímpares: {porcentagem_impares:.2f}%")

if __name__ == "__main__":
    main()