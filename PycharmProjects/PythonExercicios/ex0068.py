from random import randint

print(f'{' JOGO PAR OU ÍMPAR ':=^55}\n')
cont = 1
while True:
    jogador = int(input('Diga um valor: '))
    jogada = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    cpu = randint(0, 10)
    soma = jogador + cpu
    if soma % 2 == 0:
        res = 'PAR'
    else:
        res = 'ÍMPAR'
    print('-'*55)
    print(f'Você jogou {jogador} e o computador {cpu}. Total de {soma}, deu {res}. ')
    print('-'*55)
    if res == 'PAR' and jogada in 'Pp' or res == 'ÍMPAR' and jogada in 'Ii':
        print('Você VENCEU!')
        print('Vamos jogar de novo...')
    else:
        print('Você PERDEU!')
        break
    print('=*='*19)
    cont += 1
print('-'*55)
print(f'{f'GAME OVER! Você venceu {cont} vezes.':^55}')
print('_'*55)
