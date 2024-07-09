'''num = int(input('Numero: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(unidade)
print(dezena)
print(centena)
print(milhar)'''
from time import sleep

texto = str('Vamos testar esse código...')
texto_2 = list(texto)
print(texto_2)
t = 0
for c in range(0, len(texto_2)):
    print(end=f'{texto_2[t]}')
    sleep(0.288)
    t += 1
