from datetime import date
nascimento = int(input('Informe o ano de nascimento: '))
sexo = str(input('Informe seu sexo (F/M): ')).strip().upper()
idade = date.today().year - nascimento
if sexo == 'M':
    if idade < 18:
        if 18 - idade == 1:
            ano = 'ano'
        else:
            ano = 'anos'
        print(f'Você precisará se alistar daqui há {18 - idade} {ano}.')
        print(f'Seu alistamento será no ano de {nascimento + 18}.')
    elif idade == 18:
        print('Tá na hora de se alistar!')
    else:
        if idade - 18 == 1:
            ano = 'ano'
        else:
            ano = 'anos'
        print(f'Já passou da hora de se alistar! '
              f'Você deveria ter se alistado há {idade - 18} {ano}!'
              f'\nSeu alistamento foi no ano de {nascimento + 18}.')
else:
    print('Você é do sexo feminino e não precisa se alistar.')