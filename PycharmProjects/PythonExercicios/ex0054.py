from datetime import date
print('-'*68)
maior_idade = 0
menor_idade = 0
ano = date.today().year
for c in range(1, 8):
    nasc = int(input(f'Digite a data de nascimento da {c}ª pessoa: '))
    if nasc > ano or ano - nasc > 150:
        print('Data de nascimento \033[31mINVÁLIDA!\033[m. Tente novamente.')
    else:
        if ano - nasc >= 21:
            maior_idade += 1
        else:
            menor_idade += 1
print(f'\nNo total, {maior_idade} pessoas são maiores de idade e {menor_idade} são menores de idade.')
print('-'*68)
