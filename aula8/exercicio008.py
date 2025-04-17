#Faça um programa que solicita que o usuário digite o nome e a idade de diversas pessoas (o programa deve parar quando um nome vazio for informado).
#Retorne o nome da pessoa mais velha.
def main():
    pessoas = []

    while True:
        nome = input("Digite o nome da pessoa (ou pressione Enter para encerrar): ").strip()
        if nome == "":
            break

        try:
            idade = int(input(f"Digite a idade de {nome}: "))
            pessoas.append((nome, idade))
        except ValueError:
            print("Idade inválida. Tente novamente.")
    
    if not pessoas:
        print("\nNenhuma pessoa foi cadastrada.")
        return

    mais_velha = max(pessoas, key=lambda pessoa: pessoa[1])
    print(f"\nA pessoa mais velha é: {mais_velha[0]} ({mais_velha[1]} anos)")

if __name__ == "__main__":
    main()