# Minha solução
teste = []
for p in range(1, 6):
    peso = float(input(f'Informe o peso da {p}ª pessoa: '))
    teste += [peso]
print('-'*40)
print(f'\nO maior peso foi {max(teste):.1f}Kg.')
print(f'O menor peso foi {min(teste):.1f}Kg.')
'''
# Solução do Guanabara
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Informe o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\nO maior peso foi {maior:.1f}Kg.')
print(f'O menor peso foi {menor:.1f}Kg.')
'''


