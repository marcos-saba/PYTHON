print(f'{' MENU ':=^50}')
num1 = float(input('\nDigite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
print('-'*50)
opt = 0
while opt != 5:
    print('Escolha uma das opções abaixo: ')
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opt = int(input('Sua opção: '))
    print('-'*50)
    if opt < 1 or opt > 5:
        print('\033[31mOPÇÃO INVÁLIDA!\033[m Tente novamente.')
        print('-'*50)
    else:
        if opt == 1:
            print(f'A soma dos valores {num1} e {num2} vale {num1 + num2:.1f}.')
            print('-'*50)
        if opt == 2:
            print(f'A multiplicação dos valores {num1} e {num2} vale {num1*num2:.1f}.')
            print('-'*50)
        if opt == 3:
            maior = num1
            if num2 > maior:
                maior = num2
            print(f'O maior valor entre {num1} e {num2} é {maior}.')
            print('-'*50)
        if opt == 4:
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valor: '))
print(f'{'FIM':^50}')
print('-'*50)
