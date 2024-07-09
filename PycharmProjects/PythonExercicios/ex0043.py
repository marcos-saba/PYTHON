peso = float(input('Informe seu peso: '))
alt = float(input('Informe sua altura: '))
imc = peso / pow(alt, 2)
print('-'*30)
if imc < 18.5:
    print(f'IMC: {imc:.2f} \nVocê está \033[33mABAIXO DO PESO\033[m.')
elif 18.5 <= imc < 25:
    print(f'IMC: {imc:.2f} \nVocê está com \033[34mPESO IDEAL\033[m.')
elif 25 <= imc < 30:
    print(f'IMC: {imc:.2f} \nVocê está com \033[33mSOBREPESO\033[m.')
elif 30 <= imc < 40:
    print(f'IMC: {imc:.2f} \nVocê está com \033[35mOBESIDADE\033[m.')
else:
    print(f'IMC: {imc:.2f} \nVocê com \033[31mOBESIDADE MÓRBIDA\033[m.')
