print(f'{' CADASTRO 2.1 ':=^55}\n')
adulto = 0
homem = 0
mulher = 0
while True:
    print('-'*25)
    print(f'{'CADASTRE UMA PESSOA':^25}')
    print('-'*25)
    idade = int(input('Informe a idade: '))
    while True:
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
        if sexo in 'MnFf':
            break
    print('-'*25)
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SsNn':
            break
    if idade > 18:
        adulto += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    if continuar in 'Nn':
        break
print('-'*55)
print(f'{'FIM':^55}')
print('-'*55)
print(f'Total de pessoas com mais de 18 anos: {adulto}')
print(f'Ao todo foram cadastrados {homem} pessoas do sexo masculino '
      f'\ne {mulher} mulheres com menos de 20 anos.')
print('-'*55)
