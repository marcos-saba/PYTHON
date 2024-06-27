print(f'{' \033[1;4;33mANÁLISE DE TRIÂNGULOS\033[m ':-^50}')
r1 = float(input('\nDigite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('\nAs três retas \033[1;4;34mPODEM\033[m formar um \033[4;33mTRIÂNGULO\033[m.\n')
else:
    print('\nAs três retas \033[1;4;31mNÃO\033[m podem formar um \033[4;33mTRIÂNGULO\033[m.\n')
print('-'*50)
