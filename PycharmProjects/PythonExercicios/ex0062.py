print(f'{' PA 2.0 ':=^50}')
p_termo = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
pa = p_termo
print('-'*50)
print(pa, end='=>')
while cont != 10:
    pa += razao
    cont += 1
    print(pa, end='=>')
    if cont == 10:
        print('')
        opt = ''
        while opt != 0:
            print('-'*50)
            opt = int(input('Quer mostrar mais quantos termos: '))
            print('-'*50)
            if opt > 0:
                c = 0
                while c < opt:
                    c += 1
                    pa += razao
                    print(pa, end='=>')
            print('')
print(f'{' FIM ':=^50}')
