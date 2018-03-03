tipodeCARNE = str(input('Tipo de Carne: '))
qntddeCARNE = float(input('Quantidade de carne: '))
pag = str(input('Tipo de pagamento: '))


#promo 1 === até 5 KG
#promo 2 === mais de 5KG

promo1file = 4.9 * qntddeCARNE
promo2file = 5.8 * qntddeCARNE
promo1alcatra = 5.9 * qntddeCARNE
promo2alcatra = 6.8 * qntddeCARNE
promo1picanha = 6.9 * qntddeCARNE
promo2picanha = 7.8 * qntddeCARNE


if tipodeCARNE == "Filé Duplo" and qntddeCARNE <= 5 and pag == "Dinheiro":

     print('==== NOTA FISCAL ===')
     print('                                            ')
     print('Tipo de Carne: {}'.format(tipodeCARNE))
     print('Quantidade de Carne: {}'.format(qntddeCARNE))
     print('Valor da compra: R$ {:.2f}'.format(promo1file))

if tipodeCARNE == "Filé Duplo" and qntddeCARNE <= 5 and  pag == "Cartão Tabajara":

     print('=== NOTA FISCAL ===')
     print('                                            ')
     print('Tipo de Carne: {}'.format(tipodeCARNE))
     print('Quantidade de Carne: ')
     print('Valor da compra: R$ {:.2f}'.format(promo1file))

     print('DESCONTO DE 5%')

     print('TOTAL À PAGAR: R$ {:.2f}'.format(promo1file*0.95))
     print('Valor do desconto: R$ {:.2f}'.format(promo1file - promo1file*0.95))

if tipodeCARNE == "Filé Duplo" and qntddeCARNE > 5 and pag == "Dinheiro":

    print('=== NOTA FISCAL ===')
    print('                                            ')
    print('Tipo de Carne: {}'.format(tipodeCARNE))
    print('Quantidade de Carne: {} KG'.format(qntddeCARNE))
    print('Valor da compra: R$ {:.2f}'.format(promo2file))

if tipodeCARNE == "Filé Duplo" and qntddeCARNE > 5 and pag == "Cartão Tabajara":
    print('=== NOTA FISCAL ===')
    print('                                            ')
    print('Tipo de Carne: {}'.format(tipodeCARNE))
    print('Quantidade de Carne: {} KG'.format(qntddeCARNE))
    print('Valor da compra: R$ {:.2f}'.format(promo2file))

    print('DESCONTO DE 5%')

    print('TOTAL À PAGAR: R$ {:.2f}'.format(promo2file*0.95))
    print('Valor do desconto: R$ {:.2f}'.format(promo2file - (promo2file*0.95)))

if tipodeCARNE == "Alcatra" and qntddeCARNE <= 5 and pag == "Dinheiro":
    print('=== NOTA FISCAL ===')
    print('                                            ')
    print('Tipo de Carne: {}'.format(tipodeCARNE))
    print('Quantidade de Carne: {} KG'.format(qntddeCARNE))
    print('Valor da compra: R$ {:.2f}'.format(promo1alcatra))

if tipodeCARNE == "Alcatra" and qntddeCARNE <= 5 and pag == "Cartão Tabajara":
    print('=== NOTA FISCAL ===')
    print('                                            ')
    print('Tipo de Carne: {}'.format(tipodeCARNE))
    print('Quantidade de Carne: {} KG'.format(qntddeCARNE))
    print('Valor da compra: R$ {:.2f}'.format(promo1alcatra))

    print('DESCONTO DE 5%')

    print('TOTAL À PAGAR: R$ {:.2f}'.format(promo1alcatra*0.95))
    print('Valor do desconto: R$ {:.2f}'.format(promo1alcatra - (promo1alcatra*0.95)))

if tipodeCARNE == "Alcatra" and qntddeCARNE > 5 and pag == "Dinheiro":
    print('=== NOTA FISCAL ===')
    print('                                            ')
    print('Tipo de Carne: {}'.format(tipodeCARNE))
    print('Quantidade de Carne {} KG'.format(qntddeCARNE))
    print('Valor da compra R$ {:.2f}'.format(promo2alcatra))

if tipodeCARNE == "Alcatra" and qntddeCARNE > 5 and pag == "Cartão Tabajara":
    print('=== NOTA FISCAL ===')
    print('                                            ')
    print('Tipo de Carne: {}'.format(tipodeCARNE))
    print('Quantidade de Carne {} KG'.format(qntddeCARNE))
    print('Valor da compra R$ {:.2f}'.format(promo2alcatra))

    print('DESCONTO DE 5%')

    print('TOTAL À PAGAR R$ {:.2f}'.format(promo2alcatra*0.95))
    print('Valor do desconto R$ {:.2f}'.format(promo2alcatra - (promo2alcatra*0.95)))

if tipodeCARNE == "Picanha" and qntddeCARNE <= 5 and pag == "Dinheiro":
    print('=== NOTA FISCAL ===')
    print('                                            ')
    print('Tipo de Carne: {}'.format(tipodeCARNE))
    print('Quantidade de Carne {} KG'.format(qntddeCARNE))
    print('Valor da compra R$ {:.2f} '.format(promo1picanha))

if tipodeCARNE == "Picanha" and qntddeCARNE <= 5 and pag == "Cartão Tabajara":
    print('=== NOTA FISCAL ===')
    print('                                            ')
    print('Tipo de Carne: {}'.format(tipodeCARNE))
    print('Quantidade de Carne {} KG'.format(qntddeCARNE))
    print('Valor da compra R$ {:.2f} '.format(promo1picanha))

    print('DESCONTO DE 5%')

    print('TOTAL À PAGAR R${:.2f}'.format(promo1picanha))
    print('Valor do desconto R$ {:.2f}'.format(promo1picanha - (promo1picanha*0.95)))

if tipodeCARNE == "Picanha" and qntddeCARNE > 5 and pag == "Dinheiro":
    print('=== NOTA FISCAL ===')
    print('                                            ')
    print('Tipo de Carne: {}'.format(tipodeCARNE))
    print('Quantidade de Carne {} KG'.format(qntddeCARNE))
    print('Valor da compra R$ {:.2f} '.format(promo2picanha))

if tipodeCARNE == "Picanha" and qntddeCARNE > 5 and pag == "Cartão Tabajara":
    print('=== NOTA FISCAL ===')
    print('                                            ')
    print('Tipo de Carne: {}'.format(tipodeCARNE))
    print('Quantidade de Carne {} KG'.format(qntddeCARNE))
    print('Valor da compra R$ {:.2f} '.format(promo2picanha))

    print('DESCONTO DE 5%')

    print('TOTAL À PAGAR: R$ {}'.format(promo2picanha*0.95))
    print('Valor do desconto: R$ {:.2f}'.format(promo2picanha - (promo2picanha*0.95)))


















