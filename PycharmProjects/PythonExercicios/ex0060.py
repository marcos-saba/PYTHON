print(f'{' FATORIAL ':=^50}')
num = int(input('\nDigite um número para mostrar seu fatorial: '))
print('-'*50)
f = num
print(f'{num}! = {num}x', end='')
#com FOR:
'''for n in range(num-1, 0, -1):
    f *= n
    if n == 1:
        print(n, end=' = ')
    else:
        print(n, end='x')'''
#com WHILE:
cont = num
while cont != 1:
    cont -= 1
    f *= cont
    if cont == 1:
        print(cont, end=' = ')
    else:
        print(cont, end='x')
print(f'{f}')
print('-'*50)
