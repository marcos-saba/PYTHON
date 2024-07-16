print(f'{' PROGRESSÃO ARITMÉTICA ':=^65}')
primeiro_termo = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pa = primeiro_termo
print(f'\nOs 10 primeiros termos da PA do número {primeiro_termo} com a razão de {razao} são: \n')
for c in range(0, 10):
    print(pa, end=' => ')
    pa += razao
print('FIM.')
print('\n')
print('-'*65)
