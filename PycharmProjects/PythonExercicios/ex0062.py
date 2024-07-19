print(f'{' PA 2.0 ':=^50}')
p_termo = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 0
pa = p_termo
print('-'*50)
opt = 10
tot = 0
while opt != 0:
    tot += opt
    while cont < tot:
        print(pa, end='=> ')
        pa += razao
        cont += 1
    print('Pausa')
    print('-' * 50)
    opt = int(input('Quer mostrar mais quantos termos: '))
    print('-' * 50)
print(f'Progressão finalizado com um total de {tot} termos.')
print(f'{' FIM ':=^50}')
