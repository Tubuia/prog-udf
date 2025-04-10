#Escreva uma função que retorna se uma dada palavra é um palidromo
def palindromo(palavra):
    i = 0
    n = len(palavra)
    if n % 2 == 0:
        while i < n / 2:
            if palavra[i] != palavra[n-1-i]:
                return False
            i += 1
    return True

print(palindromo('abccba'))