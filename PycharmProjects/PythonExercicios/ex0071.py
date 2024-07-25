'''
R$50,00 - R$30,00 - R$10,00 - R$1,00
'''
print(f'{' CAIXA ELETRÔNICO RICO ':=^45}\n')
dinheiro = int(input('Qual valor a ser sacado? R$'))
ced_50 = 0
ced_20 = 0
ced_10 = 0
ced_1 = 0
cedula = dinheiro
while cedula >= 50:
    cedula -= 50
    ced_50 += 1
if cedula < 50:
    while cedula >= 20:
        cedula -= 20
        ced_20 += 1
if cedula < 20:
    while cedula >= 10:
        cedula -= 10
        ced_10 += 1
if cedula < 10:
    while cedula >= 1:
        cedula -= 1
        ced_1 += 1
print('-'*45)
print(f'Notas de R$50,00: {ced_50}')
print(f'Notas de R$20,00: {ced_20}')
print(f'Notas de R$10,00: {ced_10}')
print(f'Notas de R$1,00: {ced_1}')
print('-'*45)
print('Volte sempre! Tenha um bom dia!')
