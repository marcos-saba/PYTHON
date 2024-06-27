print('_'*45)
print('{:^45}'.format(' CALCULADORA DE VIAGEM '))
print('_'*45)
d = float(input('\nDigite a distância da viagem(km): '))
if d <= 200:
    print(f'Sua viagem será de {d}Km.\nSua passagem custará R${d*0.5:.2f}.\n')
else:
    print(f'Sua viagem será de {d}Km.\nSua passagem custará R${d*0.45:.2f}.\n')
print('_'*45)
