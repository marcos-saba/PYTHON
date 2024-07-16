from random import randint

print('-'*60)
print(f'{'\033[1;4;34mJOGO DA ADIVINHAÇÃO\033[m':^70}')
print('-'*60)
print('Vou pensar em número entre 0 e 10. Tente adivinhar!\n')
cpu = randint(0, 10)
palpite = ''
tentativa = 0
while palpite != cpu:
    palpite = int(input('Seu palpite: '))
    if palpite < 0 or palpite > 10:
        print('\033[31mOPÇÃO INVÁLIDA!\033[m Escolha um número '
              '\033[1;4;33mAPENAS\033[m entre \033[4;33m0\033[m e \033[4;33m10\033[m!')
    else:
        tentativa += 1
        if palpite != cpu:
            print(f'Erroouu!. Essa é foi sua {tentativa}ª tentativa.')
print('')
print('-'*60)
if tentativa == 1:
    print(f'Oh loko!! Você acertou na {tentativa}ª tentativa!! Parabéns!!!')
elif 1 < tentativa < 6:
    print(f'Acertou miserável! Você precisou de {tentativa} tentativas.')
elif 5 < tentativa <= 10:
    print(f'Acertou! Você precisou de {tentativa} tentativas. ')
else:
    print(f'Até que enfim! Achei que não ia acertar nunca. '
          f'\nVocê precisou de {tentativa} tentativas!')
print(f'CPU: {cpu}\nVocê: {palpite}')
print('-'*60)

