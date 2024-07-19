print(f'{' PA ':=^50}')
p_termo = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('-'*50)
cont = 1
pa = p_termo
print(pa, end='=>')
while cont < 10:
    cont += 1
    pa += razao
    if cont == 10:
        print(pa, end='=> FIM.')
    else:
        print(pa, end='=>')
print('')
print('-'*50)
