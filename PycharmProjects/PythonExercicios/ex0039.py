from datetime import date
nascimento = int(input('Informe o ano de nascimento: '))
idade = date.today().year - nascimento
if idade < 18:
    print(f'Você precisará se alistar daqui há {18 - idade} anos.')
elif idade == 18:
    print('Tá na hora de se alistar!')
else:
    print(f'Já passou da hora de se alistar! '
          f'Você deveria ter se alistado há {idade - 18} anos!')


