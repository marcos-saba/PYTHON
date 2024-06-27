nome = str(input('Qual é o seu nome? '))
if nome == 'Marcos':
    print('Que nome legal em!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino.')
else:
    print('Seu nome é bem meh.')
print(f'Tenha um bom dia, {nome}!')
