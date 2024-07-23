from random import randint

print(f'{' JOGO PAR OU ÍMPAR ':=^50}\n')
while True:
    jogador = int(input('Diga um valor: '))
    jogada = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    cpu = randint(0, 10)
    soma = jogador + cpu
    if soma % 2 == 0:
        res = 'PAR'
    else:
        res = 'ÍMPAR'
    if res == 'PAR' and jogada in 'Pp':
        print('Você VENCEU!')
