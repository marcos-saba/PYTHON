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
        if continuar in 'SN':
            break
    if idade >= 18:
        adulto += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if continuar == 'N':
        break
print('-'*55)
print(f'{'FIM':^55}')
print('-'*55)
print(f'Total de pessoas com mais de 18 anos: {adulto}')
print(f'Ao todo foram cadastrados {homem} pessoas do sexo masculino '
      f'\ne {mulher} mulheres com menos de 20 anos.')
print('-'*55)
