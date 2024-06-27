print('-'*10, 'CONVERSOR DE TEMPERATURA', '-'*10)
temp = float(input('\nInforme a temperatura em ºC: '))
fahr = temp * 1.8 + 32
print(f'A temperatura de {temp}ºC é equivalente a {fahr:.1f}ºF.')
