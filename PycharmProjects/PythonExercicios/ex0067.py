print(f'{' TABUADA 2.1 ':=^50}\n')
while True:
    n = int(input('Digite um número para mostrar sua tabuada: '))
    if n < 0:
        break
    cont = 1
    print('-'*50)
    while cont <= 10: #pode usar o "for" como alternativa
        r = n*cont
        print(f'{n:>20} x {cont:>2} = {r}')
        cont += 1
    print('-'*50)
print('-'*50)
print(f'{'Programa encerrado.':^50}')
