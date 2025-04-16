#Faça um programa que solicita uma quantidade indefinida de notas de uma prova (deve parar quando um número negativo for digitado).
#Armazena em uma lista.
#Após isso, o programa deve mostrar a média das notas.
def main():
    notas = []
    while True:
        try:
            nota = float(input("Digite uma nota (ou um número negativo para parar): "))
            if nota < 0:
                break
            notas.append(nota)
        except ValueError:
            print("Por favor, digite um número válido.")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"A média das notas é: {media:.2f}")
    else:
        print("Nenhuma nota foi inserida.")

if __name__ == "__main__":
    main()