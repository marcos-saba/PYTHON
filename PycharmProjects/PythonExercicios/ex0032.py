from datetime import date
print('*'*65)
print('{:^65}'.format('CALCULADORA DE ANOS BISSEXTO'))
print('*'*65)
ano = int(input('\nDigite o ano a ser analisado, digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.\n'.format(ano))
else:
    print('O ano {} não é BISSEXTO.\n'.format(ano))
print('*'*65)

