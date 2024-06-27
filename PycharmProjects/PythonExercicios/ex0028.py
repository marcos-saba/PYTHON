from random import randint
from time import sleep
print('='*68)
print(f'{'ADIVINHE O NÚMERO':^68}')
print('='*68)
print('\nVou pensar em um número de 0 a 5. Tente adivinhar, se você puder!')
sorteio = randint(0, 5)
sleep(0.75)
print(end='Pensando')
sleep(0.5)
print(end='.')
sleep(0.5)
print(end='.')
sleep(0.5)
print('.')
sleep(0.5)
numero = int(input('Seu palpite? '))
print(end='.')
sleep(0.5)
print(end='.')
sleep(0.5)
print('.')
sleep(0.5)
if numero < 0 or numero > 5:
    print('VOCÊ É BURRO!??? ESCOLHA UM NÚMERO DE 0 A 5, APENAS!!!\nVocê tem mais uma change!')
    numero = int(input('Seu novo palpite? '))
    print(end='.')
    sleep(0.5)
    print(end='.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    if numero < 0 or numero > 5:
        print('Não consegue né?! Essa foi sua última change!\n')
    else:
        sleep(0.5)
        if numero == sorteio:
            print('ACERTOU, MISERÁVEL! PARABÉNS!!!\n')
        else:
            print('ERROOOU!!\n')
else:
    sleep(0.5)
    if numero == sorteio:
        print('ACERTOU, MISERÁVEL! PARABÉNS!!!\n')
    else:
        print('ERROOOUUU!!!\n')
print(f'Número escolhido: {sorteio}. \nSeu palpite: {numero}.\n')
print(f'{' FIM ':=^68}')
