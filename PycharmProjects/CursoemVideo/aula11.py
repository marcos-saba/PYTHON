#print('\033[7;33;44mOlá, Mundo!\033[m')
nome = 'Marcos'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7m'}
print(f'Olá, {cores['amarelo']}{nome}{cores['limpa']}!!!')
