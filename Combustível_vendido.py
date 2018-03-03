
litros = int(input('Quantos litros vendidos: '))
comb = str(input('Tipo de combustível: '))

v1 = (litros * 1.9) - (litros * 0.03)
v2 = (litros * 1.9 ) - (litros * 0.05)
v3 = (litros * 2.5) - (litros * 0.04)
v4 = (litros * 2.5) - (litros * 0.06)

if comb == "a" and litros <=20:
    print('TOTAL: R$ {}'.format(v1))

if comb == "a" and litros > 20:
    print('TOTAL: R$ {}'.format(v2))

if comb == "g" and litros <= 20:
    print('TOTAL: R$ {}'.format(v3))

if comb == "g" and litros >20:

    print('TOTAL: R${}'.format(v4))


