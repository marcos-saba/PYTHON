sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Valor \033[31mINVÁLIDO!\033[m! Informe seu sexo [M/F]: ')).upper().strip()[0]
print('-'*40)
if sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
else:
    print('Sexo feminino registrado com sucesso!')
print('Fim!')
