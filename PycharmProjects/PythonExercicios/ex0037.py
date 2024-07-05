print('-'*50)
print(f'{'CONVERSOR DE BASES NÚMERICAS':^50}')
print('-'*50)
num = int(input('\nDigite um número: '))
print('\nAperte: \n'
      '        1 - para \033[34mBINÁRIO\n\033[m'
      '        2 - para \033[33mOCTAL\n\033[m'
      '        3 - para \033[32mHEXADECIMAL\033[m')
opt = int(input(''))
if opt == 1:
    print(f'\nO número \033[31m{num}\033[m na base \033[34mBINÁRIA\033[m é: {bin(num)[2:]}.')
elif opt == 2:
    print(f'\nO número \033[31m{num}\033[m na base \033[33mOCTAL\033[m é: {oct(num)[2:]}.')
else:
    print(f'\nO número \033[31m{num}\033[m na base \033[32mHEXADECIMAL\033[m é: {hex(num)[2:]}.')
print('-'*50)
