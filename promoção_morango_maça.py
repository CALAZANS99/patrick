mo = int(input('Quanti. em KG de morangos: '))
ma = int(input('Quanti. em KG de maçãs: '))

promo1MO = 2.5 * mo
promo2MO = 2.2 * mo
promo3MO = (2.2 * mo) - ((2.2 * mo)*0.1)

promo1MA = 1.8 * ma
promo2MA = 1.5 * ma
promo3MA = 1.5 * ma - ((1.5 * ma)*0.1)


if mo <= 5 and ma <= 5:

    print('MORANGO - R${}'.format(promo1MO))
    print('MAÇA -    R${}'.format(promo1MA))

if mo > 5 and mo <=8 and ma >4 and ma <= 8:

    print('MORANGO - R${}'.format(promo2MO))
    print('MAÇA -    R${}'.format(promo2MA))

if (mo > 8 or promo1MO > 25) and (ma > 8 or promo1MA > 25):

    print('MORANGO - R${}'.format(promo3MO))
    print('MAÇA -    R${}'.format(promo3MA))



