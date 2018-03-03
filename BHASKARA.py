a = int(input('Coeficiente 1: '))
if a == 0:
    print('"A" TEM DE SER DIFERENTE DE 0 PARA SE CONFIGURAR UMA EQUAÇÃO DO SEGUNDO GRAU, TENTE UM NÚMERO MAIOR !')
else:
 b = int(input('Coeficiente 2: '))
 c = int(input('Coeficiente 3: '))


delta = (b**2 - (4*a*c))
x1 = (-b + (delta)**(1/2))/2*a
x2 = (-b - (delta)**(1/2))/2*a

if delta < 0:
    print('EQUAÇÃO NÃO POSSUI RAÍZES')

if delta > 0:


    print('RAÍZ 1: {}'.format(x1))
    print('RAÍZ 2: {}'.format(x2))


