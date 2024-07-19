print(f'{' VERIFICADOR DE VALORES 2.0 ':=^70}')
opt = ''
cont = 1
soma = 0
maior = 0
menor = 0
print('')
while opt != 'N':
    num = int(input('Digite um número: '))
    opt = str(input('Quer continuar [S/N]? ')).strip().upper()
    while opt not in ('S', 'N'):
        print('Opção INVÁLIDA! Tente novamente.')
        opt = str(input('Quer continuar [S/N]? ')).strip().upper()
    if cont == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    if opt == 'S':
        cont += 1
    soma += num
print('-'*70)
media = soma/cont
print(f'O maior valor digitado foi {maior} e o menor valor foi {menor}.')
print(f'Foram digitados um total de {cont} valores e a média entre eles é {media:.2f}.')
print('-'*70)
print(f'{' FIM ':^70}')
