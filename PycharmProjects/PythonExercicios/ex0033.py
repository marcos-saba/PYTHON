print(f'{' COMPARADOR DE NÚMEROS ':=^40}')
a = int(input('\nDigite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
if a > b and a > c:
    print(f'O maior número é {a}.')
else:
    print(f'O maior número é {b}.' if b > a and b > c
          else f'O maior número é {c}.')
if a < b and a < c:
    print(f'E menor número é {a}.')
else:
    print(f'E o menor número é {b}.\n'if b < a and b < c
          else f'E o menor número é {c}.\n')
print('='*40)
# maior = a, menor = a, considera "a" como maior e "a" como menor
# e testa cada um (b e c).