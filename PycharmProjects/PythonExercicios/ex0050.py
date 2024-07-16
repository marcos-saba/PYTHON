print('-'*65)
print(f'{' SOMA DOS VALORES ':^65}')
print('-'*65)
print('')
s = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'\nA soma dos {cont} valores PARES informados vale {s}.')
print('-'*65)
input('Pressione "ENTER" para sair.')
