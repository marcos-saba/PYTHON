palavra = str(input('Digite uma palavra ou frase para verificar se ela é um palídromo: \n')).strip().upper().split()
junto = ''.join(palavra)
t1 = ''
t2 = ''
print(f'A frase ou palavra {junto} invertida é {junto[::-1]} \ne ela ', end='')
for c in range(1, len(junto)+1): #for letra in range(len(junto) -1, -1, -1):
    t1 += junto[c-1]               #inverso += junto [letra]
    t2 += junto[-c]              #if inverso == junto
if t1 == t2:
    print('é um PALÍNDROMO.')
else:
    print('Não é um PALÍNDROMO.')
# junto[::-1] - outra solução, inverte a frase.