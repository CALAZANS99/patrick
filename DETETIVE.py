p1 = str(input('Telefonou para a vítima? '))
p2 = str(input('Esteve no local do crime? '))
p3 = str(input('Mora perto da vítima? '))
p4 = str(input('Devia para a vítima? '))
p5 = str(input('Já trabalhou com a vítima? '))
sim = "SIM"

if p1 == "SIM":
    ponto1 = 1
else:
    ponto1 = 0

if p2 == "SIM":
    ponto2 = 1
else:
    ponto2 = 0

if p3 == "SIM":
    ponto3 = 1
else:
    ponto3 = 0

if p4 == "SIM":
    ponto4 = 1
else:
    ponto4 = 0

if p5 == "SIM":
    ponto5 = 1
else:
    ponto5 = 0

pontototal = (ponto1 + ponto2 + ponto3 + ponto4 + ponto5)

if pontototal == 5:
    print('Pontuação {}'.format(pontototal))
    print('ASSASINO')

if pontototal == 3:
    print('Pontuação {}'.format(pontototal))
    print('Cúmplice')

if pontototal == 4:
    print('Pontuação {}'.format(pontototal))
    print('Cúmplice')

if pontototal == 2:
    print('Pontuação {}'.format(pontototal))
    print('SUSPEITO')

if pontototal == 1 or 0:
    print('Pontuação {}'.format(pontototal))
    print('INOCENTE')



