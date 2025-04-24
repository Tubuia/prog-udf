alunos = {
    "Alice": 8.5,
    "Bruno": 7.8,
    "Carla": 9.2,
    "Diego": 6.9,
    "Eva": 8.0,
    "Fernando": 7.5,
    "Gabriela": 9.0,
    "Henrique": 6.7,
    "Isabela": 8.3,
    "João": 7.2
}

zero = all(alunos.values())

print(f'Existem {len(alunos)} alunos.')
if zero:
    print('Nenhum aluno tirou zero')
else:
    print('Algum aluno tirou zero')
print(f'A menor nota foi {min(alunos.values())}')
print(f'A maior nota foi {max(alunos.values())}')
