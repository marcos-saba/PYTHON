print(f'{' SOMADOR ':+^50}')
print('Digite o número inicial e final do intervalo para \nmostrar sua somatória.')
i = int(input('\nDigite o número inicial: '))
f = int(input('Digite o número final: '))
v = 0
p = 1
print('''\nDigite:  
[ 0 ] Par 
[ 1 ] Ímpar''')
escolha = int(input('Sua opção: '))
if escolha < 0 or escolha > 1:
    print('Opção INVÁLIDA. Tente novamente.')
else:
    if i > f:
        p = -1
    m = int(input('Digite um múltiplo: '))
    opt = ('pares', 'ìmpares')
    s = 0
    for c in range(i, f+1, p):
        if c % 2 == escolha and c % m == 0:
            s += c
            v += 1
    print(f'\nA soma dos {v} valores que são {opt[escolha]} de {i} a {f} \ne que são multiplos de {m} vale {s}.')
print('-'*50)