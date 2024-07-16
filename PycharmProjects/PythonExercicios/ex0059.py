opt = 0
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
while opt != 5:
    print('Escolha uma das opções abaixo: ')
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opt = int(input('Sua escolha: '))
    if opt == 1:
        print(f'A soma dos valores {num1} e {num2} vale {num1 + num2:.2f}.')
    if opt == 3:
        maior = num1
        if num2 > maior:
            maior = num2
        print(f'O maior valor entre {num1} e {num2} é {maior}')

