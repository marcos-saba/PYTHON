preco = float(input('Informe o preço do produto(R$): '))
pgt = int(input('''Informe a condição de pagamento: 

1 - à vista (dinheiro/cheque - 10% de desconto)
2 - à vista (cartão - 5% de desconto)
3 - até 2x (cartão - sem desconto)
4 - 3x ou mais (cartão - 20% de juros)\n'''))
print('-'*50)
if pgt == 1:
    print(f'Total a pagar: R${preco - (preco*10/100):.2f}')
elif pgt == 2:
    print(f'Total a pagar: R${preco - (preco*5/100):.2f}')
elif pgt == 3:
    print(f'Total a pagar: R${preco:.2f}')
else:
    print(f'Total a pagar: R${preco + (preco*20/100):.2f}')
