seg1 = float(input('Informe o 1º seguimento: '))
seg2 = float(input('Informe o 2º seguimento: '))
seg3 = float(input('Informe o 3º seguimento: '))
if (seg1 + seg2) > seg3 and (seg1 + seg3) > seg2 and (seg2 + seg3) > seg1:
    if seg1 == seg2 == seg3:
        print('Os seguimentos podem formar um triângulo EQUILÁTERO.')
    elif seg1 != seg2 != seg3 != seg1:
        print('Os seguimentos podem formar um triângulo ESCALENO.')
    else:
        print('Os seguimentos podem formar um triângulo ISÓSCELES.')
else:
    print('Os seguimentos não podem formar um triângulo.')
