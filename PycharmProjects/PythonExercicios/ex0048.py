print(f'{' SOMADOR ':+^50}')
print('Digite o número inicial e final do intervalo para mostrar sua somatória.')
i = int(input('\nDigite o número inicial: '))
f = int(input('Digite o número final: '))
print('''\nDigite:  
[ 0 ] Par 
[ 1 ] Ímpar''')
escolha = int(input('Sua opção: '))
if escolha < 0 or escolha > 1:
    print('Opção INVÁLIDA. Tente novamente.')
else:
    m = int(input('Digite um múltiplo: '))
    opt = ('pares', 'ìmpares')
    s = 0
    for c in range(i, f+1):
        if c % 2 == escolha and c % m == 0:
            s += c
    print(f'A soma de todos os números {opt[escolha]} de {i} a {f} \nque são multiplos de {m} vale {s}.')
