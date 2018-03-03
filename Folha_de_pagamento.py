hv = float(input('Quanto vale sua hora de trabalho? '))
hd = float(input('Quantas horas você trabalha por mês? '))

salariobruto = (hv * hd)

if salariobruto <= 900:
    print('Salário bruto:              R$ }'.format(salariobruto))
    print('Imposto de Renda (ISENTO):  R$ 00,00')
    print('INSS:                       R$ {}'.format(salariobruto*0.1))
    print('FGTS (11%):                 R$ {}'.format(salariobruto*0.11))
    print('Total de descontos:         R$ {}'.format(salariobruto *0.1))
    print('Salário Líquido:            R$ {}'.format(salariobruto - salariobruto*0.1))

if salariobruto >900 and salariobruto <=1500:
    print('Salário bruto:              R$ {}'.format(salariobruto))
    print('Imposto de Renda:           R$ {}'.format(salariobruto*0.05))
    print('INSS:                       R$ {}'.format(salariobruto * 0.1))
    print('FGTS (11%):                 R$ {}'.format(salariobruto * 0.11))
    print('Total de descontos:         R$ {}'.format(salariobruto*0.15))
    print('Salário Líquido:            R$ {}'.format(salariobruto - salariobruto * 0.15))

if salariobruto > 1500 and salariobruto <= 2500:
    print('Salário bruto:              R$ {}'.format(salariobruto))
    print('Imposto de Renda:           R$ {}'.format(salariobruto * 0.1))
    print('INSS:                       R$ {}'.format(salariobruto * 0.1))
    print('FGTS (11%):                 R$ {}'.format(salariobruto * 0.11))
    print('Total de descontos:         R$ {}'.format(salariobruto * 0.2))
    print('Salário Líquido:            R$ {}'.format(salariobruto - salariobruto * 0.20))

if salariobruto > 2500:
    print('Salário bruto:              R$ {}'.format(salariobruto))
    print('Imposto de Renda:           R$ {}'.format(salariobruto * 0.2))
    print('INSS:                       R$ {}'.format(salariobruto * 0.1))
    print('FGTS (11%):                 R$ {}'.format(salariobruto * 0.11))
    print('Total de descontos:         R$ {}'.format(salariobruto * 0.3))
    print('Salário Líquido:            R$ {}'.format(salariobruto - salariobruto * 0.3))





