#Escreva um programa que aplica a função módulo a todos os elementos e uma lista.
lista = [-4, 2, -3, 5, -6, 1]
lista_modulo = []

for c in range(len(lista)):
    op = abs(lista[c])
    lista_modulo.append(op)

print(lista_modulo)