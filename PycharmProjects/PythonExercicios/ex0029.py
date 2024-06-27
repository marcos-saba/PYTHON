print('*'*55)
print(f'{'RADAR DE VELOCIDADE':^55}')
print('*'*55)
vel = float(input('\nQual a velocidade do \033[0;33mcarro\033[m? '))
if vel > 80:
    print(f'Sua velocidade foi de {vel}km/h. \nO limite de velocidade é de 80km/h.')
    multa = (vel - 80)*7
    print(f'Você ultrapassou o limite de velocidade em {vel-80:.1f}Km/h \ne foi multado em R${multa:.2f}!')
print(f'Sua velocidade foi de {vel}Km/h e está dentro \ndo limite permitido, que é de 80Km/h.')
print(f'\n{' FIM ':*^55}')
