n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1 + n2) / 2
print('_'*25)
if media < 5.0:
    print(f'Média: \033[31m{media:.1f}\033[m\nSituação: \033[31mREPROVADO\033[m')
elif 5.0 <= media <= 6.9:
    print(f'Média: \033[33m{media:.1f}\033[m\nSituação: \033[33mRECUPERAÇÃO\033[m')
else:
    print(f'Média: \033[34m{media:.1f}\033[m\nSituação: \033[34mAPROVADO\033[m')
