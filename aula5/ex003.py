senha = str(input('DIgite uma senha: '))

menos_8 = False
mais_16 = False
mai = False
num = False
especial = False
espaço = False

if len(senha) < 8:
    menos_8 = True
if len(senha) < 16:
    mais_16 = True

for s in senha:
    if s in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
        mai = True
    elif s in '0123456789':
        num = True
    elif s in '@#$%&*/?.:;':
        especial = True
    elif s in ' ':
        espaço = True

print('menos de 8') if menos_8 else None
print('mais de 16') if mais_16 else None
print('Não possui letra maiuscula') if not mai else None
print('não possui caracteres especiais') if not especial else None
print('não possui numeros') if not num else None
print('Não pode conter espaços') if espaço else None
