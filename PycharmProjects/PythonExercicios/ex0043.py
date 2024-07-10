peso = float(input('Informe seu peso: '))
alt = float(input('Informe sua altura: '))
imc = peso / pow(alt, 2)
print('-'*33)
print(f'IMC: {imc:.1f} \nVocê está com ', end='')
if imc < 18.5:
    print(f'\033[33mABAIXO DO PESO\033[m.')
elif 18.5 <= imc < 25:
    print(f'\033[34mPESO IDEAL\033[m.')
elif 25 <= imc < 30:
    print(f'\033[33mSOBREPESO\033[m.')
elif 30 <= imc < 40:
    print(f'\033[35mOBESIDADE\033[m.')
else:
    print(f'\033[31mOBESIDADE MÓRBIDA\033[m.')
