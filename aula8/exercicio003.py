#Escreva um programa que apaga todos os elementos negativos de uma lista.
def remove_negativos(lista):
    return [x for x in lista if x > 0]

lista = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
lista_sem_negativos = remove_negativos(lista)
print(lista_sem_negativos)