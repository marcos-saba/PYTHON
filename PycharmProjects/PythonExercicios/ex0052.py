print(f'{' VERIFICADOR DE NÚMEROS PRIMOS ':=^55}')
num = int(input('\nDigite um número para verificar se ele é primo: '))
t = 0
print(f'O número {num} ', end='')
for c in range(1, num + 1):
    if num % c == 0:
        t += 1
if t == 2:
    print('é PRIMO.\n')
else:
    print('NÃO é PRIMO.\n')
print('-'*55)
