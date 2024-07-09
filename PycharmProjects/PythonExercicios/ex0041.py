from datetime import date
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
if idade <= 9:
    print(f'Idade: {idade} anos\nCategoria: MIRIN')
elif 9 < idade <= 14:
    print(f'Idade: {idade} anos\nCategoria: INFANTIL')
elif 14 < idade <= 19:
    print(f'Idade: {idade} anos\nCategoria: JUNIOR')
elif idade == 20:
    print(f'Idade: {idade} anos\nCategoria: SÊNIOR')
else:
    print(f'Idade: {idade} anos\nCategoria: MASTER')
