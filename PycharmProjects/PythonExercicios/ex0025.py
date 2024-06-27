nome = str(input('Digite seu nome: ')).strip()
silva = str(nome.upper().find('SILVA')) #.format('SILVA' in nome.upper())
print(f'Tem "SILVA" no seu nome? \n{silva.isnumeric()} ')
