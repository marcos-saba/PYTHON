print('-'*65)
media = 0
maior_idade = 0
menor_idade = 0
velho = ''
for c in range(1, 5):
    print(f'---- {c}ª PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        menor_idade += 1
print('-'*65)
print(f'A média de idade do grupo é de {media/4:.2f} anos.')
if maior_idade > 0:
    print(f'O nome do homem mais velho do grupo é {velho.title()} e ele tem {maior_idade} anos.')
if menor_idade > 0:
    if menor_idade > 1:
        print(f'No grupo, {menor_idade} mulheres têm menos de 20 anos.')
    else:
        print(f'No grupo, {menor_idade} mulher tem menos de 20 anos.')
print('-'*65)
