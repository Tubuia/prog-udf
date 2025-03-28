t1 = str(input('digite uma palavra: '))
vogais = 0
consoantes = 0

for letra in t1:
    if letra in 'aeiou':
        vogais +=1
    else:
        consoantes +=1
print(f'a palavra tem {vogais} vogais e {consoantes} consoantes')