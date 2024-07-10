from random import randint
from time import sleep
cores = {'limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m',
         'vermelho': '\033[31m', 'verde': '\033[32m'}
print(f'-'*55)
print(f'{'JO... KEN... PÔ':^50}')
print('-'*55)
print(f'Vamos jogar Jokenpô?!\n\nRegras do jogo:\n'
      f'\n- {cores['amarelo']}PEDRA{cores['limpa']} ganha da {cores['vermelho']}TESOURA{cores['limpa']}, '
      f'mas perde para o {cores['azul']}PAPEL{cores['limpa']};'
      f'\n- {cores['azul']}PAPEL{cores['limpa']} ganha da {cores['amarelo']}PEDRA{cores['limpa']}, '
      f'mas perde para a {cores['vermelho']}TESOURA{cores['limpa']};'
      f'\n- {cores['vermelho']}TESOURA{cores['limpa']} ganha do {cores['azul']}PAPEL{cores['limpa']}, '
      f'mas perde para a {cores['amarelo']}PEDRA{cores['limpa']}.')
print('_'*55)
print(f'''Escolha uma opção:

[ 1 ] {cores['amarelo']}PEDRA{cores['limpa']}
[ 2 ] {cores['azul']}PAPEL{cores['limpa']}
[ 3 ] {cores['vermelho']}TESOURA{cores['limpa']}
''')
jogador = int(input('Sua opção: '))
if jogador > 3 or jogador < 1:
    print(f'\nOpção {cores['vermelho']}INVÁLIDA{cores['limpa']}! Tente novamente.')
else:
    computador = randint(1, 3)
    opcao = ('PEDRA', 'PAPEL', 'TESOURA')
    sleep(0.5)
    print(end='\nJO...')
    sleep(0.5)
    print(end='KEN...')
    sleep(0.5)
    print('PÔ!')
    sleep(0.5)
    print('')
    print('-'*55)
    if jogador == 1 and computador == 1 or jogador == 2 and computador == 2 or jogador == 3 and computador == 3:
        print(f'Você: {opcao[jogador-1]}. \nComputador: {opcao[computador-1]}. '
              f'{cores['amarelo']}\n\nEMPATE{cores['limpa']}! 🙂')
    elif jogador == 1 and computador == 2 or jogador == 2 and computador == 3 or jogador == 3 and computador == 1:
        print(f'Você: {opcao[jogador-1]}. \nComputador: {opcao[computador-1]}. '
              f'\n\nVocê {cores['vermelho']}PERDEU{cores['limpa']}! 😬')
    elif jogador == 1 and computador == 3 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
        print(f'Você: {opcao[jogador-1]}. \nComputador: {opcao[computador-1]}. '
              f'\n\nVocê {cores['verde']}GANHOU{cores['limpa']}!!! 🎉')
print('_'*55)
