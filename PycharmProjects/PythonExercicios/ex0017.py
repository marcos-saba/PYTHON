from math import hypot
print('='*10, 'CALCULADORA DE TRIÂNGULOS', '='*10)
cop = float(input('\nDigite o comprimento do cateto oposto: '))
cad = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(cop, cad)
print(f'O comprimento da hipotenusa para os catetos informados \né igual a {hip:.2f}.')
print('='*15, 'FIM', '='*15)
