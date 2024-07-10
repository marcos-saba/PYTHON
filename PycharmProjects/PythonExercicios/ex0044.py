preco = float(input('Informe o preço do produto(R$): '))
print('''FORMAS DE PAGAMENTO: 
( 1 ) à vista dinheiro/cheque (10% de desconto)
( 2 ) à vista cartão (5% de desconto)
( 3 ) 2x no cartão (sem desconto)
( 4 ) 3x ou mais no cartão (20% de juros)\n''')
pgt = int(input('Sua opção: '))
print('-'*50)
if pgt == 1:
    print(f'Total a pagar: R${preco - (preco*10/100):.2f}')
elif pgt == 2:
    print(f'Total a pagar: R${preco - (preco*5/100):.2f}')
elif pgt == 3:
    print(f'Total de parcelas: 2x R${preco / 2:.2f}')
    print(f'Total a pagar: R${preco:.2f}')
elif pgt == 4:
    parcelas = int(input('Informe o número de parcelas: '))
    print(f'Total de parcelas: {parcelas}x R${(preco + (preco*20/100))/parcelas:.2f}. ')
    print(f'Total a pagar: R${preco + (preco*20/100):.2f}')
else:
    print('\033[31mOPÇÃO INVÁLIDA!\033[m Tente novamente.')
# Pode-se criar uma variável para o preço final
