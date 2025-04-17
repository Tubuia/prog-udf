#Escreva um programa que solicita que o usuário digite a altura e o peso de 5 pessoas.
#Verifique se pelo menos duas das pessoas tem a mesma altura e mesmo peso.
def main():
    pessoas = []

    for i in range(5):
        try:
            altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
            peso = float(input(f"Digite o peso da pessoa {i+1} (em kg): "))
            pessoas.append((altura, peso))
        except ValueError:
            print("Entrada inválida! Por favor, digite números válidos.")
            return

    duplicados = len(pessoas) != len(set(pessoas))

    if duplicados:
        print("\nPelo menos duas pessoas têm a mesma altura e o mesmo peso.")
    else:
        print("\nTodas as pessoas têm altura e peso diferentes.")

if __name__ == "__main__":
    main()