from time import sleep
'''for c in range(6, 1, -2):
    print(c)
print('fim')'''
'''n = int(input('Digite um número: '))
for c in range(1, n+1):
    print(c, end=' ')
    sleep(0.25)
print('FIM')'''
'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print(f'A somatória de todos os valores é {s}.')
