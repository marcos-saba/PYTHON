print(f'{' LEITOR NUMÉRICO ':=^50}')
cont = 0
num = 0
soma = 0
l_num = []
print('Digite [999] para finalizar.')
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        l_num += [num]
        cont += 1
print('-'*50)
print(f'Ao todo foram digitados {cont} números. Sendo eles: \n{l_num}')
print(f'A soma de todos eles vale {soma}.')
print('-'*50)
print(f'{' FIM ':^50}')
