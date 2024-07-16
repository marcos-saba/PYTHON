sexo = ''
while sexo not in ('M', 'F'):
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    if sexo not in ('M', 'F'):
        print('Valor \033[31minválido\033[m. Tente novamente.')
print('Fim!')
