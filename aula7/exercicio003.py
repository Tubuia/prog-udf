#Escreva uma função que retorna o fatorial de um numero dado
def fatorial(n):
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
    return resultado

print(fatorial(5))