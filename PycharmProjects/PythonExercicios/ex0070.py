print('-'*45)
print(f'{' LOJA PREÇO EM QUEDA LIVRE':^45}')
print('-'*45, '\n')
tot_gasto = 0
mil = 0
mais_barato = 0
nome_barato = ''
cont = 1
while True:
    nome_prod = str(input('Nome do produto: '))
    preco_prod = float(input('Preço: R$'))
    while True:
        ctrl = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if ctrl in 'SsNn':
            break
    if preco_prod > 1000:
        mil += 1
    if cont == 1:
        mais_barato = preco_prod
        nome_barato = nome_prod
    if preco_prod < mais_barato:
        mais_barato = preco_prod
        nome_barato = nome_prod
    tot_gasto += preco_prod
    if ctrl in 'Nn':
        break
    cont += 1
print(f'\n{' FIM ':-^45}')
print(f'Total da compra: R${tot_gasto:.2f}')
print(f'Produtos acima de R$1000,00: {mil}')
print(f'Produto mais barato: {nome_barato} - R${mais_barato:.2f}')
