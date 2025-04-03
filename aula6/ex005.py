import random

bilhete = []
for i in range(6):
    bilhete.append(random.randint(0, 60))

print(f'Seu bilhete é {bilhete}')
